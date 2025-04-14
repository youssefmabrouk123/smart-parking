from flask import Blueprint, render_template, redirect, url_for, flash, session
from models import User, Reservation
from datetime import datetime

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile')
def profile():
    if 'logged_in' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('auth.signin'))
    
    # Fetch user data directly from session for reliability
    user = {
        'id': session.get('user_id'),
        'name': session.get('name'),
        'email': session.get('email'),
        'created_at': User.get_by_email(session.get('email')).get('created_at')
    }
    
    if not user['name'] or not user['email']:
        flash('User data incomplete. Please log in again.', 'warning')
        return redirect(url_for('auth.signin'))
    
    return render_template('profile/profile.html', user=user)

@profile_bp.route('/history')
def history():
    if 'logged_in' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('auth.signin'))
    
    reservations = Reservation.get_by_user(session.get('user_id'))
    # Add status to each reservation
    now = datetime.now()
    for reservation in reservations:
        reservation['status'] = 'Active' if reservation['end_time'] > now else 'Expired'
    
    return render_template('profile/history.html', reservations=reservations)