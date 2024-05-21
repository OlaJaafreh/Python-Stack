from django.shortcuts import render, redirect
import random

def GoldTotal(FCHQ):
    if FCHQ in ['farm', 'cave', 'house']:
        return random.randint(10, 20)
    elif FCHQ == 'quest':
        return random.randint(-50, 50)
    else:
        return 0

def index(request):
    if 'Yourgold' not in request.session:
        request.session['Yourgold'] = 0
        request.session['activities'] = []

    activities_reversed = list(reversed(request.session['activities']))

    return render(request, 'index.html', {
        'Yourgold': request.session['Yourgold'],
        'activities': activities_reversed
    })

def process_money(request):
    if request.method == 'POST':
        FCHQ = request.POST.get('FCHQ')
        gold_earned = GoldTotal(FCHQ)
        request.session['Yourgold'] += gold_earned

        color = 'green' if gold_earned > 0 else 'red'
        activity = f'<span style="color: {color};">Earned {gold_earned} gold from the {FCHQ}!</span>'



        # activity = f'Earned {gold_earned} gold from the {FCHQ}!'
        request.session['activities'].append(activity)
        request.session.modified = True
    return redirect('/')

def deleteed(request):
    del request.session['Yourgold']
    del request.session['activities']
    return redirect('/')
