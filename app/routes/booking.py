from flask import Blueprint, render_template, request, redirect, url_for

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')

@booking_bp.route('/', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Handle form submission and save data to the database
        pass
    return render_template('booking.html')
