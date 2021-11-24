from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('',Home,name="home"),
    path('energy/',RestHome,name="rest_home"),
    path('signup/',Signup,name="signup"),
    path('profile/',Profile.as_view(),name='profile'),
    
    path('signup/verification/',Verification,name="login"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)