from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Feature)
class FeatureAdminModel(admin.ModelAdmin):
    list_display=['id','unique','timein','timeout','appliance','kwh','state','e_consumption']

@admin.register(Appliance,CustomAppliance)
class AdminModel(admin.ModelAdmin):
    list_display=['id','name','category','kwh','image']


 

@admin.register(Otp)
class OtpAdminModel(admin.ModelAdmin):
    list_display=['id','unique','email','otp','password']