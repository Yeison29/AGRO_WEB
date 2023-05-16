from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from ..models.models import User

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
    print("entro")
    return render_template("tablePrecisProducts/products.html")