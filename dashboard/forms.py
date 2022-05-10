from django import forms
from .models import Mail, Settings
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class MailForm(forms.ModelForm):
    email=forms.EmailField()
    message = forms.TextInput()
    subject = forms.TextInput()
    class Meta:
        model = Mail
        fields = ["subject","email","message"]
        
class SettingsForm(forms.ModelForm):
    logo=forms.ImageField()
    gender = forms.CharField(widget=forms.RadioSelect(choices=[('1', _('Roboto')), ('2', _('Montserrat')),('3', _('Open Sans'))]))

    class Meta:
        model=Settings
        fields=["logo","gender"]