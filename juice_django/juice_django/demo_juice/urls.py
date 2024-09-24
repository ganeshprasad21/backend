from django.urls import path
from . import views

urlpatterns = [
    path('juices', views.juices),
    path('get_juices', views.get_juices),

    
]