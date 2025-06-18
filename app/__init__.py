from flask import Flask

from app.extensions import socketio
from configuration import Configuration


def create_app(config_class=Configuration):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    socketio.init_app(app)

    # Register blueprints
    from app.simplex import bp as home_bp

    app.register_blueprint(home_bp)

    return app
