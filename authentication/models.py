from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password, **other_fields):
        if not (email or first_name or last_name or password):
            return ValueError(_('You must provide all details'))
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password,**other_fields):
        if not (email or first_name or last_name or password):
            return ValueError(_('You must provide all details'))
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
        if other_fields.get('is_staff') is not True:
            return ValueError('Superuser must be assigned true as staff')
        if other_fields.get('is_active') is not True:
            return ValueError('Superuser must be assigned true as active')
        return self.create_user(email,username,first_name,last_name,password,**other_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(_('email address'),unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    first_name=models.CharField(_('First Name'),max_length=150)
    last_name=models.CharField(_('Last Name'),max_length=150)
    date_joined=models.DateTimeField(default=timezone.now)
    gender = models.CharField(_("Gender"), max_length=1, choices=(('1', _('Male')), ('2', _('Female')),('3', _('Transgender'))),  blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, default='')
    state = models.IntegerField(_("state"), blank=True, null=True)
    username = models.CharField(max_length=150, unique=True)
    tel = models.CharField(_("tel"), max_length=10,blank=True, null=True)
    marital = models.CharField(_("Marital Status"), max_length=1, choices=(('1', _('Married')), ('2', _('Unmarried'))), blank=True, null=True)
    resident = models.CharField(_("Resident status"), max_length=1, choices=(('1', _('Resident')), ('2', _('Resident'))), blank=True, null=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_blocked=models.BooleanField(default=False)
    objects=CustomAccountManager()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','first_name','last_name']
    
    def __str__(self):
        return self.email
    