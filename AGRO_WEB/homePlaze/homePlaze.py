from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash
from ..models.models import User
homePlaze_bp = Blueprint("homePlaze_bp", __name__, template_folder="templates", static_folder="static")

@homePlaze_bp.route('/homePlaze')
def homePlaze():
    user = User.query.filter_by(email='ydascanioa@ufpso.edu.co',password='ascanio').first()
    return render_template("homePlaze.html",user=user)