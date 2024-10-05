from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)  # Get tasks for the logged-in user
    return render(request, 'taskapp/index.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Bind the form to the POST data
        if form.is_valid():
            task = form.save(commit=False)  # Save the task but don't commit to the database yet
            task.user = request.user  # Set the user to the logged-in user
            task.save()  # Now save to the database
            return redirect('index')  # Redirect to the index page after successful creation
        else:
            print(form.errors)  # Log the errors to the console for debugging
    else:
        form = TaskForm()  # Initialize an empty form

    return render(request, 'taskapp/create_task.html', {'form': form})


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Bind the form to the existing task instance
        if form.is_valid():  # Validate the form
            form.save()  # Save the updated task
            return redirect('index')  # Redirect to index after saving
    else:
        form = TaskForm(instance=task)  # Create a form instance with the existing task data

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration
        else:
            messages.error(request, 'Please correct the errors below.')  # Notify the user of form errors
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
