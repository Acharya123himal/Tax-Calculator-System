from django import forms
from .models import User

class profilepictureForm(forms.ModelForm):
    """Form to add profile picture to User model."""

    class Meta:
        model = User
        fields = ('profile_pic', )
        
class UserForm(forms.ModelForm):
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name=forms.CharField()
    gender = forms.Select()
    address = forms.CharField()
    state = forms.Select()
    username = forms.CharField()
    telephone = forms.CharField()
    marital = forms.Select()
    resident = forms.Select()
    
    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","gender","marital","resident","address","state","telephone"]