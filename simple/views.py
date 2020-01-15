from . import app,db
from flask import render_template,redirect,url_for,request

@app.route('/')
def index():
    return render_template('index.html')

#create_an_account
@app.route('/register')
def create_account():
    return render_template('singup.html')

#sign_in
@app.route('/login')
def sign_in_user():
    return render_template('login.html')
