from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    Snum=request.form['strawberry']
    Rnum=request.form['raspberry']
    Anum=request.form['apple']
    CustumerFirstName=request.form['first_name']
    CustumerLastName=request.form['last_name']
    CustumerNum=request.form['student_id']
    return render_template("checkout.html",Snum=Snum,Rnum=Rnum,Anum=Anum,CustumerFirstName=CustumerFirstName,CustumerLastName=CustumerLastName,CustumerNum=CustumerNum,count=int(Snum)+int(Rnum)+int(Anum))

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    