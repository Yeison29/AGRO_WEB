from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from ..models.models import db, PricePlaze, ProductPlaze, User
from datetime import datetime, timedelta
import pytz

home_bp = Blueprint("home_bp", __name__, template_folder="templates", static_folder="static")

@home_bp.route('/')
def home():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    print(user)
    return render_template("home.html",user=user)

@home_bp.route('/home')
def homeSecundary():
    return redirect("/")

@home_bp.route('/precisProducts')
def precisProducts():
    pagination=0
    # Obtener la zona horaria de Colombia
    time_zone_colombia = pytz.timezone('America/Bogota')

    # Obtener la fecha y hora actual en la zona horaria de Colombia
    dateDay = datetime.now(time_zone_colombia).date() 
    # fecha_anterior = dateDay - timedelta(days=1)

    print(dateDay)
    pricesDate = db.session.query(ProductPlaze,PricePlaze, User).\
        join(PricePlaze, ProductPlaze.id == PricePlaze.fk_product_plaze).\
        join(User, ProductPlaze.fk_user == User.id).filter(PricePlaze.date == dateDay).\
        order_by(PricePlaze.price.desc()).limit(15).all()
    return render_template("tablePrecisProducts/products.html",pricesDate=pricesDate,date=dateDay,pagination=pagination)

@home_bp.route('/precisProductPagination/<pagination>')
def precisProductsPagination(pagination):
    # Obtener la zona horaria de Colombia
    time_zone_colombia = pytz.timezone('America/Bogota')
    pagination=int(pagination)
    # Obtener la fecha y hora actual en la zona horaria de Colombia
    dateDay = datetime.now(time_zone_colombia).date() + timedelta(days=pagination)
    print(dateDay)
    pricesDate = db.session.query(ProductPlaze,PricePlaze, User).\
        join(PricePlaze, ProductPlaze.id == PricePlaze.fk_product_plaze).\
        join(User, ProductPlaze.fk_user == User.id).filter(PricePlaze.date == dateDay).\
        order_by(PricePlaze.price.desc()).limit(15).all()
    return render_template("tablePrecisProducts/products.html",pricesDate=pricesDate,date=dateDay,pagination=pagination)