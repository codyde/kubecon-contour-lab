from flask_cors import CORS
from flask.logging import create_logger
from flask import Flask, jsonify, request, render_template, url_for
import os
import time

app = Flask(__name__)
LOG = create_logger(app)
app.secret_key = "super secret key"
CORS(app)

"""
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
"""

@app.route("/kubecon")
def home():
    return render_template('index.html')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
