from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.settings import LOGIN_REDIRECT_URL
from .forms import loginForm, regForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django import forms


def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    form = regForm()
    if request.method == "POST":
        form = regForm(request.POST)
        if form.is_valid():
            login = request.POST.get("login")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            mail_ad = request.POST.get("email")
            # form.save()
            if password2 == password1:
                user = User.objects.create_user(username=login, email=mail_ad, password=password1)
                if mail_ad != User.objects.get(email = mail_ad):
                    user.save()
                    return render(
                        request,
                        'home.html')
                else: 
                    raise forms.ValidationError("User already exist")
            
            else: 
                raise forms.ValidationError("Passwords don't match")
                # return render(request, 'signup.html', {'form':form} )
            
    else:
        return render(request, 'signup.html', {'form':form} )


def login_view(request):
    formin = loginForm
    if request.method ==  "POST":
        formin = loginForm(request.POST)
        if formin.is_valid():
            cd = formin.cleaned_data

            user = authenticate(username=cd["login"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(
                    request,
                    'home.html'
                        )
                else:
                    return render(request, 'login.html', {'formin':formin} )
            else:
                    return render(request, 'login.html', {'formin':formin} )
    else:
        # formin = loginForm()
        return render(request, 'login.html', {'formin':formin} )

def logout_view(request):
    template_name = "logout.html"
    logout(request)
    return render(request, template_name)