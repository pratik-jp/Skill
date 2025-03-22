from django.shortcuts import render,redirect

def Base(request):
    return render(request,'base.html')

def Home(request):
    return  render(request,'main.html')