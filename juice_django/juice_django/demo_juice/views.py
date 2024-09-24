from django.shortcuts import render
from django.shortcuts import render
from .models import Juice
from .serializer import JuiceSerializer
from django.http import JsonResponse

# Create your views here.
def juices(request):
  return render(request,'demo_juice/demo_juice.html')

def get_juices(request):
  #get juices   
  juices = Juice.objects.all()
  juice_serializer = JuiceSerializer(juices, many=True)
  return JsonResponse(juice_serializer.data, safe=False)