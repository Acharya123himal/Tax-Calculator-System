from django.db import models
from ckeditor.fields import RichTextField
class Mail(models.Model):
    sender = models.CharField(max_length = 50,verbose_name = "Name")
    subject = models.CharField(max_length = 50,verbose_name = "Subject")
    email = models.EmailField(verbose_name = "Email")
    message = RichTextField()

class Settings(models.Model):
    image=models.ImageField(upload_to="uploads")