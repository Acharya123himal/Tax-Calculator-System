from django import forms
from .models import Feedback
from django.forms import ModelForm
class FeedbackForm(forms.ModelForm):
    sender = forms.TextInput()
    email = forms.EmailField()
    message=forms.TextInput()
    tel = forms.TextInput()
    class Meta:
        model = Feedback
        fields = ["sender","tel","email","message"]