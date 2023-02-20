from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')
def info():
    return "<h1>Puppies are cute<h1>"

#dynamic routing
@app.route('/puppy/<name>')
def puppy(name):
    #if you pass string it will give internal server error
    #so to avoid n solve the error you can debug and run it on console
    return (f"This page is for {name[100]}")

if __name__=='__main__':
    app.run(debug=True)
