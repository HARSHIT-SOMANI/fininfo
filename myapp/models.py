
import numbers
from django.db import models

# Create your models here.

class details(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    flat=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    dob=models.DateField(null=True)
    
