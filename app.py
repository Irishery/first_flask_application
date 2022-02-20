import os
import ast

from src.forms.volunteerfrom import VolForm
from src.forms.em_accessform import EmAccessform
from flask import Flask, redirect, render_template, request, url_for
import json


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=["GET"])
def main():
    return render_template("base.html", title="LOL")


@app.route('/training/<prof>', methods=["GET"])
def get_training(prof):
    name: str
    img_link: str

    if prof == "doc":
        name = "Научные симуляторы"
        img_link = "doc_train.jpg"
    elif prof == 'eng':
        name = "Инженерные тренажеры"
        img_link = "eng_train.jpg"

    return render_template("training_info.html", name=name, img_link=img_link)


@app.route('/volunteerform', methods=['GET', 'POST'])
def get_volform():
    form = VolForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for("get_form_info", form=form.data))
    return render_template("volunteerform.html", title='Форма добровольца', form=form)


@app.route('/form_info/<form>', methods=['GET'])
def get_form_info(form):
    form = ast.literal_eval(form)
    return render_template("form_info.html", form=form)


@app.route('/em_access', methods=["GET", "POST"])
def get_emform():
    form = EmAccessform()
    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for("get_form_info", form=form.data))
    return render_template("em_access_form.html", form=form)


@app.route('/prof_list/<list>', methods=["GET"])
def get_proflist(list):
    profs = ['test' for _ in range(10)]
    return render_template("prof_list.html", prof_list=profs, list=list)


app.run("127.0.0.1", port=8080, debug=True)
