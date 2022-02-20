from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)


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


app.run("127.0.0.1", port=8080, debug=True)
