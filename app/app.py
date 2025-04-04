from flask import Flask
from flask_cors import CORS

from app.AppConfig import get_config_by_name, AppConfig
from app.src.api import api
from config.Config import Env


def create_app(env: Env):
    # Create Flask app instance
    app = Flask(__name__)

    # Enable CORS if needed
    CORS(app)

    # Load config based on environment
    config: AppConfig = get_config_by_name(env)
    app.config.from_object(config)

    # Register blueprints
    app.register_blueprint(api)

    @app.errorhandler(404)
    def not_found_error(error):
        print(error)
        return {"error": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(error):
        print(error)
        return {"error": "Internal server error"}, 500

    return app
