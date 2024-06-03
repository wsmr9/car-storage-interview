from flask import Blueprint, jsonify
from app.controllers.car_controller import create_car, get_cars, update_car, delete_car

car_blueprint = Blueprint('car', __name__)

@car_blueprint.route('/', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")


car_blueprint.route('/car', methods=['POST'])(create_car)

car_blueprint.route('/car', methods=['GET'])(get_cars)

car_blueprint.route('/car/<int:id>', methods=['PUT'])(update_car)

car_blueprint.route('/car/<int:id>', methods=['DELETE'])(delete_car)


