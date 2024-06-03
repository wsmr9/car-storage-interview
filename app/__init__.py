from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize SQLAlchemy with no parameters initially.
db = SQLAlchemy()

def create_app():
    """
    Factory function to create a Flask application.
    
    Returns:
        app (Flask): The Flask application instance configured and ready to run.
    """
    
    # Create a Flask application instance
    app = Flask(__name__)
    
    # Load configurations from the Config class defined in config.py
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy with the Flask app for database operations
    db.init_app(app)
    
    # Import models after the db variable is initialized to ensure they are correctly associated with the database
    from .models.car import Car  # Adjust the import path based on your project structure
    
    # Ensure all database tables are created based on the defined models
    # It's crucial to perform this within the application context
    with app.app_context():
        db.create_all()

    # Import and register Blueprints for route handling
    from .routes.car_routes import car_blueprint
    app.register_blueprint(car_blueprint)

    # Return the configured Flask app instance
    return app
