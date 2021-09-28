from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='db_project-home'),
    path('about/', views.about, name='db_project-about'),
]