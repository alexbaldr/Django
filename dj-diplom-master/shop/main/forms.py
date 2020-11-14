from django import forms
from main.models import Review, Article
from ckeditor.widgets import CKEditorWidget


class ReviewForm(forms.ModelForm):
    text = forms.CharField(label='Содержание', required=False)
    score = forms.IntegerField(max_value=5, min_value=1, required=True)

    class Meta:
        model = Review
        fields = ('name', 'score')


class ArticleForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget(),
                           label='Содержание', required=False)

    class Meta:
        model = Article
        fields = ('name', 'text', 'product')
