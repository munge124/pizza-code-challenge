#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from models import db
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)


# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route("/")
def index():
    return "<h1>Pizza API Challenge</h1>"

if __name__ == "__main__":
    app.run(port=5555, debug=True)
