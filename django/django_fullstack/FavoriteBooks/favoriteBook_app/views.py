from django.shortcuts import render ,redirect
from .models import Users , Books
import bcrypt
from django.contrib import messages

def loginPage(request):
    return render(request,'login.html')


def login(request):
    email = request.POST['emailLog']
    password = request.POST['pass']
    user = Users.objects.filter(email=email)
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect("books")
        else:
            messages.error(request, 'Incorrect User name or Password')
    else:
        messages.error(request, 'Incorrect User name or Password')
    return redirect('loginPage')


def register(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        messages.error(request, 'Registration failed.')
        return render(request,'login.html', {'errors': errors})
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        messages.success(request, 'Registration successful. You can now log in.')
        return render(request ,"login.html")
    

def AddBooks(request):
    errors = Books.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('books')
    else:
        title = request.POST['title']
        desc = request.POST['desc']
        user = Users.objects.get(id = request.session['userid'])
        book = Books.objects.create(title = title,desc = desc,uploaded_by=user)
        book.user.add(user)
        return redirect ('books')

def AddToFavorite(request,BookId):

    book = Books.objects.get(id=BookId)
    user = Users.objects.get(id = request.session['userid'])
    book.user.add(user)

    if book.uploaded_by.id == request.session['userid']:
        return redirect('userBook', BookId=BookId)
    else:
        return redirect('otherBook', BookId=BookId)

    # return redirect ('otherBook', BookId=BookId)


def RemoveFromFavorite(request,BookId):

    book = Books.objects.get(id=BookId)
    user = Users.objects.get(id = request.session['userid'])
    book.user.remove(user)

    return redirect ('userBook', BookId=BookId)

def books(request):
    user = Users.objects.get(id = request.session['userid'])
    userBooks = Books.objects.all
    return render(request ,"books.html",{'userBooks':userBooks,'user': user})

    

def confirmBook(request,BookId):
    # user = Users.objects.get(id = request.session['userid'])
    book = Books.objects.get(id=BookId)
    if book.uploaded_by.id == request.session['userid']:
        return redirect('userBook', BookId=BookId)
    else:
        return redirect('otherBook', BookId=BookId)

def EdituserBook(request,BookId):
    if request.method == "POST":
        title = request.POST.get('titleEdit')
        desc = request.POST.get('descEdit')
        user = Users.objects.get(id=request.session['userid'])
        userBooks = Books.objects.get(id=BookId, uploaded_by=user)
        userBooks.title = title
        userBooks.desc = desc
        userBooks.save()
        return redirect('userBook', BookId=BookId)
    else:
        return redirect('userBook', BookId=BookId)
    

def DeleteuserBook(request,BookId):
    user = Users.objects.get(id=request.session['userid'])
    userBooks = Books.objects.get(id=BookId, uploaded_by=user)
    userBooks.delete()
    return redirect('books')

def userBook(request,BookId):
    user = Users.objects.get(id = request.session['userid'])
    userBooks = Books.objects.get(id=BookId,uploaded_by=user)
    return render(request ,"userBook.html",{'userBooks':userBooks,'user': user})

def otherBook(request,BookId):
    userBooks = Books.objects.get(id=BookId)
    user = Users.objects.get(id = request.session['userid'])
    return render(request ,"otherBook.html",{'userBooks':userBooks,'user': user})
