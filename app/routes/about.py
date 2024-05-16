from flask import Blueprint, render_template

print("about_bp is being created")

from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route('/')
def about():
    return render_template('about.html')
