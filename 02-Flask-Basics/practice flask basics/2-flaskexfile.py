from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to latin page! Go to /puppy_latin/<name> to convert the name!</h1>"

@app.route('/puppy_latin/<name>')
def puppylatin(name):
    puppyname = ''
    if name[-1]=='y':
        puppyname = name[:-1]+'iful'
    else:
        puppyname = name+'y'
#return the value always after the function created
    return (f"<h1>The {name} is converted to its puppylatin name i.e {puppyname}.</h1>")

if __name__ == "__main__":
    app.run(debug=True)
