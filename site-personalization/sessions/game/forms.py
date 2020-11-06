from django import forms
# from game.models import Player,Game


class PostForm(forms.Form):
    number = forms.IntegerField(label="Тут, ты должен загадать число", max_value=10, min_value=1)


class GuessForm(forms.Form):
    second_number = forms.IntegerField(label="Тут, ты должен отгадать число", max_value=10, min_value=1)
