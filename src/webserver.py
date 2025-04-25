from flask import Flask, render_template, Response
import camera
import time

#Initialize the Flask app
app = Flask(__name__, template_folder="./webserver")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    while True:
        yield Response(camera.getWebStream(), mimetype='multipart/x-mixed-replace; boundary=frame')
        time.sleep(0.1)

def run():
    app.run(debug=False, port=9900, host="0.0.0.0")