from django import forms
from .models import Product

class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        Widgets={
            'Date':forms.SelectDateWidget()
        }

