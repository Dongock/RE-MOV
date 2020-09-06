from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name="index"),
    path('firstchoice/', views.firstchoice, name='firstchoice'),
    path('getmovies/<str:name>', views.getmovies, name='getmovies'),
    path('<int:pk>/movie_like/', views.movie_like, name='movie_like'),
    path('<int:pk>/', views.detail, name='detail'),
    path('togenre/', views.togenre, name='togenre'),
]