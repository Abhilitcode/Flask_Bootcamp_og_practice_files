from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    name = "Abhi"
    letters = list(name)
    dict = {'pup_name':'Abby'}
    return render_template('basic.html',name=name,letters=letters,dict=dict)

if __name__ == '__main__':
    app.run(debug=True)
