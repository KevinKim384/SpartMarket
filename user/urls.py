from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup')
    
]
