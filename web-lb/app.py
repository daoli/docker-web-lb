from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
hitcount = 0


@app.route('/')
def home():
    global hitcount
    hitcount += 1
    return f"Hello world from server {hostname}!\n\nI've been visited {hitcount} times."
