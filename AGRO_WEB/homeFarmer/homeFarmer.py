from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash
from ..models.models import User

homeFarmer_bp = Blueprint("homeFarmer_bp", __name__, template_folder="templates", static_folder="static")

@homeFarmer_bp.route('/homeFarmer')
def homeFarmer():
    user = User.query.filter_by(email='ydascanioa@ufpso.edu.co',password='ascanio').first()
    return render_template("homeFarmer.html",user=user)