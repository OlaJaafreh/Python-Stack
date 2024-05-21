from django.shortcuts import render,redirect
from .models import Actor,Movie,Movie_has_Actor,Category
from django.db.models import Count

def index(request):
    categories = Category.objects.all()
    actors = Actor.objects.all()
    movies = Movie.objects.all()
    actors = Actor.objects.annotate(movie_count=Count('movies'))
    return render(request,"index.html",{'categories': categories, 'actors': actors, 'movies': movies})

def movies(request):
    movie_name = request.post.get('movie_name')
    movie_desc = request.post.get('movie_desc')
    movie_img = request.post.get('movie_img')
    actor_name = request.post.get('actor_name')
    actor = Actor.objects.get(name =actor_name)
    cat_name = request.post.get('cat_name')
    cat = Category.objects.get(name=cat_name)
    Movie.objects.create(title = movie_name,description=movie_desc,url_img=movie_img,cat=cat,act=actor)
    return redirect('index')
