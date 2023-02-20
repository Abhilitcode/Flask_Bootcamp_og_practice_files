from flask import Flask , render_template,flash,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'kmykey'

class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?')
    submit = SubmitField('Click Me!')

@app.route('/', methods=['GET','POST'])
def index4():


    form = SimpleForm()
    #action perform pe 2nd ye run hoga
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for('index4'))
#pehle ye run hoga normal return of index page
    return render_template('index4.html',form=form)

if __name__ == '__main__':
    app.run(debug = True)
