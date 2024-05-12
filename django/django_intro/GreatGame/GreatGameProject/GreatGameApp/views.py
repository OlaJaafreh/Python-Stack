from django.shortcuts import render,redirect
import random


def index(request):
    # print(request.session['MachineNum'] )
    if 'MachineNum' not in request.session:
        request.session['MachineNum'] = random.randint(1, 100)
    if request.method == 'POST':
        userGuess = int(request.POST['Guess'])
        if userGuess == request.session['MachineNum']:
            result = str(userGuess) + " was the number!"
            request.session.pop('MachineNum') 
            return render(request, "index1.html",{'result':result})
        elif userGuess < request.session['MachineNum']:
            result = "Too low!"
        else:
            result = "Too high!"
        return render(request, "index.html",{'result':result})
    return render(request, "index.html")

def Results(request):
    return redirect('/')