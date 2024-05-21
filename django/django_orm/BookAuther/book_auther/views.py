from django.shortcuts import render,redirect
from .models import Books,Authors

# views.py
from django.shortcuts import render, redirect
from .models import Books


def bookhtml(request):
    books = Books.objects.all()
    return render(request,"book.html",{'books':books})

def authorhtml(request):
    authors = Authors.objects.all()
    return render(request,"author.html",{'authors':authors})

def book(request):
    title = request.POST['title']
    description = request.POST['description']
    Books.objects.create(title=title, description=description)
    return redirect('bookhtml')

def bookdet(request,id):
    books = Books.objects.get(id=id)
    authors = Authors.objects.all()
    return render(request,"bookdet.html",{'book':books,'authors':authors})

def authordet(request,id):
    author = Authors.objects.get(id=id)
    books = Books.objects.all()
    return render(request,"authordet.html",{'books':books,'author':author})

def bookdetAdd(request,id):
        bookauthor = request.POST.get('bookauthor')
        bookauthorobj = Authors.objects.get(id = bookauthor )
        book =Books.objects.get(id = id ) 
        book.authors.add(bookauthorobj)
        return redirect('bookdet',id)

def authordetAdd(request,id):
        bookauthor = request.POST.get('authorbook')
        bookauthorobj = Books.objects.get(id = bookauthor )
        author =Authors.objects.get(id = id ) 
        author.books.add(bookauthorobj)
        return redirect('authordet',id)


def author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Authors.objects.create(first_name=first_name, last_name=last_name ,notes=notes)
    return redirect('authorhtml')





