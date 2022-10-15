from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Lock
import time
import json

# 
# Initializations
# 

# Thread initialsizations
thread = None
thread_lock = Lock()
counter = 0

# Flask Initialization
app = Flask(__name__)

# Socket Initialization
socketio = SocketIO(app)

#
# Functions
#

def data_relay():
    print("Starting communication thread")
    while True:
        with open('/home/arthur/Dev/testing/website-testing/data/data.json','r') as openfile:
            json_object = json.load(openfile)
        socketio.emit('update_data',json_object)
        time.sleep(1)
        
#
# Socket Functions
#

@socketio.on('connect')
def connect():
    global thread
    print("Front end connected")

    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(data_relay)

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected", request.sid)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app)
