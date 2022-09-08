from django.shortcuts import render,redirect

def studentbase(request):
    return render(request,"STUDENT/studentbase.html")

def home(request):
    return render(request,'STUDENT/home.html')