from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def indexAction():
    user = {'nickname': 'Slab'}
    posts = [
        {
            'author': {'nickname': 'Dr. Zed'},
            'body': 'You know leaves a hole of a bullet but a\'int a bullet? Cause I freakin\' don\'t.'
        },
        {
            'author': {'nickname': 'Brick'},
            'body': 'I punch her problems!!'
        },
        {
            'author': {'nickname': 'Mr. Torgue'},
            'body': 'EXPLOSIONS??!!!!'
        }
    ]
    return render_template('index.html.jinja2', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def loginAction():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html.jinja2', title='Sign In', form=form)
