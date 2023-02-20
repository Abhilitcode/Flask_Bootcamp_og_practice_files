from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    user_logged_in = True
    mylist = ['ABHI','RAHUL','PRIYA']
    return render_template('template_contol_flow.html',mylist=mylist,user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)
