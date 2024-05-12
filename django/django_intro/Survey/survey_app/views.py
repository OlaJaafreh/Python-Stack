from django.shortcuts import render ,redirect
    
def index(request):
    
    return render(request, "index.html")

def result(request):
    
    if request.method == "POST":
        data={
            "name" : request.POST['username'],
            "location" :request.POST['location'],
            "language" : request.POST['language'],
            "comment" : request.POST['comment'],
            "yes_no": request.POST ['Op'],
            "check" : request.POST.getlist('check[]')
    }
    
    return render(request,"show.html",data)

def login(request):
    return redirect ("/")
    

    