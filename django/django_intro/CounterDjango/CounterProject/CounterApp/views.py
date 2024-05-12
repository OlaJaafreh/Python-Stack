from django.shortcuts import render ,redirect

def Counter(request):
    if 'counterr' not in request.session:
        request.session['counterr']=0
    if 'count' not in request.session:
        request.session['count']=0
    else:
        request.session['counterr'] = request.session['counterr']+1
        request.session['count'] = request.session['count']+0
    return render(request, "index.html")

def add2(request):
    if request.method == "POST":
        if 'count' not in request.session:
            request.session['count']=0
        elif 'counterr' not in request.session:
            request.session['counterr']=0
        else:
            request.session['count'] = request.session['count']+2
            request.session['counterr'] = request.session['counterr']-1
    return redirect('/')

def Reset(request):
    if request.method == "POST":
        request.session['count']=0
        if 'counterr' not in request.session:
            request.session['counterr']=0
        else:
            request.session['counterr'] = request.session['counterr']-1
    return redirect('/')

def addUser(request):
    if request.method == "POST":
        request.session['num'] = request.POST['Enter']
        if 'count' not in request.session:
            request.session['count']=0
        elif 'counterr' not in request.session:
            request.session['counterr']=0
        else:
            request.session['count'] = request.session['count']+int(request.session['num'])
            request.session['counterr'] = request.session['counterr']-1
    return redirect('/')

def distroy(request):
    request.session.clear()
    return redirect('/')