from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('about', views.about_page, name='about'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my-tasks', views.my_tasks, name='my-tasks'),
    path('delete-task/<int:pk>', views.delete_task, name='delete-task'),
    path('edit-task/<int:pk>', views.edit_task, name='edit-task'),
    path('update-status/<int:pk>', views.update_status, name='update-status'),
    path('profile', views.profile_view, name='profile'),
    # Path to change password
    path('profile/change_password/', views.change_password, name='change_password'),
]