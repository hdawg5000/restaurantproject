from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Show all restaurants
@app.route('/')
def restaurantMenu():
    restaurants = session.query(Restaurant).all()
    output = '<html><body><h1>Restaurants</h1>'
    for restaurant in restaurants:
        output += restaurant.name + "</br></br>"
    output += "</body></html>"
    return output

#Create a new restaurant
@app.route('/restaurant/new')
def createRestaurant():
    output = 'This will display the create a new restaurant form'
    return output

#Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    output = 'This will display the edit a restaurant page for ' + str(restaurant_id)
    return output

#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    output = 'This will display the delete a restaurant page for ' + str(restaurant_id)
    return output

#Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    output = 'This will display the show a restaurant menu page for ' + str(restaurant_id)
    return output

#Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/new')
def newMenuItem(restaurant_id, menu_id):
    output = 'This will display the create new restaurant menu item page'
    return output

#Edit a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    output = 'This will display the edit restaurant menu item page'
    return output

#Delete a menu item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    output = 'This will display the delete restaurant menu item page'
    return output

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
