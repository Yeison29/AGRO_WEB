from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app

homeFarmer_bp = Blueprint("homeFarmer_bp", __name__, template_folder="templates", static_folder="static")

@homeFarmer_bp.route('/homeFarmer')
def homeFarmer():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    print(user)
    return render_template("homeFarmer.html",user=user)