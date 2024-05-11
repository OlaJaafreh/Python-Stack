from flask import Flask ,request ,render_template,redirect,session
import random
app = Flask(__name__)
app.secret_key='Ola'

@app.route('/', methods=['GET', 'POST'])
def Enter():
    if 'MachineNum' not in session:
        session['MachineNum'] = random.randint(1, 100)
    if request.method == 'POST':
        userGuess = int(request.form['Guess'])
        if userGuess == session['MachineNum']:
            result = str(userGuess) + " was the number!"
            session.pop('MachineNum') 
            return render_template("index1.html", result=result)
        elif userGuess < session['MachineNum']:
            result = "Too low!"
        else:
            result = "Too high!"
        return render_template("index.html", result=result)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def Results():
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
