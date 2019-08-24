from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from OAuthApp import OAuthApp
import json
app = Flask(__name__)
OAHandler = OAuthApp()

@app.route("/")
def index():
    return "Hello World"

@app.route("/register", methods=['POST'])
def registerUser():
    userName = str(request.form['name'])
    userPassword = str(request.form['password'])
    OAHandler.createUser(userName, userPassword)
    return "I Have created a user", 200

@app.route("/login", methods=['POST'])
def loginUser():
    userName = str(request.form['name'])
    userPassword = str(request.form['password'])
    access_token, verified = OAHandler.loginUser(userName, userPassword)

    if not verified:
        return "Not Valid User", 200
    return jsonify({"accessToken": access_token}),200

@app.route("/validate", methods=['POST'])
def validateToken():
    accessToken = str(request.form['accessToken'])
    verified = OAHandler.validateToken(accessToken)

    return jsonify({'Verification': verified}), 200

if __name__ == "__main__":
    app.run(port='5000',debug = True)
