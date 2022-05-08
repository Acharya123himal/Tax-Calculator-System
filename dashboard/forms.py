from django import forms
from .models import Mail
from django.forms import ModelForm

class MailForm(forms.ModelForm):
    sender = forms.TextInput()
    email=forms.EmailField()
    message = forms.TextInput()
    subject = forms.TextInput()
    class Meta:
        model = Mail
        fields = ["sender","subject","email","message"]