from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from models import ParkingSpace, Reservation
import qrcode
from io import BytesIO
import base64

parking_bp = Blueprint('parking', __name__)

@parking_bp.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('auth.signin'))
    
    parking_spaces = ParkingSpace.get_all()
    return render_template('dashboard/home.html', parking_spaces=parking_spaces)

@parking_bp.route('/reserve/<int:space_id>', methods=['GET', 'POST'])
def reserve(space_id):
    if 'logged_in' not in session:
        flash('Please login first', 'danger')
        return redirect(url_for('auth.signin'))
    
    space = ParkingSpace.get_by_id(space_id)
    if not space:
        flash('This parking space is already taken', 'danger')
        return redirect(url_for('parking.dashboard'))
    
    if request.method == 'POST':
        hours = int(request.form['hours'])
        reservation_id, start_time, end_time = Reservation.create(session['user_id'], space_id, hours)
        
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(f"RESERVATION:{reservation_id}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered)
        qr_code = base64.b64encode(buffered.getvalue()).decode()
        
        return render_template('dashboard/reservation.html', 
                             reservation_id=reservation_id,
                             space_number=space['space_number'],
                             start_time=start_time,
                             end_time=end_time,
                             qr_code=qr_code)
    
    return render_template('dashboard/reservation.html', space=space)