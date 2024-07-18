from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/intro-to-ds')
def intro_to_ds():
    return render_template('intro_to_ds.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')