from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import datetime as dt
from .models import Profile,Image
from django.contrib.auth.models import User

#Create your views here
def welcome(request):
    return render(request,'welcome.html')
