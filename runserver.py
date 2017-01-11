import time, sys, os
from flask import Flask, render_template
from flask_socketio import SocketIO

from rtmidi.midiutil import open_midiport

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app, async_mode='threading')
gif_path = 'static/gifs'

@app.route("/")
def index():
    gifs = os.listdir(gif_path)
    return render_template('index.html', gif_count=len(gifs))

@socketio.on('connect')
def handle_connect():
    print('connect')


beat_count = 0
last_beat = None
def beat_check():
    global beat_count
    global last_beat
    beat_count = beat_count + 1
    if beat_count >= 48:
        beat_count = 0
        now = time.time()
        if last_beat:
            time_diff = now - last_beat 
            bpm = 120/time_diff
        else:
            bpm = None
        last_beat = now
        print('beat')
        socketio.emit('beat', {'bpm':bpm})

class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port

    def __call__(self, event, data=None):
        message, _ = event
        if message[0] == 248:
            beat_check()

try:
    midiin, port_name = open_midiport(None, use_virtual=True, interactive=False)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Attaching MIDI input callback handler.")
midiin.ignore_types(timing=False)
midiin.set_callback(MidiInputHandler(port_name))

socketio.run(app, port=3000)
