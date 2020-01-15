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


        user_exists=User.query.filter_by(email=email).first()
        if user_exists:
            flash("The email {} has been used already".format(email))
            return redirect('create_account')

        elif confirm != passw_hash:
            flash("Passwords do not Match")
            return redirect('create_account')
        
        else:
            new_user={
                'name':name,
                'email':email,
                'location':location,
                'gender':gender,
                'password':generate_password_hash(passw_hash)
            }

            try:
                db.session.add(User(**new_user))
                db.session.commit()
                flash("Account for user {} has been created",format(name))
                return redirect('create_account')
            
    return render_template('singup.html')

#sign_in
@app.route('/login')
def sign_in_user():
    return render_template('login.html')
