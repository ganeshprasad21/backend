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
        # myDict = {
        #       'keyone':"val of key 1",
        #       'keyanother':"val of key 1",
        #       'keythree':"val of key 1",
        #       'keyfour':"val of key 1",
        #       'keyfive':"val of key 1",
        #       'keysix':"val of key 1",
        # }
        myDict = ["item1","item 2","item3"]
        context = {'num':num, 'myDict': myDict}
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