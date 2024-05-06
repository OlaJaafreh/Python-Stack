from flask import Flask , render_template
app = Flask(__name__)


@app.route('/')
def checkboard():
    color=["red","black"]
    return render_template("index.html",Rows=8,Col=8,color=color)

@app.route('/<int:Rows>')
def checkboard1(Rows):
    color=["green","bisque"]
    return render_template("index.html",Rows=Rows,Col=8,color=color)

@app.route('/<int:Rows>/<int:Col>')
def checkboard2(Rows,Col):
    color=["green","bisque"]
    return render_template("index.html",Rows=Rows,Col=Col,color=color)

@app.route('/<int:Rows>/<int:Col>/<color1>/<color2>')
def checkboard10(Rows,Col,color1,color2):
    color=[color1,color2]
    return render_template("index.html",Rows=Rows,Col=Col,color=color)

if __name__=="__main__":
    app.run(debug=True)