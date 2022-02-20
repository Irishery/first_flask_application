from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class VolForm(FlaskForm):
    title = StringField('Логин', validators=[DataRequired()])
    surname = PasswordField('Пароль', validators=[DataRequired()])
    name = StringField("Имя")
    education = StringField('Образование')
    profession = StringField("Профессия", validators=[DataRequired()])
    sex = StringField("Пол", validators=[DataRequired()])
    motivation = TextAreaField("Мотивация")
    ready = BooleanField("Готов остаться на Марсе?")
    submit = SubmitField("Войти")