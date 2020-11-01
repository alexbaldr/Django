from django import forms

from main.models import Review

class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Содержание', required=False)
    score = forms.IntegerField(max_value=5, min_value=1, required=True)  # widget=forms.HiddenInput


    class Meta:
        model = Review
        fields = ('name', 'score')