from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Genre_counter, Trending, Gender_age_counter
from django.core import serializers
import requests
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from community.models import Review, ShortReview
from django.db.models import Q
from community.forms import ShortReviewForm
from django.utils import timezone

# Create your views here.
def mainpage(request):
    return render(request, 'movies/mainpage.html')

def index(request):
    # trending
    if Trending.objects.all().filter(trendingdate = timezone.now()).exists():
        trending = Trending.objects.all().filter(trendingdate=timezone.now())[0]
        trending_movies = trending.movies.all()[:10]
    else:
        trending = Trending()
        trending.save()
        response = requests.get('https://api.themoviedb.org/3/trending/movie/day?api_key=9d1ff31749b9442fee29807f44a16275&language=ko-KR').json()
        results = response['results']
        for result in results:
            if Movie.objects.all().filter(pk=result['id']).exists():
                trending.movies.add(result['id'])
            else:
                movie = Movie()
                movie.pk = result['id']
                movie.ktitle = result['title']
                movie.popularity = result['popularity']
                movie.vote_average = result['vote_average']
                movie.vote_count = result['vote_count']
                movie.adult = result['adult']
                movie.poster_path = result['poster_path']
                movie.backdrop_path = result['backdrop_path']
                movie.original_language = result['original_language']
                movie.original_title = result['original_title']
                movie.genres = result['genre_ids']
                movie.koverview = result['overview']
                movie.release_date = result['release_date']
                english_response = requests.get(f'https://api.themoviedb.org/3/movie/{movie.pk}?api_key=9d1ff31749b9442fee29807f44a16275&language=en-US').json()
                movie.etitle = english_response['title']
                movie.eoverview = english_response['overview']
                movie.save()
                trending.movies.add(movie.pk)
        trending.save()
        trending_movies = trending.movies.all()[:10]

    #나이& 성별 선호도
    if request.user.is_authenticated:
        year = timezone.now().year - request.user.date_of_birth.year
        if year<20:
            year = '10'
        elif year<30:
            year = '20'
        elif year<40:
            year = '30'
        elif year<50:
            year = '40'
        else:
            year = '50'
        gender_age_counters =  Gender_age_counter.objects.all().filter(gender = request.user.gender, ages=year).order_by('-counter')
        gender_age_movies = []
        if request.user.gender  == 'F':
            gender = '여성'
        else:
            gender = '남성'
        for gender_age_counter in gender_age_counters:
            if gender_age_counter.movie not in gender_age_movies:
                gender_age_movies.append(gender_age_counter.movie)
            if len(gender_age_movies) ==10:
                break
    else:
        gender_age_movies = []
        gender = ''
        year = ''



    # 장르선호도
    if not request.user.is_authenticated:
        print('no')
        movies = Movie.objects.all().filter(vote_count__gte=350, vote_average__gte=8).order_by('-release_date')[:10]
        context = {
            'movies':movies,
            'trending_movies': trending_movies,
            'gender_age_movies' : gender_age_movies,
            'year' : year, 
            'gender' : gender,
        }
    else:
        genres = Genre_counter.objects.all().filter(user=request.user).order_by('-counter')
        if genres.count() == 0:
            movies = Movie.objects.all().filter(vote_count__gte=350, vote_average__gte=8).order_by('-release_date')[:10]
            context = {
                'movies' : movies,
                'trending_movies' : trending_movies,
                'gender_age_movies' : gender_age_movies,
                'year' : year, 
                'gender' : gender,
            }
        else:
            genre = genres[0].genre
            liked_movies = request.user.liked_movies.all()
            movies = list(Movie.objects.all().filter(genres=genre, vote_average__gte=7).order_by('-release_date'))
            picks = []
            for movie in movies:
                if movie in liked_movies or movie in picks:
                    continue
                picks.append(movie)
                if len(picks) == 5:
                    break
            if len(picks) < 10 and len(genres)>1:
                genre = genres[1].genre
                movies = list(Movie.objects.all().filter(genres=genre, vote_average__gte=7).order_by('-release_date'))
                for movie in movies:
                    if movie in liked_movies or movie in picks:
                        continue
                    picks.append(movie)
                    if len(picks) == 10:
                        break
            picks.sort(key=lambda x:x.vote_average, reverse=True)
            context = {
                'movies':picks,
                'trending_movies' : trending_movies,
                'gender_age_movies' : gender_age_movies,
                'year' : year, 
                'gender' : gender,
            }
    return render(request, 'movies/index.html', context)



