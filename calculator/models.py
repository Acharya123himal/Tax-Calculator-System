from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class TaxCalculator(models.Model):
   email=models.EmailField(_('email address'))
   tax=models.CharField(_('Tax'),max_length=150)
   date_calculated = models.DateTimeField(auto_now_add=True,verbose_name="Calculated On:")
   