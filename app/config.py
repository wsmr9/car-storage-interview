import os
from dotenv import load_dotenv

# Load environment variables from a .env file if present
load_dotenv()

class Config:
    """
    Configuration class that sets up default configurations for the Flask application.

    Attributes:
        SQLALCHEMY_DATABASE_URI (str): Database connection URL retrieved from environment variables.
            This should be in the appropriate format for SQLAlchemy, typically something like
            'postgresql://username:password@localhost/dbname' for PostgreSQL or
            'sqlite:///example.db' for SQLite.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to configure whether to track modifications
            of objects and emit signals. This is set to False to disable this feature which,
            if enabled, can consume significant memory and has a performance cost.
    """

    # Database URL setup
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://wayner:admin123@postgres_server:5432/car_management')
    # Disable SQLAlchemy track modifications to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False