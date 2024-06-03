from datetime import datetime
from app import db

class Car(db.Model):
    """
    Represents a car in the automotive inventory system. This model defines the structure
    and expected data for each car entry in the database.
    
    Attributes:
        id (int): The primary key for the Car.
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The listed price of the car.
        created_at (datetime): The timestamp when the car record was created, set to current UTC time by default.
    """
    
    # Database columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        """
        Provides a string representation of this Car instance, primarily useful for debugging and logging.
        
        Returns:
            str: A string that represents the car, formatted as '<Car [brand] [model] [year]>'.
        """
        return f'<Car {self.brand} {self.model} {self.year}>'
