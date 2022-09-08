from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def home(request):
    return render(request, 'Admin/home.html')

@login_required(login_url='/')
def addstudent(request):
    return render(request, 'Admin/addstudent.html')