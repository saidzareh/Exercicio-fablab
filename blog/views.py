from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chiclete(request):

    return render(request,template_name='blog/home.html')

def jujuba(request):
    html = '<html><body><h1>Coma Jujuba<h1></boldy></html'
    return HttpResponse(html)