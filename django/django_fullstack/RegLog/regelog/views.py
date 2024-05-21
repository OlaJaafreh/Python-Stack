from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registration,LogIn
import bcrypt



def index(request):
    return render(request ,"index.html")

def creat(request):
        

        errors = Registration.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            messages.error(request, 'Registration failed.')
            return redirect('index')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            Registration.objects.create(first_name=first_name,last_name=last_name,email=email,password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
            messages.success(request, 'Registration successful. You can now log in.')
        return redirect("index")

def Login(request):
        user = Registration.objects.filter(email=request.POST['emailLog']) 
        if user: 
            logged_user = user[0] 
        errors = LogIn.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('index')
        else:
            request.session['userid']=logged_user.id
            return render(request ,"index1.html",{'first_name':logged_user.first_name})
        
def Logout(request):
    del request.session['userid']
    return render(request ,"index.html")


