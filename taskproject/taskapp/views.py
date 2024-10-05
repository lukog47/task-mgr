from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone

from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, CustomUserCreationForm
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskapp/index.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_at = timezone.now()
            task.user = request.user
            task.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = TaskForm()

    return render(request, 'taskapp/create_task.html', {'form': form})


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)

    return render(request, 'taskapp/update_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'taskapp/delete_task.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})