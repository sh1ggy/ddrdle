import os
from flask import Flask, send_from_directory
from flask import Flask, render_template, Response, send_file, g, session, request
from datetime import datetime
import json
import random

app = Flask(__name__)

IMAGE_DIR = "./static/images"
AUDIO_DIR = "./static/audio"

songImages = []
songAudio = []


@app.route("/")
def home():
    with open("./templates/index.html", "r") as file:
        return file.read()


@app.route("/jacket")
def jacket():
    with open("./templates/game/jacket.html", "r") as file:
        return file.read()


@app.route("/track")
def track():
    with open("./templates/game/track.html", "r") as file:
        return file.read()


@app.route("/static/images/<filename>")
def send_image(filename):
    return send_from_directory(IMAGE_DIR, filename)


@app.route("/static/audio/<filename>")
def send_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)


@app.route("/api/images/daily")
def daily_jacket():
    date_int = int((datetime.today()).strftime("%Y%m%d"))
    return json.dumps(songImages[date_int % len(songAudio)])


@app.route("/api/audio/daily")
def daily_track():
    date_int = int((datetime.today()).strftime("%Y%m%d"))
    return json.dumps(songAudio[date_int % len(songAudio)])


@app.route("/api/images/songs")
def get_songs():
    query = request.args.get("query", "").lower()
    suggestions = [
        song["title"] for song in songImages if query in song["title"].lower()
    ]
    return json.dumps(suggestions)


@app.route("/api/audio/songs")
def get_audio():
    query = request.args.get("query", "").lower()
    suggestions = [
        song["title"] for song in songAudio if query in song["title"].lower()
    ]
    return json.dumps(suggestions)


@app.route("/api/images/random-song")
def get_random_image_song():
    return json.dumps(random.choice(songImages))


@app.route("/api/audio/random-song")
def get_random_audio_song():
    return json.dumps(random.choice(songAudio))


def make_song_images_object_from_file(file):
    return {"title": file.split("-jacket")[0], "imagesUrl": f"/static/images/{file}"}


def make_song_audio_object_from_file(file):
    title = file.split("-song")[0]
    return {
        "title": title,
        "audioUrl": f"/static/audio/{file}",
        "imagesUrl": f"/static/images/{title}-jacket.png",
    }


if __name__ == "__main__":
    songImages = os.listdir(IMAGE_DIR)
    songAudio = os.listdir(AUDIO_DIR)
    songImages = [make_song_images_object_from_file(file) for file in songImages]
    songAudio = [make_song_audio_object_from_file(file) for file in songAudio]
    app.run(debug=False, host="0.0.0.0", port=5001)
