from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from app.controllers.number_controller import number_bp
    app.register_blueprint(number_bp)

    return app