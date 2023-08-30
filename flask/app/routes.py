from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import User

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')





@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        new_user = User(username=username)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_user.html')
