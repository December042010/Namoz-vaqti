from flask import Flask, render_template
from threading import Thread
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'Alive'

def run():
    app.run(
        host='0.0.0.0',
        port = random.randint(2000, 9000)
        )

def keep_alive():
    t = Thread(target=run)
    t.start()