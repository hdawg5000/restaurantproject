from flask import Flask, render_template, request, redirect, url_for

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
    return render_template('restaurants.html', restaurants=restaurants)

#Create a new restaurant
@app.route('/restaurant/new', methods=['GET', 'POST'])
def createRestaurant():
    if request.method == 'POST':
        restaurant = Restaurant(name=request.form['name'])
        session.add(restaurant)
        session.commit()
        return redirect(url_for('restaurantMenu'))
    else:
        return render_template('newRestaurant.html')

#Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        return redirect(url_for('restaurantMenu'))
    else:
        return render_template('editMenuItem.html',restaurant = restaurant_id)

#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurant)
        session.commit()
        return redirect(url_for('restaurantMenu'))
    else:
        return render_template('deleteRestaurant.html', restaurant_id=restaurant_id, restaurant=restaurant)

#Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/menu')
def showRestaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)

#Create a new menu item
@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        menuItem = MenuItem(name=request.form['name'], description=request.form['description'], price=request.form['price'], id=restaurant_id)
        session.add(menuItem)
        session.commit()
        return redirect(url_for('showRestaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant=restaurant)

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
