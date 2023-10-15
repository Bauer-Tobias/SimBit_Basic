from pathlib import Path
import os
import sys
import webbrowser
from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import eventlet # Forces pipreqs to add eventlet to requirements.txt

app = Flask(__name__)
app.config["SECRET_KEY"] = "b'q\xd3cn\x82N\xec\x13K\x0em\xfe\xc8\x10\x07('"
socketio = SocketIO(app)
RUNNING = False

# Path to watched file, time stamp of last modification and current file contents
FILE_PATH = ""
MTIME = 0
CONTENT = ""


def get_file_path():
    global FILE_PATH
    FILE_PATH = sys.argv[1]


def read_file():
    with open(FILE_PATH, "r") as f:
        content = f.read()
    return content
    
def get_imports():
    with open("imports.js","w") as f:
        f.write("const impArr = [];")
    for p in Path('./imports').glob('*.py'):
        with open("imports.js","a") as f:
            f.write("\nimpArr.push([\"" + p.name + "\",`" + p.read_text() + "`]);")


# Flask route to serve the index page
@app.route("/")
def serve_index():
    response = send_from_directory(os.getcwd(), "index.html")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


# Flask route to serve any file request
@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory(os.getcwd(), filename)


# If at least one client has connected to the server, start observing the file
@socketio.on("new_client")
def connect_new_client():
    if not RUNNING:
        file_watcher()


# Allows clients to request current content without waiting for the next file change
@socketio.on("initialize_sim_content")
def initialize_sim_content():
    socketio.emit("update_content", {"content": CONTENT})


# Constantly watch the file and emit update_content when change occurs
def file_watcher():
    global MTIME
    global RUNNING
    global CONTENT
    RUNNING = True

    while True:
        new_mtime = os.path.getmtime(FILE_PATH)

        if new_mtime != MTIME:
            CONTENT = read_file()
            MTIME = new_mtime
            socketio.emit("update_content", {"content": CONTENT})

        socketio.sleep(1)


if __name__ == "__main__":
    get_file_path()
    get_imports()
    webbrowser.open_new("http://localhost:5000/")
    socketio.run(app)
