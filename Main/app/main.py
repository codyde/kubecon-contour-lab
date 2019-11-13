from flask_cors import CORS
from flask.logging import create_logger
from flask import Flask, jsonify, request, render_template, url_for
import os
import time

app = Flask(__name__)
LOG = create_logger(app)
app.secret_key = "super secret key"
CORS(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/api")
def default_route():
    LOG.debug('this is a DEBUG message')
    LOG.info('this is an INFO message')
    LOG.warning('this is a WARNING message')
    LOG.error('this is an ERROR message')
    LOG.critical('this is a CRITICAL message')
    return jsonify('hello world')

@app.route("/api/health", methods=["GET"])
def get_health():
    stats = "{'status':'completed','platform':'healthy'}"
    return jsonify(stats)


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
