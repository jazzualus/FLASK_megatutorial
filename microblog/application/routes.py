from application import app
#from __init__ import app
from flask import render_template, flash, redirect, url_for
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User1'}
    posts = [
        {
            'author':{'username': 'Jonas'},
            'body':'Nuostabi diena negerti!'
        },
        {
            'author': {'username': 'Suzana'},
            'body': 'Moterys meluoja geriau!'
        },
        {
            'author': {'username': 'Kernagis'},
            'body': 'Sakale lek!!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sign in', form=form)

