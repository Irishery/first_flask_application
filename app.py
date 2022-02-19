from turtle import title
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template("base.html", title="LOL")

app.run("127.0.0.1", port=8080, debug=True)