import os
from flask import Flask, send_from_directory
from flask import Flask, render_template, Response, send_file, g, session, request
import json

app = Flask(__name__)

IMAGE_DIR = "static/images"
songs = []

# Sample song data
songs = [
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "coverUrl": "https://3icecream.com/img/banners/f/0b8lD690qQO1bDOib1IqiO0OO169o9IQ.jpg",
    },
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "coverUrl": "https://3icecream.com/img/banners/f/0b8lD690qQO1bDOib1IqiO0OO169o9IQ.jpg",
    },
    {
        "title": "Dance Monkey",
        "artist": "Tones and I",
        "coverUrl": "https://3icecream.com/img/banners/f/0b8lD690qQO1bDOib1IqiO0OO169o9IQ.jpg",
    },
    {
        "title": "Someone Like You",
        "artist": "Adele",
        "coverUrl": "https://3icecream.com/img/banners/f/0b8lD690qQO1bDOib1IqiO0OO169o9IQ.jpg",
    },
    {
        "title": "Uptown Funk",
        "artist": "Mark Ronson ft. Bruno Mars",
        "coverUrl": "https://m.media-amazon.com/images/I/61GJHS7W7lL._UF894,1000_QL80_.jpg",
    },
]

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
    import random
    return json.dumps(random.choice(songs))

def make_song_object_from_file(file):
    return {
        "title": file.split("-jacket")[0],
        "coverUrl": f"/static/images/{file}",
    }

if __name__ == "__main__":
    songs = os.listdir(IMAGE_DIR)
    songs = [make_song_object_from_file(file) for file in songs]
    print
    app.run(debug=True)
