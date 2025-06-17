Pizza Restaurant API - Flask Code Challenge
Overview:
This is a RESTful API built using Flask and SQLAlchemy for managing a pizza restaurant. It handles Restaurants, Pizzas, and their association (RestaurantPizzas with price). It supports retrieving, creating, and deleting data. You can test the API using Thunder Client or Postman.

Project Structure:

server/

app.py: Main Flask application

models/: Contains SQLAlchemy model definitions

controllers/: Contains route logic (controllers)

seed.py: Script to populate the database with sample data

config.py: Database configuration

Models:

Restaurant

id (int, primary key)

name (string)

address (string)

Pizza

id (int, primary key)

name (string)

ingredients (string)

RestaurantPizza

id (int, primary key)

price (float between 1 and 30)

pizza_id (foreign key)

restaurant_id (foreign key)

Routes:

GET /pizzas
Returns a list of all pizzas.

GET /restaurants
Returns a list of all restaurants.

GET /restaurants/<id>
Returns a single restaurant and its pizzas.

POST /restaurant_pizzas
Creates a new RestaurantPizza entry.
Requires JSON body with: price, pizza_id, restaurant_id

DELETE /restaurants/<id>
Deletes a restaurant by ID.

How to Run the Project:

Navigate to the project folder.

Create and activate a virtual environment.

Install dependencies:
pip install flask flask_sqlalchemy flask_cors

Run the server:
python server/app.py

To seed the database:
python server/seed.py

Testing with Thunder Client:

Open VS Code, install Thunder Client extension.

Import the JSON file "pizza-api.thunder_collection.json".

Make sure your server is running at http://localhost:5555 or your configured port.

Use GET, POST, and DELETE requests to test the endpoints.

Notes:

Make sure you have SQLite installed (or change the DB URI in config.py).

Add validation and error handling as needed.

Follow proper naming and file structure.

Credits:
This project was built as part of a Flask code challenge for learning REST API design