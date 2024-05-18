from django.shortcuts import render, redirect
from .models import User

def index(request):
        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        age = request.POST.get("age")
        User.objects.create(first_name=first, last_name=last, email=email, age=age)
        return redirect("usersadd")

def usersadd(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})
