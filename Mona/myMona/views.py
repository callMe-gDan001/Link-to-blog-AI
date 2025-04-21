from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "index.html")

def Signup(request):
    return render(request, "signup.html")

def Login(request):
    return render()