from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.template import loader
from django.contrib import sessions


def index(request):
    datetime = str(timezone.now().date())+" "+str(timezone.now().time())
    template = loader.get_template('smartmirror/index.html')
    context = {
        "datetime": datetime,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
