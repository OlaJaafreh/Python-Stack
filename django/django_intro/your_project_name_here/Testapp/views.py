from django.shortcuts import render , HttpResponse , redirect 
from django.http import JsonResponse

def root(request):
    return redirect('/blog')

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def New(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def Create(request):
    return redirect('/')
# Create your views here.

def show(request,Number):
    return HttpResponse(f'placeholder to display blog number : {Number}')

def edit(request,Number):
    return HttpResponse(f'placeholder to edit blog : {Number}')

def destroy(request,Number):
    return redirect('/blog')

def JasonMethod(request):
    return JsonResponse({"response":"Json","status":True})

