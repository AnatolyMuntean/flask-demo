from flask import render_template
from app import app

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
