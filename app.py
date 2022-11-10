from tkinter.tix import Tree
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/servicos")
def servicos():
    return render_template("servicos.html")


       

if __name__ == "__main__":
    app.run()