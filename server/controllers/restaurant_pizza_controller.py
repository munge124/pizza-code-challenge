from flask import Blueprint, request, jsonify
from models.restaurant_pizza import RestaurantPizza
from models import db

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

@restaurant_pizza_bp.route("/restaurant_pizzas", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    if not all([price, pizza_id, restaurant_id]):
        return jsonify({"errors": ["Missing required fields"]}), 400

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    try:
        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()
        return jsonify(new_rp.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Internal Server Error"}), 500
