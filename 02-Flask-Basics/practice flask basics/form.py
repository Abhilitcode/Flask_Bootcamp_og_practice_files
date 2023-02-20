from flask import Flask , render_template
from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecurity'

#create ur own form class and inherit from FlaskForm
class InfoForm(FlaskForm):
    #form that grab info of puppy!
    #attributes
    breed = StringField("What breed are you?")
    submit = SubmitField("Submit")

@app.route('/', methods=['GET','POST'])
def index():
    #this breed is only a variable
    breed= False

    #create instance of a form
    form = InfoForm()

    if form.validate_on_submit():
        #grab data from form
        breed = form.breed.data
        form.breed.data = ''
    return render_template('index3.html',form=form,breed=breed)

if __name__ == '__main__':
    app.run(debug = True)
