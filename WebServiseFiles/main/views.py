from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'main/home.html')


