from flask import Flask

def create_app():
    print("create_app is being called")
    app = Flask(__name__)

    from .routes.home import home_bp
    from .routes.booking import booking_bp
    from .routes.terms import terms_bp
    from .routes.about import about_bp
    from .routes.maps import maps_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(terms_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(maps_bp)

    return app
