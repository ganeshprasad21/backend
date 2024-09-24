from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render as rr
from .models import Movie
import random

movies = [
  {
    'name': 'upendra',
    'rating': "5*",
    'awards': "yes",
  },
  {
    'name': 'uppi',
    'rating': "3*",
    'awards': "no",
  },
  {
    'name': 'kgf',
    'rating': "5*",
    'awards': "yes",
  },
]

demo_data = {
  # 'movies' : movies, #demo
  'movies' : Movie.objects.all(), #db

}


def movies_list(request):
  demo_data = {
  # 'movies' : movies, #demo
  'movies' : Movie.objects.all(), #db
  }
  return rr(request,'demoapp/dempapp_movies_list_template.html', demo_data)

def movie_detail_fetch(request,id):
  data = Movie.objects.get(pk=id)
  demo_data = {
  'movies' : data,
  'id': id,
  }
  return rr(request,'demoapp/demoapp_one_movie_detail.html', demo_data)

def add_movie(request):
  data = request.POST
  name = request.POST.get("name")
  print(name)
  ratings = request.POST.get("ratings")
  awards = request.POST.get("awards")
  year = request.POST.get("year")
  if name is not None:
    movie = Movie(name=name,ratings=ratings,awards=awards,year=year)
    movie.save()

  demo_data = {
  'movies' : data}
  print(data)
  return rr(request,'demoapp/add_movie.html')

def delete_movie(request,id):
  Movie.objects.get(pk=id).delete() #carefull
  return rr(request,"demoapp/delete_movie.html")

