from django.contrib import admin
from django.urls import path
from .views import helloworld, hellostudent, increment, decrement, reset

urlpatterns = [
    path('helloworld/', helloworld),
    path('hellostudent/', hellostudent),
    path('increment/', increment),
    path('decrement/', decrement),
    path('reset/', reset)
]
