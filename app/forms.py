from django import forms
    

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserSignup(UserCreationForm):

#  phone=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','autofocus':'','type':'tel','pattern':'[0-9]{10}'}))
  
   password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
   email=forms.EmailField(required=True,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
#overriding password input's class of UserCreationForm and adding email field



   class Meta:
      model=User
      #fields of models to use + explicitly declared fields  
      fields=['username','email','password1','password2']

     
 
      # to set field attributes for model fields which are generated automatically modelform

      widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class OtpForm(forms.Form):

   
      input1=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
      input2=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
      input3=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))
      input4=forms.CharField(max_length=1, label='',widget=forms.TextInput(attrs={'class':'form-control','autofocus':''}))

     