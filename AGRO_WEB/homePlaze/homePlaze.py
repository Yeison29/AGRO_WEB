from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app

homePlaze_bp = Blueprint("homePlaze_bp", __name__, template_folder="templates", static_folder="static")

@homePlaze_bp.route('/homePlaze')
def homePlaze():
    session = current_app.config['GLOBAL_SESSION']
    user = session.value
    print(user)
    return render_template("homePlaze.html",user=user)