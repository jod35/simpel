from . import app,db
from flask import render_template,redirect,url_for,request,flash
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash


@app.route('/')
def index():
    return render_template('index.html')

#create_an_account
@app.route('/register',methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        name=request.form.get('name')
        email=request.form.get('email')
        gender=request.form.get('gender')
        location=request.form.get('location')
        passw_hash=request.form.get('password')
        confirm=request.form.get('confirm')


        new_user={
            'name':name,
            'email':email,
            'gender':gender,
            'location':location,
            'password':generate_password_hash(passw_hash)
        }
        user=User(**new_user)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Account for {} has beed created! ".format(name))
            return redirect(url_for('create_account'))
        except:
            flash("Invalid Credentials! Try Again")
            return redirect(url_for('create_account'))
                

    return render_template('singup.html')

#sign_in
@app.route('/login')
def sign_in_user():
    return render_template('login.html')
