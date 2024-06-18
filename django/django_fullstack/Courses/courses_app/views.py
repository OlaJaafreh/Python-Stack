from django.shortcuts import render, HttpResponse,redirect
from .models import Course
from django.contrib import messages

def index(request):
    course = Course.objects.all
    return render(request,"main.html",{'course':course})

def addCourses(request):


    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        messages.error(request, 'Add failed.')
        return redirect('index')
    else:
        name= request.POST['name']
        description = request.POST['description']
        Course.objects.create(name=name,description=description)
        messages.success(request, 'Addtion successful')
    return redirect("index")


def delCourses(request,Cid):
    course = Course.objects.get(id=Cid)
    return render(request,"del.html",{'course':course})

def deleteCourse(request,Cid):
    course = Course.objects.get(id=Cid)
    course = course.delete()
    return redirect('index')

