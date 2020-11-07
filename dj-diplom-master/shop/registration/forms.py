from django import forms
from django.contrib.auth.models import User


class loginForm(forms.Form):
    email = forms.EmailField(required=True,
                             label="Укажите ваш электронный адрес")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput,
                               label="Пароль")


class regForm(forms.Form):
    login = forms.CharField(max_length=20, label="Имя пользователя")
    password1 = forms.CharField(max_length=20, label="Придумайте пароль",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, label="Подтвердите пароль",
                                widget=forms.PasswordInput)
    email = forms.EmailField(required=True,
                             label="Укажите ваш электронный адрес")

    class Meta:
        model = User
        fields = ('username', 'email')
