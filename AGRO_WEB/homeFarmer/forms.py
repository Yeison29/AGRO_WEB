from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators, IntegerField, DateField, BooleanField, ValidationError, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange
from wtforms.widgets import TextArea
from wtforms.fields.simple import EmailField

class RegisterHarvest(FlaskForm):
    date_init = DateField('Fecha de siembra', validators=[DataRequired()])
    date_fin = DateField('Fecha aproximada a cosechar', validators=[DataRequired()])
    hectares = FloatField('Cantidad de hectareas sembradas', validators=[validators.DataRequired()])
    time_production = IntegerField('Semanas aproximadas de cosecha', validators=[DataRequired(), NumberRange(min=0)])