from . import app,db,login_manager
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_user,logout_user,current_user,login_required
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash


login_manager.login_view='sign_in_user'


#the homepage
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
@app.route('/login',methods=['GET', 'POST'])
def sign_in_user():
    email=request.form.get('email')
    password=request.form.get('password')

    user=User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password,password):
        login_user(user)
        return redirect(url_for('user_dashboard')) 
    return render_template('login.html')

#the user dashboard
@app.route('/dashboard')
@login_required
def user_dashboard():
    return render_template('dashboard.html')

#logout a user
@app.route('/logout')
def logout_a_user():
    logout_user()
    return redirect(url_for('sign_in_user'))