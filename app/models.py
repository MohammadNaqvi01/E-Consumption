from django.db import models
from django.contrib.auth.models import User
# Create your models here


CHOICES=(

('Hw','Heavy'),
('Lt','Light'),
  

)

class Feature(models.Model):
    unique=models.CharField(max_length=130) 
    timein=models.IntegerField(null=True,max_length=50)
    timeout=models.IntegerField(null=True,max_length=50)
    appliance=models.CharField(max_length=50)
    kwh=models.PositiveIntegerField()
    state=models.CharField(max_length=12,default='')
    e_consumption=models.CharField(null=True,max_length=50)
    bill=models.CharField(null=True,max_length=50)

class Otp(models.Model):

    unique=models.CharField(max_length=130)
    email=models.CharField(max_length=130)
    otp=models.PositiveIntegerField()
    password=models.CharField(max_length=130)


class Appliance(models.Model):
    name=models.CharField(max_length=12,null=True)
    image=models.ImageField(upload_to='producting')
    category=models.CharField(choices=CHOICES,max_length=10)
    kwh=models.PositiveIntegerField() 

class CustomAppliance(Appliance):
    unique=models.ForeignKey(Otp,on_delete=models.CASCADE)
    


