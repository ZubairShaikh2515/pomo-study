from flask import Flask, render_template, request
from flask_session import Session
from helpers import login_required
import sqlite3

app = Flask(__name__)
db = sqlite3.connect('pomo.db')
Session(app)


@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("login.html")


@app.route('/register')
def register():
    if request.method == "POST":
        pass
    else:
        render_template("register.html")


@app.route('/callback')
def callback():
    pass


if __name__ == "__main__":
    app.run(debug = True)