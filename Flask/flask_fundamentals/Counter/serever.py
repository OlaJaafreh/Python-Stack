from flask import Flask ,render_template ,session,redirect,request
app = Flask(__name__)
app.secret_key = 'Ola'

@app.route('/')
def Counter():
    if 'counterr' not in session:
        session['counterr']=0
    if 'count' not in session:
        session['count']=0
    else:
        session['counterr'] = session['counterr']+1
        session['count'] = session['count']+0
    return render_template("index.html",counterr=session['counterr'],count=session['count'])


@app.route('/destroy_session' )#with post if its in form
def distroy():
    session.clear()
    return redirect('/')

@app.route('/IncBy2',methods=['POST'])
def add2():
    if 'count' not in session:
        session['count']=0
    elif 'counterr' not in session:
        session['counterr']=0
    else:
        session['count'] = session['count']+2
        session['counterr'] = session['counterr']-1
    return redirect('/')


@app.route('/Reset' ,methods=['POST'])#with post if its in form
def Reset():
    session['count']=0
    if 'counterr' not in session:
        session['counterr']=0
    else:
        session['counterr'] = session['counterr']-1
    return redirect('/')
    
@app.route('/IncByUser',methods=['POST'])
def addUser():
    num = int(request.form['Enter'])
    if 'count' not in session:
        session['count']=0
    elif 'counterr' not in session:
        session['counterr']=0
    else:
        session['count'] = session['count']+num
        session['counterr'] = session['counterr']-1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
