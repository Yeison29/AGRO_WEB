from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash
from ..models.models import User

def getSessionUser():
    # user = User.query.filter_by(email='ydascanioa@ufpso.edu.co',password='ascanio').first()
    user = User.query.filter_by(email='corabastos@gamil.com',password='corabastos').first()
    print(user)
    return user