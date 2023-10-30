from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth

@has_permission_decorator('home')
def home(request):
   return render(request, 'home.html')
        