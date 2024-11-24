from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my-tasks', views.my_tasks, name='my-tasks'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit-task'),
    path('update-status/<int:pk>', views.update_status, name='update-status'),
]