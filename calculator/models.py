from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class TaxCalculator(models.Model):
   email=models.EmailField(_('email address'),unique=True)
   first_name=models.CharField(_('First Name'),max_length=150)
   last_name=models.CharField(_('Last Name'),max_length=150)
   date_calculated=models.DateTimeField(default=timezone.now)
   gender = models.CharField(_("Gender"), max_length=10, choices=(('male', _('Male')), ('female', _('Female')),('trans', _('Transgender'))),  blank=True, null=True)
   address = models.CharField(max_length=150, blank=True, default='')
   state = models.CharField(max_length=150, blank=True,choices=(('1', _('1')), ('2', _('2')), ('3', _('3')),('4', _('4')),('5', _('5')),('6', _('6')),('7', _('7'))), default='')
   telephone = models.CharField(_("Telephone"), max_length=10,blank=True, null=True)
   marital = models.CharField(_("Marital Status"), max_length=10, choices=(('married', _('Married')), ('unmarried', _('Unmarried'))), blank=True, null=True)
   resident = models.CharField(_("Resident status"), max_length=10, choices=(('resident', _('Resident')), ('rental', _('Rental'))), blank=True, null=True)
