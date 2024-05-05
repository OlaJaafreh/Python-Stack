from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return ' "Sorry! No response. Try again.!' 

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def ask_name(name):
    return "Hi "+name

@app.route('/repeat/<int:num>/<name>')
def print_name(name, num):
   return '<br>'.join([name] * num)


@app.route('/<path:invalid_route>')
def invalid_route(invalid_route):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
