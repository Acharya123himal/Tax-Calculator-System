from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class Feedback(models.Model):
    sender=models.CharField(max_length = 150,verbose_name = "Name")
    email=models.EmailField(verbose_name = "Email")
    message = RichTextField(verbose_name = "Message")
    tel= models.CharField(max_length = 10,verbose_name = "Phone")
    date_sent=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_sent']