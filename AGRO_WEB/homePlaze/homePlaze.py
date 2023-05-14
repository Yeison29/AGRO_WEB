from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash

homePlaze_bp = Blueprint("homePlaze_bp", __name__, template_folder="templates", static_folder="static")

@homePlaze_bp.route('/homePlaze')
def homePlaze():

    return render_template("homePlaze.html")