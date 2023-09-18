from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.

def HomePage(request):
    return HttpResponse("Welcome to home page!")

def Register(request):
    #If the request is a post method (Form submission)
    if request.method == "POST":
        #Extracting the submitted form
        form = RegistrationForm(request.POST)
        #If the form is valid
        if form.is_valid():
            #Calling the save method that will return a user instance with details binded to the user instance
            user = form.save()
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
