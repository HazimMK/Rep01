from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return HttpResponse('You have created a web application'),

def fun2(request):
    return render(request,"tmp.html"),

def fun3(request):
    return render(request,"profile.html")