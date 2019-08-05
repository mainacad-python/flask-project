from app import app
from flask import render_template
import datetime


@app.route('/')
@app.route('/index')
def index():
    title = None
    user = {
        'username': "Max"
    }
    return render_template('index.html', title=title, user=user)


@app.route('/about')
def about():
    user1 = {
        'username': "Max"
    }
    date1 = datetime.datetime.utcnow()
    return render_template('about.html', user=user1, date=date1)


