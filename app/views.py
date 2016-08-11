from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():

    user = {'nickname' : 'Worthy'}
    posts = [
        {
            'author' : 'Jogn',
            'body' : 'nice summer'
        },
        {
            'author' : 'Lily',
            'body' : 'Which could be my boyfriend'
        },
        {
            'author': 'Sindy',
            'body': 'It\'s my first day!!! Great Day!!!'
        }
    ]
    return render_template("index.html",
                           title = "Home",
                           posts = posts,
                           user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login resquested for OpenID = "'+form.openid.data + '", remembem_me = ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)
