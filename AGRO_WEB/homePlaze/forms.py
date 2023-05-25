from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, validators, IntegerField, DateField, BooleanField, ValidationError, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional
from wtforms.widgets import TextArea
from wtforms.fields.simple import EmailField

class RequestProductPlaze(FlaskForm):
    price_min = FloatField('Precio Minimo ($)x1Kg', validators=[validators.DataRequired()])
    price_max = FloatField('Precio Maximo ($)x1kg', validators=[validators.DataRequired()])
    quality = FloatField('Cantidad (Kg)', validators=[validators.DataRequired()])