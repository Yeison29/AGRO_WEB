from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash
from ..models.models import User

def getSessionUser():
    #user = User.query.filter_by(email='ydascanioa@ufpso.edu.co',password='ascanio').first()
    #user = User.query.filter_by(email='hm@ufpso.edu.co',password='Carvajalino').first()
    user = User.query.filter_by(email='sanabastos@gamil.com',password='sanabastos').first()
    print(user)
    return user