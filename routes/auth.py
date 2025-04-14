from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from werkzeug.security import check_password_hash
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.get_by_email(email)
        
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            session['user_id'] = user['id']
            session['name'] = user['name']
            session['email'] = user['email']
            flash('You are now logged in', 'success')
            return redirect(url_for('parking.dashboard'))
        else:
            flash('Invalid login credentials', 'danger')
    
    return render_template('auth/signin.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return render_template('auth/signup.html')
        
        if User.get_by_email(email):
            flash('Email already exists', 'danger')
            return render_template('auth/signup.html')
        
        User.create(name, email, password)
        flash('You are now registered and can log in', 'success')
        return redirect(url_for('auth.signin'))
    
    return render_template('auth/signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))