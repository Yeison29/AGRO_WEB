from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from ..models.models import db, PricePlaze, ProductPlaze, User, RequestProductPlaze, City, Harvest, ControlHarvest
from datetime import datetime, timedelta
from .forms import  RegisterHarvest
import pytz
import json
from sqlalchemy import func
from dateutil.relativedelta import relativedelta

homeFarmer_bp = Blueprint("homeFarmer_bp", __name__, template_folder="templates", static_folder="static")

@homeFarmer_bp.route('/homeFarmer')
def homeFarmer():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value

    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 

    harvest=db.session.query(Harvest).all()

    requestProductPlaze = db.session.query(RequestProductPlaze,ProductPlaze, User, City).\
    join(ProductPlaze, ProductPlaze.id == RequestProductPlaze.fk_product_plaze).\
    join(User, ProductPlaze.fk_user == User.id).\
    join(City, City.id == User.fk_city).\
    order_by(RequestProductPlaze.id.desc()).\
    limit(15).all()
    print(requestProductPlaze)
    return render_template("homeFarmer.html",user=user,requestProductPlaze=requestProductPlaze,date=dateDay,harvest=harvest)

@homeFarmer_bp.route('/registerHarvest')
def registerHarvest():
    form = RegisterHarvest()
    session = current_app.config['GLOBAL_SESSION']
    user = session.value

    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 

    harvest=db.session.query(Harvest).all()
    print(harvest)

    return render_template("control/registerHarvest.html",user=user,date=dateDay,form=form,harvest=harvest)

@homeFarmer_bp.route('/register', methods=['POST'])
def register():
    form = RegisterHarvest()
    session = current_app.config['GLOBAL_SESSION']
    user = session.value

    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 

    harvest = request.form['harvest']
    print(harvest)

    register= ControlHarvest(hectares=form.hectares.data,date_init=form.date_init.data,date_fin=form.date_fin.data,time_production=form.time_production.data,fk_user=user.id,fk_harvest=harvest)
    db.session.add(register)
    db.session.commit()

    return redirect('/homeFarmer')

@homeFarmer_bp.route('/queryHarvest', methods=['GET','POST'])
def queryHarvest():
    mes_mas=0
    harvest = request.get_json()
    idHarvest = harvest['harvest']
    print(idHarvest)
    fecha_mas_alta = db.session.query(func.max(ControlHarvest.date_fin)).filter(ControlHarvest.fk_harvest == idHarvest).scalar()
    print(fecha_mas_alta)
    date = ControlHarvest.query.filter_by(date_fin=fecha_mas_alta).order_by(ControlHarvest.time_production.desc()).filter(ControlHarvest.fk_harvest == idHarvest).first()
    print(date)
    date_time_production=date.time_production
    date_mas_mes=date_time_production/4
    if int(date_mas_mes)<date_mas_mes:
            date_mas_mes=int(date_mas_mes)
    date_date_fin = date.date_fin + relativedelta(months=date_mas_mes)
    control = ControlHarvest.query.filter(ControlHarvest.fk_harvest == idHarvest).all()  # Realiza una consulta para obtener todos los usuarios
    print(control)
    # if datos != None:
    #     mes_mas=datos.time_production/4
    #     print(mes_mas)
    #     if int(mes_mas)<mes_mas:
    #         mes_mas=int(mes_mas)
    #     print(mes_mas)
    #     fecha_mas_un_mes = fecha_mas_alta + relativedelta(months=mes_mas)
    #     print(fecha_mas_un_mes)

    #     mes_escrito = fecha_mas_un_mes.strftime('%B')
    #     print(mes_escrito)

    cantidadCosechada=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(cantidadCosechada)

    for item in control:
        item_date_fin=item.date_fin
        print(item_date_fin.strftime('%B'))
        print(item_date_fin.strftime('%m'))
        item_time_production=item.time_production
        print(item_time_production)
        mas_mes=item_time_production/4
        print(mas_mes)
        if int(mas_mes)<mas_mes:
            mas_mes=int(mas_mes)
        print(mas_mes)
        date_fin = item_date_fin + relativedelta(months=mas_mes)
        print(date_fin)
        print(date_fin.strftime('%m'))
        hec=item.hectares
        print(hec)
        i=int(item.date_fin.strftime('%m'))
        y=int(date_fin.strftime('%m'))
        print(i)
        print(y)
        if i>y:
            y=12+y
        print(y)
        while i <= y:
            if i>12:
                cantidadCosechada[i-12] += hec
            else:
                cantidadCosechada[i] += hec
            i=i+1
        print(cantidadCosechada)
        print(item.date_fin)


    time_zone_colombia = pytz.timezone('America/Bogota')
    dateDay = datetime.now(time_zone_colombia).date() 
    print(dateDay.strftime('%m'))
    date_actual=int(dateDay.strftime('%m'))
    arrayMeses=[]
    arrayH=[]
    i=date_actual
    y=int(date_date_fin.strftime('%m'))
    print(i)
    print(y)
    if i>y:
        y=12+y
    print(y)
    
    while i <= y:
        if i>12:
            arrayH.append(cantidadCosechada[i-12])
            name_mes = datetime.strptime(str(i-12), "%m").strftime("%B")
            arrayMeses.append(name_mes)
        else:
            arrayH.append(cantidadCosechada[i])
            name_mes = datetime.strptime(str(i), "%m").strftime("%B")
            arrayMeses.append(name_mes)
        i=i+1
    print(arrayH)
    print(arrayMeses)
    data={
        "arrayMeses": arrayMeses,
        "arrayHarvest": arrayH
    }
    # Convierte los datos en formato JSON
    control_json = json.dumps(data)

    # Devuelve el JSON como respuesta
    return control_json
