from django.shortcuts import render

# Create your views here.

def bs(request):
    return render(request,'bs.html')

def home(request):
    return render(request,'home.html')


def link(request):
    return render(request,'link.html')