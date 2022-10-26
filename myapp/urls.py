from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path('myfirstexample/',views.fun1,name="firstexample"),
    path('myfirstpage/' ,views.fun2,name="myfirstweb"),
    path('imagepage/' ,views.fun3,name="myimagepage")
]