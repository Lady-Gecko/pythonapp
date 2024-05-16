from flask import Blueprint, render_template

maps_bp = Blueprint('maps', __name__, url_prefix='/maps')

@maps_bp.route('/')
def maps():
    return render_template('maps.html')
