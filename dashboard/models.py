from django.db import models
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import os
from uuid import uuid4
class Mail(models.Model):
    subject = models.CharField(max_length = 50,verbose_name = "Subject")
    email = models.EmailField(verbose_name = "Email")
    message = RichTextField()

from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):
    def _save(self,name, content):
        if self.exists(name):
            self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self,name,max_length=None):
        return name

def path_and_rename(instance, filename):
    upload_to = 'static'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('logo', 'png')
    return os.path.join(upload_to, filename)

class Settings(models.Model):
    logo=models.ImageField(upload_to=path_and_rename,storage=OverwriteStorage(),verbose_name="Logo",default="static/logo.png")
    fonts = models.CharField(_("Fonts"), max_length=10,  blank=True, null=True)