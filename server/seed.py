import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

with app.app_context():
    db.init_app(app)
    db.drop_all()
    db.create_all()

    # Seed Restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Cheese Street")
    r2 = Restaurant(name="Luigi's Pies", address="456 Dough Ave")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Slice Blvd")

    db.session.add_all([r1, r2, r3])

    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Peppers, Onions, Mushrooms")

    db.session.add_all([p1, p2, p3])
    db.session.commit()

    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r2.id)
    rp3 = RestaurantPizza(price=8, pizza_id=p3.id, restaurant_id=r3.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Database seeded!")
