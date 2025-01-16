import os
from flask import Flask, send_from_directory
from flask import Flask, render_template, Response, send_file, g, session, request
import json
import random

app = Flask(__name__)

IMAGE_DIR = "./static/images"
songs = []

@app.route("/")
def home():
    with open('./templates/index.html', 'r') as file:
        return file.read();

@app.route('/static/images/<filename>')
def send_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

@app.route("/api/songs")
def get_songs():
    query = request.args.get("query", "").lower()
    suggestions = [song['title'] for song in songs if query in song['title'].lower()];
    return json.dumps(suggestions)

@app.route("/api/random-song")
def get_random_song():
    return json.dumps(random.choice(songs))

def make_song_object_from_file(file):
    return {
        "title": file.split("-jacket")[0],
        "coverUrl": f"/static/images/{file}",
    }

if __name__ == "__main__":
    songs = os.listdir(IMAGE_DIR)
    songs = [make_song_object_from_file(file) for file in songs]
    app.run(debug=False, host='0.0.0.0') 
