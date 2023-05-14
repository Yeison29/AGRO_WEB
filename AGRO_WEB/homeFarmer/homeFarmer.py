from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash

homeFarmer_bp = Blueprint("homeFarmer_bp", __name__, template_folder="templates", static_folder="static")

@homeFarmer_bp.route('/homeFarmer')
def homeFarmer():

    return render_template("homeFarmer.html")