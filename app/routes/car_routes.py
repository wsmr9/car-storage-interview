from flask import Blueprint, jsonify
from app.controllers.car_controller import create_car, get_cars, update_car, delete_car

# Create a Flask Blueprint for the car-related routes.
# This groups all car-related routes under a common 'car' endpoint.
car_blueprint = Blueprint('car', __name__)

@car_blueprint.route('/', methods=['GET'])
def hello_world():
    # A simple endpoint that returns a JSON response greeting.
    return jsonify(message="Hello, World!")

# Define the route for creating a car using the POST method.
# This route is linked to the 'create_car' function from the car controller.
car_blueprint.route('/car', methods=['POST'])(create_car)

# Define the route for retrieving all cars using the GET method.
# This route is linked to the 'get_cars' function from the car controller.
car_blueprint.route('/car', methods=['GET'])(get_cars)

# Define the route for updating a specific car by its 'id' using the PUT method.
# This route is linked to the 'update_car' function from the car controller.
car_blueprint.route('/car/<int:id>', methods=['PUT'])(update_car)

# Define the route for deleting a specific car by its 'id' using the DELETE method.
# This route is linked to the 'delete_car' function from the car controller.
car_blueprint.route('/car/<int:id>', methods=['DELETE'])(delete_car)
