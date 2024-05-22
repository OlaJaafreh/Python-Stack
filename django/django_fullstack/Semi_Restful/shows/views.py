from django.shortcuts import render,redirect
from .models import TVShows


def index(request):
    return render(request,"addshow.html")


def addshow(request):
    if request.method=='POST':
        title = request.POST['title']
        network = request.POST['network']
        releasedate = request.POST['releasedate']
        description = request.POST['description']
        new = TVShows.objects.create(title=title,network=network,releasedate=releasedate,description=description)
        return redirect('tvshow',new.id)
    return render(request,"addshow.html")


def allshow(request):
    shows = TVShows.objects.all()
    return render(request,"allshow.html",{'shows':shows})

def editshow(request,id):
    tvshow = TVShows.objects.get(id=id)
    if request.method=='POST':
        tvshow.title = request.POST['title']
        tvshow.network = request.POST['network']
        tvshow.releasedate = request.POST['releasedate']
        tvshow.description = request.POST['description']
        tvshow.save()
        return redirect('tvshow',id)
    
    return render(request,"editshow.html",{'show':tvshow})

def tvshow(request,id):
    tvshoww = TVShows.objects.get(id=id)
    return render(request,"tvshow.html",{'show':tvshoww})

def delete(request,id):
    tvshoww = TVShows.objects.get(id=id)
    tvshoww.delete()
    return redirect("/shows")