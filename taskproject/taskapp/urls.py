from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('index/', views.index, name='index'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/update/<int:pk>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
]