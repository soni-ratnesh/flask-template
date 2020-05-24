from flask import Flask


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        from .home import home
        app.register_blueprint(home.home_bp)

        return app