from django import forms

class loginForm(forms.Form):
    login = forms.CharField(max_length=20, label = "Имя пользователя")
    password = forms.CharField(max_length=20, label = "Пароль")
    
class regForm(forms.Form):
    login = forms.CharField(max_length=20, label = "Имя пользователя")
    password1 = forms.CharField(max_length=20, label = "Придумайте пароль")
    password2 = forms.CharField(max_length=20, label = "Подтвердите пароль")
    email = forms.EmailField(required=False, label = "Укажите ваш электронный адрес")
    
