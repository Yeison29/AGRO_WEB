from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from .forms import  RequestProductPlaze as RPPF
from ..models.models import db, PricePlaze, ProductPlaze, User, RequestProductPlaze, City
from datetime import datetime, timedelta
import pytz
import base64
import os

homePlaze_bp = Blueprint("homePlaze_bp", __name__, template_folder="templates", static_folder="static")

@homePlaze_bp.route('/homePlaze')
def homePlaze():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 
    print(user.id)
    requestProductPlaze = db.session.query(RequestProductPlaze,ProductPlaze, User, City).\
    join(ProductPlaze, ProductPlaze.id == RequestProductPlaze.fk_product_plaze).\
    join(User, ProductPlaze.fk_user == User.id).\
    join(City, City.id == User.fk_city).\
    filter(ProductPlaze.fk_user == user.id).\
    order_by(RequestProductPlaze.id.desc()).\
    limit(15).all()
    print(requestProductPlaze)
    return render_template("homePlaze.html",user=user, requestProductPlaze=requestProductPlaze,date=dateDay)

# @homePlaze_bp.route('/getProductPlaze')
# def getProductPlaze():
#     productPlazeAll = db.session.query(ProductPlaze,User).\
#         join(User, ProductPlaze.fk_user == User.id).all()
#     print(productPlazeAll)
#     return jsonify(ProductPlazeAll)

@homePlaze_bp.route('/requestProductPlaze', methods=['POST'])
def requestProductPlaze():
    form = RPPF()
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    pagination=0
    code = request.form['productPlaze']
    print(code)
    # Obtener la zona horaria de Colombia
    time_zone_colombia = pytz.timezone('America/Bogota')

    # Obtener la fecha y hora actual en la zona horaria de Colombia
    dateDay = datetime.now(time_zone_colombia).date() 
    # fecha_anterior = dateDay - timedelta(days=1)
    requestProductPlaze= RequestProductPlaze(price_max=form.price_max.data,price_min=form.price_min.data,quantity=form.quality.data,date=dateDay,fk_product_plaze=code)
    db.session.add(requestProductPlaze)
    db.session.commit()
    return redirect("/homePlaze")

@homePlaze_bp.route('/requestProducts')
def requestProducts():
    form = RPPF()
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    pagination=0
    # Obtener la zona horaria de Colombia
    time_zone_colombia = pytz.timezone('America/Bogota')

    # Obtener la fecha y hora actual en la zona horaria de Colombia
    dateDay = datetime.now(time_zone_colombia).date() 
    # fecha_anterior = dateDay - timedelta(days=1)
    productPlazeAll = db.session.query(ProductPlaze).filter(ProductPlaze.fk_user == user.id).all()
    print(productPlazeAll)

    print(user.id)
    return render_template("RequestProductPlaze/requestProduct.html",date=dateDay,pagination=pagination,user=user,form=form,productPlazeAll=productPlazeAll)

@homePlaze_bp.route('/saveImg', methods=['GET', 'POST'])   # a esta ruta envio el array de imagenes editadas
def guardarImg():
    if request.method == "POST":
        imagen_base64 = request.form['imagen']
        session = current_app.config['GLOBAL_SESSION']
        time_zone_colombia = pytz.timezone('America/Bogota')
        dateDay = datetime.now(time_zone_colombia).date() 
        user = session.value
        codigo=request.form['codigo']
        oferta="ofertas"
        imagen_binaria = base64.b64decode(imagen_base64.split(',')[1])
        ruta=f'{"/home/yeison/proyectoIntegrador/AGRO_WEB/AGRO_WEB/static/fotos"}'
        os.makedirs(f'{"/home/yeison/proyectoIntegrador/AGRO_WEB/AGRO_WEB/static/fotos/"}{oferta}', exist_ok=True)
        r=f"{ruta}/{oferta}/{codigo}_{dateDay}.jpg"
        with open(r, "wb") as imagen_file:
            imagen_file.write(imagen_binaria)
    return render_template("homePlaze.html",user=user)
