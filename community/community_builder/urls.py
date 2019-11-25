from django.contrib import admin
from django.urls import path
from user import views as user_views
from . import views

urlpatterns = [
    path('', views.home, name='community-about'),
    path('about/', views.about, name='community-home'),
    path('register/', user_views.register, name='register'),

]