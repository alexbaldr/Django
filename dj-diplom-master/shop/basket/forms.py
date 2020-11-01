from django import forms

PRODUCT_QUANTITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class CartAddForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int, label='Количество')
    override = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)

# class CartAddFormForMain(forms.Form):
