from django.db import models

GENDER = (
   ('M', 'Male'),
   ('F', 'Female')
)

class TaxCalculator(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    gender=models.CharField(max_length=2,choices=GENDER, default=1)
