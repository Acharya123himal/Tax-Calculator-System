from django import forms
from .models import User
class profilepictureForm(forms.ModelForm):
    """Form to add profile picture to User model."""

    class Meta:
        model = User
        fields = ('profile_pic', )