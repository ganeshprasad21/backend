from django.urls import path
from . import views

urlpatterns = [
    path('movies_list', views.movies_list),
    path('add_movie', views.add_movie),
    path('delete_movie_id_<int:id>', views.delete_movie),
    path('movies_list_singl_<int:id>', views.movie_detail_fetch),
]