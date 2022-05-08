from django import forms
from .models import Blog
from django.forms import ModelForm
class BlogForm(forms.ModelForm):
    title = forms.TextInput()
    blog_image = forms.ImageField()
    content=forms.TextInput()
    class Meta:
        model = Blog
        fields = ["title","content","blog_image"]