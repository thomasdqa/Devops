from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import bleach



auth = Blueprint('auth', __name__)

MAX_LENGTH = 50

#This function will run whenever we go to the '/login' route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #gets data from POST request
    if request.method == 'POST':
        email = bleach.clean(Bcrypt(request.form.get('email')))[:MAX_LENGTH]
        password = bleach.clean(Bcrypt(request.form.get('password')))[:MAX_LENGTH]

        user = User.query.filter_by(email=email).first()
        if user:
            #authenticates password against hash stored in databse
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                #logs user in
                login_user(user, remember=True)
                #sends user to sepcific route based on their admin privlidges
                if user.admin == 'true':
                    return redirect(url_for('views.admin'))
                else:
                    return redirect(url_for('views.home'))
            #authenticates emails and password and notifies user if authentication fails
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    #renders the login.html page
    return render_template("login.html", user=current_user)

#This function will run whenever we go to the '/logout' route
@auth.route('/logout')
#ensures user is logged in
@login_required
def logout():
    #logs user out
    logout_user()
    #returns user to login page
    return redirect(url_for('auth.login'))

#This function will run whenever we go to the '/sign-up' route
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #gets data from POST request
    if request.method == 'POST':
        email = bleach.clean(Bcrypt(request.form.get('email')))[:MAX_LENGTH]
        first_name = bleach.clean(Bcrypt(request.form.get('firstName')))[:MAX_LENGTH]
        password1 = bleach.clean(Bcrypt(request.form.get('password1')))[:MAX_LENGTH]
        password2 = bleach.clean(Bcrypt(request.form.get('password2')))[:MAX_LENGTH]

        #authenticates users sign-ip attempts
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            #if user sign-up passes authentication it adds this user to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'), admin = 'False')
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            #dirents newly signedup user to the home page
            return redirect(url_for('views.home'))
    #renders signup html page
    return render_template("sign_up.html", user=current_user)



