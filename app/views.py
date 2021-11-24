
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponseRedirect, JsonResponse
from .models import *
from .serializers import *
from django.views import View
from datetime import datetime
from app.forms import *
import time
import smtplib

def Home(request):
   appliances=Appliance.objects.all()
   
   return render(request,'app/home.html',{'appliances':appliances})


class Profile(View):
    def get(self,request):
       pass
    def post(request):
       pass



def Signup(request):
     if request.method=="GET":
       print("#######################")
       form=UserSignup()
       request.session['user']='user'
       return render(request,'app/signup.htm',{'form':form})
     
     if request.method=="POST": 
   
              form=UserSignup(request.POST)
              
         
              
              if form.is_valid():
                
                form.save()
                email=form.cleaned_data['email']
                pwd=form.cleaned_data['password1']
                
                
                form=OtpForm()
                code="1234"
                Otp(unique=request.COOKIES['sessionid'],email=email,otp=code,password=pwd).save()
                request.session['email']=email
                # Python code to illustrate Sending mail from
# your Gmail account             
                

# creates SMTP session
                s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
                s.starttls()

# Authentication
                s.login("email", "pass")

# message to be sent
                message = code

# sending the mail
                s.sendmail("",email, message)

# terminating the session
                s.quit()

                return HttpResponseRedirect('verification/')
              else :
                 
               
                 return render(request,'app/signup.htm',{'form':form})
            



def Verification(request):
        
         if request.method=="GET":
         
            form=OtpForm()
            return render(request,'app/otpverification.htm',{'otpform':form,'email':request.session['email']})
      

         if request.method=="POST":
            
            
            form=OtpForm(request.POST)
            if form.is_valid():
               var1=form.cleaned_data['input1']
               var2=form.cleaned_data['input2']
               var3=form.cleaned_data['input3']
               var4=form.cleaned_data['input4']
               otp=int(var1+var2+var3+var4)
               
               if Otp.objects.filter(Q(unique=request.COOKIES['sessionid'])&Q(otp=otp)).exists() :
                   take=Otp.objects.get(Q(unique=request.COOKIES['sessionid'])&Q(otp=otp))
                   usr=User.objects.get(email=take.email)
                   login(request,usr)
                   return HttpResponseRedirect('/')
            else:
               form=OtpForm()
               return render(request,'app/otpverification.htm',{'otpform':form,'email':request.session['email']})
      



def RestHome(request):
        timing=time.time()
        device=request.GET['appliance']
        state=request.GET['state']
        print(device)
        print(state)
        device2=device.split("_")
        
        name=device2[0]
        kwh=device2[1]
 
    
      
        if state=="On":
                 
              #When clicked On button twice
            #   if Rest.objects.filter(Q(unique=unique)& Q(appliance=name) & Q(kwh=kwh)).exists():
            #      data={
            #      'state':'Already On'
            #       }
            #      return JsonResponse(data)
              
            #   #Clicked On first time
            #   else:
              
              #Clicked On first time
              data={
               'state':'On'
             }
         
              
              Feature(unique=request.COOKIES['sessionid'],timein=timing,appliance=name,kwh=kwh,state=state).save()
              return JsonResponse(data)
        else:
             
            #  if (Rest.objects.filter(Q(unique=unique)& Q(appliance=name) & Q(kwh=kwh))).exists() and :
            #      data={
            #      'state':'Already Off'
            #       }
            #      return JsonResponse(data)
            #  else:
            

             #Clicked OFF first time
             data={
               'state':'Off'
             }
             
           
             change=Feature.objects.get(Q(unique=request.COOKIES['sessionid'])& Q(appliance=name) & Q(kwh=kwh))
             change.timeout=timing
             change.state=state
             
             e_time_in_secs=change.timeout-change.timein
             e_time_in_hrs=e_time_in_secs/3600
             e_consumption=(change.kwh*(e_time_in_hrs/1000))
             change.e_consumption=e_consumption
            
             change.save()
             
             data['consumption']=round(e_consumption,4)
             data['secs']=int(e_time_in_secs)
             return JsonResponse(data)

def Result(request):
   return render()         
         

         
    #json_data,"application/json"