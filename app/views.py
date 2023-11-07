from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Priya(request):
    return HttpResponse('<h1><marquee>Hi Priya!How are you?</marquee></h1>')