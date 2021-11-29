from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='db_project-home'),
    path('substore', views.substore, name='list-substore'),
    path('store', views.store, name='list-store'),
    path('registration', views.registration, name='db_project-registration'),
    path('login', auth_views.LoginView.as_view(template_name='db_project/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='db_project/logout.html'), name='logout')
]