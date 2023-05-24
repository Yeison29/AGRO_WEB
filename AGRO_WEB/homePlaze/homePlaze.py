from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from .forms import  RequestProductPlaze
from ..models.models import db, PricePlaze, ProductPlaze, User
from datetime import datetime, timedelta
import pytz

homePlaze_bp = Blueprint("homePlaze_bp", __name__, template_folder="templates", static_folder="static")

@homePlaze_bp.route('/homePlaze')
def homePlaze():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    print(user)
    return render_template("homePlaze.html",user=user)

# @homePlaze_bp.route('/getProductPlaze')
# def getProductPlaze():
#     productPlazeAll = db.session.query(ProductPlaze,User).\
#         join(User, ProductPlaze.fk_user == User.id).all()
#     print(productPlazeAll)
#     return jsonify(ProductPlazeAll)

@homePlaze_bp.route('/requestProducts')
def requestProducts():
    form = RequestProductPlaze()
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    pagination=0
    # Obtener la zona horaria de Colombia
    time_zone_colombia = pytz.timezone('America/Bogota')

    # Obtener la fecha y hora actual en la zona horaria de Colombia
    dateDay = datetime.now(time_zone_colombia).date() 
    # fecha_anterior = dateDay - timedelta(days=1)
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    productPlazeAll = db.session.query(ProductPlaze).filter(ProductPlaze.fk_user == user.id).all()
    print(productPlazeAll)

    print(user.id)
    return render_template("RequestProductPlaze/requestProduct.html",date=dateDay,pagination=pagination,user=user,form=form,productPlazeAll=productPlazeAll)