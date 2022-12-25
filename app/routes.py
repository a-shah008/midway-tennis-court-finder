from app import app, db
from flask import render_template, url_for, flash, redirect, session, request
from app.scripts import construct_courts
from app.forms import UserLocationsForm
from app.map import get_coords, get_middle_coords, get_distance_between
from app.models import TennisCourt
import numpy as np
import ast

COURT_OBJS = construct_courts()

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():

    return render_template("home.html")

@app.route("/find_courts", methods=["GET", "POST"])
def find_courts():
    form = UserLocationsForm()
    ordered_courts = None

    if request.method == "POST":
        if form.validate_on_submit():
            location1 = get_coords(form.location1_coords.data)
            location2 = get_coords(form.location2_coords.data)
            if location1 == None or location2 == None:
                flash("Please enter valid GPS coordinates (longitude, latitude).", "warning")
                return redirect(url_for("find_courts"))

            mid_coords = list(get_middle_coords(location1[0], location1[1], location2[0], location2[1]))

            ordered_courts = dict(sorted(get_distance_between(mid_coords).items(), key=lambda item: item[1]))

            return redirect(url_for("results", ordered_courts=ordered_courts))

    return render_template("find_courts.html", form=form, ordered_courts=ordered_courts)

@app.route("/courts", methods=["GET", "POST"])
def courts():

    return render_template("courts.html", court_objs=COURT_OBJS)

@app.route("/results/<ordered_courts>", methods=["GET", "POST"])
def results(ordered_courts):
    ordered_courts_objs = []
    ordered_courts = ast.literal_eval(ordered_courts)
    for i in ordered_courts.keys():
        obj = TennisCourt.query.filter_by(name=str(i)).first()
        ordered_courts_objs.append(obj)

    return render_template("results.html", ordered_courts=ordered_courts, ordered_courts_objs=ordered_courts_objs)
