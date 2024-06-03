from flask import jsonify, request
from app import db
from app.models.car import Car

def create_car():
    """
    Create a new car entry from a JSON request.

    Extracts data from a JSON payload, creates a new Car object, commits it to the database,
    and returns a JSON response with the new car's ID.

    Returns:
        Response: JSON object containing the message and the newly created car's ID if successful, status code 201.
                 JSON object containing error message if the creation fails, status code 400.
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
    Retrieve all cars from the database.

    Fetches all car records from the database and formats them into a JSON list.

    Returns:
        Response: JSON list of all cars, each represented as a dictionary.
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

    Attempts to find a car by its ID. If found, returns a JSON object with car details,
    otherwise returns a 404 with an error message.

    Returns:
        Response: JSON object with car details if found, otherwise JSON object with an error message, status code 404.
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

    Fetches a car by ID and updates its details with provided JSON data, then commits the changes.
    Returns a success message if updated, or a not-found message if no car matches the ID.

    Returns:
        Response: JSON object with success message if the car is updated, status code 200.
                  JSON object with error message if no car is found, status code 404.
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

    Attempts to find and delete a car by its ID. If successful, commits the change and returns a success message.
    If the car is not found, returns a 404 error message.

    Returns:
        Response: JSON object with success message if deleted, status code 200.
                  JSON object with error message if no car is found, status code 404.
    """
    car = db.session.query(Car).filter(Car.id == id).first()
    if car:
        db.session.delete(car)
        db.session.commit()
        return jsonify({'message': 'Car deleted successfully'})
    else:
        return jsonify({'message': 'Car not found'}), 404
