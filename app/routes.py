from app import app, db
from flask import render_template, url_for, flash, redirect, session, request
from app.models import TennisCourt

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():

    return render_template("home.html")
