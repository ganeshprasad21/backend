from django.shortcuts import render
from django.http import HttpResponse
def ganesh_prasad_r(request):
    string="hey there man this is ganesh prasad r!!!"
    return HttpResponse(string)