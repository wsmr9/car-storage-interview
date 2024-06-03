from datetime import datetime
from app import db

class Car(db.Model):
    """
    Represents a car in the automotive inventory system.

    Attributes:
        id (int): The primary key for the Car.
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The listed price of the car.
        created_at (datetime): The timestamp when the car record was created, set to current UTC time by default.
    """
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Provides a string representation of this Car instance, useful for debugging and logging.
        
        Returns:
            str: A string indicating the brand, model, and year of the car.
        """
        return f'<Car {self.brand} {self.model} {self.year}>'
