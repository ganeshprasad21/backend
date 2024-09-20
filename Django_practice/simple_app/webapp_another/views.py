from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings

def newGaneshPrasadR(request):
    template = loader.get_template('w_a.html')
    return HttpResponse(template.render())

# Create your views here.
