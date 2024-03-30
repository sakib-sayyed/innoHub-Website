from django.shortcuts import render,redirect
from .models import Services

def home(request):
    return render(request,"home.html")

def services(request):
    services = Services.objects.all()
    return render(request,'services.html',{'services':services})

def aboutUs(request):
    return render(request,'aboutUs.html')

def team(request):
    return render(request,'team.html')

def contactUs(request):
    return render(request,'contactUs.html')