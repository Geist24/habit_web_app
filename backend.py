from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
import config, os, json

app = Flask(__name__)
app.config.from_object(config)
JSON_FILE = 'users.json'

def load_users():
    pass

def save_users():
    pass


@app.route('/')
def home():
    return render_template("home_page.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['Password']

    return render_template("login.html")

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['Username']
        passowrd = request.form['Password']
        
    return render_template("signup.html")


if __name__ == "__main__":

    app.run(debug=True)