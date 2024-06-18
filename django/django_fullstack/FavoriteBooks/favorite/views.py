from django.shortcuts import render,redirect
from .models import Users,Books
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
            return redirect("AddBook")
        else:
            messages.error(request, 'Incorrect Password')
    else:
        messages.error(request, 'Email not found')
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
    
def AddBook(request):
    books = Books.objects.all()
    user = Users.objects.get(id = request.session['userid'])
    return render(request,'addBooks.html',{'books': books,'user': user})

def AddMyBook(request,U_id):
    errors = Books.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("AddBook")
    else:
        title = request.POST['title']
        description = request.POST['description']
        Books.objects.create(title=title,desc=description,user = Users.objects.get(id = U_id))
        messages.success(request, 'The book added ')
        return redirect("AddBook")
    

def EditBook(request,U_id,B_id):
    book = Books.objects.get(id = B_id)
    user = Users.objects.get(id = U_id)
    return render(request,'editMyBook.html',{'book': book,'user': user})

def EditMyBook(request,U_id,B_id):
    if request.method == 'POST':
        book = Books.objects.get(id=B_id)
        book.title = request.POST['edittitle']
        book.desc = request.POST['editdesc']
        book.save()
        return redirect('EditBook',U_id,B_id)
    

# def deleteBook(request):
#     book = Books.objects.all
#     user = Users.objects.all
#     return render(request,'editMyBook.html',{'book': book,'user': user})

def deleteMyBook(request,U_id,B_id):
    if request.method == 'POST':
        book = Books.objects.get(id=B_id)
        book.delete()
        return redirect('EditBook',U_id,B_id)

def OtherBook(request,O_id):
    return render(request,'otherBook.html')
    