def firstchoice(request):
    #추가 모델링이나 필요하다면 바로 말씀해주세요.
    genres = Genre.objects.all()
    context = {
        'genres': genres
    }
    return render(request, 'movies/firstchoice.html', context)

@login_required
def getmovies(request, name):
    genre = get_object_or_404(Genre, kname = name)
    movies = Movie.objects.filter(vote_average__gte=8).filter(genres__id=genre.pk).order_by('-popularity')[:50]
    data = serializers.serialize('json', movies)
    return HttpResponse(data)

@login_required
def movie_like(request, pk):
    user = request.user
    print('kita')
    gender = user.gender
    year = timezone.now().year - user.date_of_birth.year
    if year<20:
        year = '10'
    elif year<30:
        year = '20'
    elif year<40:
        year = '30'
    elif year<50:
        year = '40'
    else:
        year = '50'
    movie = get_object_or_404(Movie, pk=pk)
    if movie.liked_users.filter(pk=user.pk).exists():
        movie.liked_users.remove(user)
        for genre in movie.genres.all():
            genre_counter = Genre_counter.objects.all().filter(user=user, genre=genre)[0]
            genre_counter.counter -=1
            genre_counter.save()
        gender_age_counter = Gender_age_counter.objects.all().filter(gender=gender, ages=year, movie=movie)[0]
        gender_age_counter.counter -= 1
        gender_age_counter.save()
        liked = False
    else:
        movie.liked_users.add(user)
        for genre in movie.genres.all():
            if Genre_counter.objects.all().filter(user=user, genre=genre).exists():
                genre_counter = Genre_counter.objects.all().filter(user=user, genre=genre)[0]
                genre_counter.counter += 1
                genre_counter.save()
            else:
                genre_counter = Genre_counter()
                genre_counter.user = user
                genre_counter.genre = genre
                genre_counter.counter = 1
                genre_counter.save()
        if Gender_age_counter.objects.all().filter(gender=gender, ages=year, movie=movie).exists():
            gender_age_counter = Gender_age_counter.objects.all().filter(gender=gender, ages=year, movie=movie)[0]
            gender_age_counter.counter += 1
            gender_age_counter.save()
        else:
            gender_age_counter = Gender_age_counter()
            gender_age_counter.gender = user.gender
            gender_age_counter.ages = year
            gender_age_counter.movie = movie
            gender_age_counter.save()
        liked = True
    data = {
        'liked':liked,
        'count':movie.liked_users.count()
    }
    return JsonResponse(data)

def search(request):
    keyword = request.GET['keyword']
    movies = Movie.objects.all().filter(Q(ktitle__icontains=keyword) |
     Q(etitle__icontains=keyword) | Q(koverview__icontains=keyword) | Q(eoverview__icontains=keyword)).distinct().order_by('ktitle')
    reviews = Review.objects.all().filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(user__nickname__icontains=keyword))
    User = get_user_model()
    users = User.objects.all().filter(Q(username__icontains=keyword) | Q(nickname__icontains=keyword))
    context = {
        'movies' : movies,
        'users' : users,
        'reviews' : reviews
    }
    return render(request, 'movies/search.html', context)
    

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    shortreviews = ShortReview.objects.all().filter(movie = movie)
    shortreviewForm = ShortReviewForm()
    reviews = Review.objects.all().filter(movie = movie)
    context = {
        'movie':movie,
        'shortreviews':shortreviews,
        'reviews':reviews,
        'shortreviewForm': shortreviewForm,
    }
    return render(request, 'movies/detail.html', context)


def togenre(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    context = {
        'movies':movies,
        'genres':genres,
    }
    return render(request, 'movies/choicegenre.html', context)



