import os
from dotenv import find_dotenv, load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import random
import flask
import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user,
    login_required,
)

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

AUTH_URL = "https://accounts.spotify.com/api/token"
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
DATABASE_URL = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)
app.secret_key = bytes(os.getenv("SECRET_KEY"), "utf-8")

login_manager = LoginManager()
login_manager.init_app(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    artists = db.Column(db.ARRAY(db.String(64)), nullable=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def __repr__(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    return Task.query.filter_by(username=username).first()


# db.create_all()
# db.drop_all()


@app.route("/")
def index():
    return flask.render_template("login.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_name = flask.request.form["username"]
        if Task.query.filter_by(username=user_name).first() == None:
            return flask.redirect("/signup")
        else:
            login_user(Task.query.filter_by(username=user_name).first())
            return flask.redirect("/add_artists")
    return flask.redirect("/add_artists")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_name = flask.request.form.get("new_username")
        task = Task(username=user_name, artists=[])
        db.session.add(task)
        db.session.commit()
        return flask.render_template("index.html")
    return flask.render_template("signup.html")


@app.route("/add_artists", methods=["GET", "POST"])
def add_artists():
    if request.method == "POST":
        username = current_user.username
        user = Task.query.filter_by(username=username).first()
        _ids = list(user.artists)
        _ids.append(flask.request.form.get("new_artist"))
        user.artists = _ids
        print(user.artists, "hi")
        db.session.commit()
        return flask.redirect("/artists")
    return flask.render_template("index.html")


@app.route("/artists")
def artists():
    song_name, artist_name, preview, cover = pick_artist_and_song()
    return flask.render_template(
        "index.html",
        song_name=song_name,
        artist_name=artist_name,
        preview=preview,
        cover=cover,
        current_user=current_user,
    )


def pick_artist_and_song():
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    Task.query.filter_by(username=current_user.username).first().artists
    artists = Task.query.filter_by(username=current_user.username).first().artists
    pick = random.choice(artists)

    song_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_song = random.choice(song_list)

    results = sp.artist_top_tracks(pick)
    track = results["tracks"][chosen_song - 1]
    artist_name = track["album"]["artists"][0]["name"]
    song_name = track["name"]
    preview = str(track["preview_url"])
    cover = track["album"]["images"][0]["url"]

    return song_name, artist_name, preview, cover


app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
