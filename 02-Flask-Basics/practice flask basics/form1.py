from flask import Flask , render_template,session, redirect,url_for
from wtforms import (StringField, BooleanField,DateTimeField,
                    RadioField,SelectField,TextAreaField
                    ,SubmitField)
from flask_wtf import FlaskForm

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

#form class
class InfoForm(FlaskForm):
    breed = StringField('What breed are You?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood:",
                    choices = [('mood_one','Happy'),('mood_two','Excited')])
#unicode string
    food_choice = SelectField(u'Pick your favourite food:',
                                choices = [('chiken','Chicken'),('beef','Beef'),
                                            ('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit(): #it will check for the validators
        #hold info for particular session of the user
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
        #first it will return the form and then it will grab the data and return
    return render_template('formindex.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug = True)
