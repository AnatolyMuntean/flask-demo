from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def indexAction():
    user = {'nickname': 'Slab'}
    return render_template('index.html', title='Home', user=user)