from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from ..models.models import db, PricePlaze, ProductPlaze, User, RequestProductPlaze, City
from datetime import datetime, timedelta
import pytz

homeFarmer_bp = Blueprint("homeFarmer_bp", __name__, template_folder="templates", static_folder="static")

@homeFarmer_bp.route('/homeFarmer')
def homeFarmer():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value

    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 

    requestProductPlaze = db.session.query(RequestProductPlaze,ProductPlaze, User, City).\
    join(ProductPlaze, ProductPlaze.id == RequestProductPlaze.fk_product_plaze).\
    join(User, ProductPlaze.fk_user == User.id).\
    join(City, City.id == User.fk_city).\
    order_by(RequestProductPlaze.id.desc()).\
    limit(15).all()
    print(requestProductPlaze)
    return render_template("homeFarmer.html",user=user,requestProductPlaze=requestProductPlaze,date=dateDay)