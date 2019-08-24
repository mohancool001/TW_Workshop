from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(port='4000',debug = True)