from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
     return "Hello World!"
     user = {'nickname': 'Miguel'} # fake user
     posts= [ # fake array of posts
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day in Portland!'
            },
            {
                'author': {'nickname': 'Susan'},
                'body': 'The Avenges movie was so cool!'
            }
        ]
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember-me=%s' %
                (form.openid,data, str(form.remember_,me.data)))
        return redirect('/index')
    return render_template( 'index.html',
                            'login.html',
                            title='Sign In',
                            user=user,
                            posts=posts,
                            form=form)
