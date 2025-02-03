from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from SG import views

urlpatterns = [
 
    path('',views.HomePage, name='home'),
    path('About-us/',views.AboutPage, name='about-us'),
    path('Menu/',views.MenPage, name='menu'),
    path('Franchasi/',views.FranchasiPage, name='franchasi'),
    path('Contact/',views.ContactPage, name='contact'),
    
    
]
