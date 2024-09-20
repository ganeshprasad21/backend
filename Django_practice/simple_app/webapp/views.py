from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.template.loader import get_template
import random

def ganesh_prasad_r(request):
    # try:
        # template = get_template('w_.html')
        # return HttpResponse(template.render())
        num = str(random.randint(3,303)) 
        print(num)
        context = {'num':num, }
        template = get_template('w_.html')
        res = template.render(context,request)
        # print(HttpResponse(res))
        return HttpResponse(res)
        # # return template.render()


    
def testGlobalTemplate(request):
    return get_template('w_.html').render()



# def ganesh_prasad_r(request):
#     string="hey there man this is ganesh prasad r!!!"
#     return HttpResponse(string)