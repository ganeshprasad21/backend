from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings

def newGaneshPrasadR(request):
    print(settings.TEMPLATES)
    print(loader.get_template('webapp_another/w_a.html'))

    return render(request, 'webapp_another/w_a.html')

# Create your views here.
