from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()
    return render(request, "index.html", {"dojos": dojos, "ninjas": ninjas})

def ninja(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        dojo_name = request.POST.get("dojo")  
        dojo = Dojo.objects.get(name=dojo_name)
        # if first_name=="" or last_name =="" :
        #     return render(request, "index.html")
        Ninja.objects.create(first_name=first_name, last_name=last_name, dojo=dojo)
        return redirect("index")
    return render(request, "index.html")

def dojo(request):
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        state = request.POST.get("state")
        # if name=="" or city =="" or state =="":
        #     return render(request, "index.html")
        Dojo.objects.create(name=name, city=city, state=state)
        return redirect("index")
    return render(request, "index.html")
