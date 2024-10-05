from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Task

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter your username'
        #     }),
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter your email'
        #     }),
        #     'password1': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter your password'
        #     }),
        #     'password2': forms.PasswordInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Confirm your password'
        #     }),
        # }
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority',]
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

        # widgets = {
        #     'due_date': forms.DateInput(attrs={'type': 'date'}),
        # }