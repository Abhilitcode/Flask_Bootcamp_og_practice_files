from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/signup')
#url_for('name') should be same as the view function
def signup():
    return render_template('signup.html')

@app.route('/thanku')
def thanku():
    #grab the value of the first and last name
    first= request.args.get('first')
    last = request.args.get('last')
#later will store this data in database
    return render_template('thanku.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True)
