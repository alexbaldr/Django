from django import  forms
from django.shortcuts import redirect, render
from registration.forms import regForm
from django.contrib.auth.models import User


def signup(request):
    form = regForm()
    if request.method == "POST":
        form = regForm(request.POST)
        if form.is_valid():
            login = request.POST.get("login")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            mail_ad = request.POST.get("email")

            if password2 == password1:
                user = User.objects.create_user(username=login, email=mail_ad, password=password1)
                if mail_ad != User.objects.get(email = mail_ad):
                    user.save()
                    return redirect(request.build_absolute_url())
                else: 
                    raise forms.ValidationError("User already exist")
            
            else: 
                raise forms.ValidationError("Passwords don't match")         
    else:
        return render(request, 'registration/signup.html', {'form':form} )
