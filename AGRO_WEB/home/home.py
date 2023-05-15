from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash
# from ..database.db import connect_to_db, get_query_result_conect

home_bp = Blueprint("home_bp", __name__, template_folder="templates", static_folder="static")

@home_bp.route('/')
def home():
    # conn=connect_to_db()
    # result = get_query_result_conect(conn)
    print("Conectado")
    return render_template("home.html")

@home_bp.route('/home')
def homeSecundary():
    return redirect("/")