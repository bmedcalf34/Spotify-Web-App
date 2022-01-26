import os
from dotenv import find_dotenv, load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
import random
import flask
import requests

load_dotenv(find_dotenv())
app = flask.Flask(__name__)

AUTH_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

artists = ['spotify:artist:4pejUc4iciQfgdX6OKulQn', 'spotify:artist:1Yox196W7bzVNZI7RBaPnf', 'spotify:artist:3HCpwNmFp2rvjkdjTs4uxs'] 
#QOTSA, MEGADETH, KYUSS

@app.route("/")
def index():
    song_name, artist_name, preview, cover = pick_artist_and_song()
    return flask.render_template("index.html", song_name = song_name, artist_name = artist_name, preview = preview, cover = cover)
    #render template here

def pick_artist_and_song():
    num_list = [0, 1, 2]
    chosen_artist = random.choice(num_list) #create a list 1-3, choose random number, and assign that number as the artist

    song_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen_song = random.choice(song_list)

    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)


    results = sp.artist_top_tracks(artists[chosen_artist]) #the results wil be assigned to the random artist chosen from the list above

    track = results['tracks'][chosen_song - 1]
    artist_name = track['album']['artists'][0]['name']
    song_name = track['name']
    preview = str(track['preview_url'])
    cover = track['album']['images'][0]['url']
    print('track: ' + track['name'])
    print('audio: ' + str(track['preview_url']))
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
    #above function does what it appears to do, but for some reason only works all the way for kyuss

    return song_name, artist_name,  preview, cover


app.run(
    host = '0.0.0.0',
    port =int(os.getenv("PORT", 8080))
)