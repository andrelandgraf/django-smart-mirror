from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    datetime = str(timezone.now().date())+" "+str(timezone.now().time())
    return HttpResponse("Hello World: "+datetime)

# Create your views here.
