from flask import Blueprint, render_template

print("terms_bp is being created")

terms_bp = Blueprint('terms', __name__, url_prefix='/terms')

@terms_bp.route('/')
def terms():
    return render_template('terms.html')
