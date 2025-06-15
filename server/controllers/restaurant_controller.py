from flask import Blueprint, jsonify, request
from models.restaurant import Restaurant
from models import db

restaurant_bp = Blueprint("restaurants", __name__)

@restaurant_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
def get_restaurant(id):
    restaurant = db.session.get(Restaurant, id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    restaurant_data = restaurant.to_dict()
    restaurant_data["restaurant_pizzas"] = [
        {
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": rp.pizza.to_dict()
        }
        for rp in restaurant.restaurant_pizzas
    ]

    return jsonify(restaurant_data), 200

@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = db.session.get(Restaurant, id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return "", 204
