from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

# A local file server to send computercraft files.

@app.route('/<path:path>')
def index(path):
    return send_from_directory('.', path)