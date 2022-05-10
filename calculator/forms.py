from django import forms
from .models import TaxCalculator
from django.forms import ModelForm
class CalculatorForm(forms.ModelForm):
    tax = forms.TextInput()
    class Meta:
        model = TaxCalculator
        fields = ["tax"]