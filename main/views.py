from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .forms import RegistrationForm
from .models import Student
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
@login_required(login_url="/login")
def HomePage(request):
    return render(request, "registration/home.html", {})


def Register(request):
    #If the request is a post method (Form submission)
    if request.method == "POST":
        #Extracting the submitted form
        form = RegistrationForm(request.POST)
        #If the form is valid
        if form.is_valid():
            #Calling the save method that will return a user instance with details binded to the user instance
            user = form.save()
              #Creating a instance of the group to be assigned
            student_group = Group.objects.get(name='Student')
            user.groups.add(student_group)
            Student.objects.create(first_name = user.first_name, last_name = user.last_name)
            #calling inbuilt method for login authentication.
            login(request, user)
            #Setting up a message to show in the redirected page.
            messages.success(request, "Successfully registered.")
            return redirect("main:home")
        else:
            messages.error(request, "Invalid information. Try again!")
            return redirect("main:home")
    # If the request is a get request, new form is rendered.
    form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid credentials")
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})

def Logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:login")