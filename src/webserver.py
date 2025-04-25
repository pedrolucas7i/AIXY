from flask import Flask, render_template, Response
import camera

#Initialize the Flask app
app = Flask(__name__, template_folder="./webserver")

@app.route('/stream')
def stream():
    return Response(camera.getWebStream(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=False, port=9900)