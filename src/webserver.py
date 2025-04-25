from flask import Flask, render_template, Response
import camera

#Initialize the Flask app
app = Flask(__name__, template_folder="./webserver")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    return Response(camera.getWebStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

def run():
    app.run(debug=False, port=9900, host="0.0.0.0")