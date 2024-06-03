from flask import jsonify, request
from app import db
from app.models.car import Car

def create_car():
    """
    Create a new order with car from a JSON request.

    Processes a JSON payload to create an order and its associated items, computes total,
    and commits the transaction to the database.

    Returns:
        Response: JSON object with the message and created order ID, status code 201.
    """
    data = request.get_json()
    try:
        new_car = Car(
            brand=data['brand'],
            model=data['model'],
            year=data['year'],
            price=data['price']
        )
        db.session.add(new_car)
        db.session.commit()
        return jsonify({'message': 'Car created successfully', 'car_id': new_car.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

def get_cars():
    """
    Retrieve all car from the database.

    Returns:
        Response: JSON list of all car.
    """
    cars = db.session.query(Car).all()
    cars_data = [{
        'id': car.id,
        'brand': car.brand,
        'model': car.model,
        'year': car.year,
        'price': car.price,
        'created_at': car.created_at.isoformat()
    } for car in cars]
    return jsonify(cars=cars_data)

def get_car(car_id):
    """
    Retrieve a single car by its ID.
    """
    car = db.session.query(Car).filter(Car.id == car_id).first()
    if car:
        car_data = {
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'year': car.year,
            'price': car.price,
            'created_at': car.created_at.isoformat()
        }
        return jsonify(car_data)
    else:
        return jsonify({'message': 'Car not found'}), 404

def update_car(id):
    """
    Update a car record by its ID.
    """

    data = request.get_json()
    car = db.session.query(Car).filter(Car.id == id).first()
    if car:
        car.brand = data.get('brand', car.brand)
        car.model = data.get('model', car.model)
        car.year = data.get('year', car.year)
        car.price = data.get('price', car.price)
        db.session.commit()
        return jsonify({'message': 'Car updated successfully'})
    else:
        return jsonify({'message': 'Car not found'}), 404


def delete_car(id):
    """
    Delete a car record by its ID.
    """
    car = db.session.query(Car).filter(Car.id == id).first()
    if car:
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted successfully'})
    else:
        return jsonify({'message': 'Car not found'}), 404
