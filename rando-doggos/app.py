import random

from flask import Flask, render_template

app = Flask(__name__)

# list of doggo images
images = [
    "https://pbs.twimg.com/media/C6mYrK0UwAANhep.jpg",
    "https://pbs.twimg.com/media/C6k7SR5WwAABtb9.jpg",
    "https://pbs.twimg.com/media/C6atpTLWYAIL7bU.jpg",
    "https://pbs.twimg.com/media/C6Ryuf7UoAAFX4a.jpg",
    "https://pbs.twimg.com/media/C5oSiskU0AI2lcZ.jpg",
    "https://pbs.twimg.com/media/C5eTCOVUsAAWhvc.jpg",
    "https://pbs.twimg.com/media/C5d0QtvXMAI_7uz.jpg"
]


@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
