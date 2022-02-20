from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EmAccessform(FlaskForm):
    astronaut_id = StringField("id атронавта")
    astronaut_pas = StringField("Пароль астронавта")
    captain_id = StringField("id капитана")
    captain_pas = StringField("Пароль капитана")
    access_but = SubmitField("Доступ")
