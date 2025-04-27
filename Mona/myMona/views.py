from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


### AUTHENTICATION BEGIN

def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['password']
        cpwd = request.POST['confirmPassword']
        
        if pwd == cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "This username exists... try again")
                return redirect("Signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email exists... try again")
                return redirect("Signup")
            else:
                user = User.objects.create_user(username=username, password=pwd, email=email)
                user.save()
                return redirect("Login")
        else:
            return render(request, "signup.html")
    else:
        messages.info(request, "Something went wrong... try again")
        return render(request, "signup.html")

def Login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        # user = User.objects.filter(username=username, password=password).exists()
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Incorrect username or password")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def Logout(request):
    logout(request)
    return redirect("/")


### AUTHENTICATION ENDED


@csrf_exempt
def generate_blog(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            yt_link = data.get('link')
            print(yt_link)
            
            return JsonResponse({"content": "Blog successful!"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
            
            
    return JsonResponse({"error": "Invalid request method"}, status=405)
