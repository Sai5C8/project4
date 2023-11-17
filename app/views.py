from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sai(request):
    return HttpResponse('<h1>sai is good boy</h1>')
def nag(request):
    return render(request,'nag.html')