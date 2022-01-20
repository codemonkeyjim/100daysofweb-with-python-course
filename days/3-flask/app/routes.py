from flask import render_template
import json

from app import app

CHECKINS = "../data/untappd.json"


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/checkins")
def checkins():
    with open(CHECKINS) as checkins_fh:
        return render_template("checkins.html", checkins=json.load(checkins_fh))
