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
        with open('/var/www/web-iot/data/data.json','r') as datafile:
            json_data = json.load(datafile)
        socketio.emit('update_data',json_data)
        with open('/var/www/web-iot/data/stpt.json','r') as stptfile:
            json_stpt = json.load(stptfile)
        socketio.emit('update_stpt',json_stpt)
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

@socketio.on('stpt')
def stpt(stpt_json):
    print("Running STPT!")
    with open('/var/www/web-iot/data/stpt.json','w') as outfile:
        json.dump(stpt_json,outfile)

@socketio.on('disconnect')
def disconnect():
    print("Client disconnected", request.sid)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app)
