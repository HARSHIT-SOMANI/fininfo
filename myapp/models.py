
from django.db import models
import os
import datetime
# Create your models here.

def filepath(request,filename):
    old_filename=filename
    timeNow=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename="%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)
class details(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    flat=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    dob=models.DateField(null=True)
    image=models.ImageField(upload_to=filepath,null=True,blank=True)
    
