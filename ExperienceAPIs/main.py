from FoodyApp import FoodyApp
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
app = Flask(__name__)
FAHandler = FoodyApp()

@app.route("/")
def index():
    return "Hello World"

@app.route("/search", methods=['POST'])
def searchLookup():
    LookupKey = str(request.form['term'])
    RestList = FAHandler.DoLookupForRests(LookupKey)
    Food = FAHandler.DoLookupForFoods(LookupKey)

    if RestList:
        JsonRestList = []
        for rests in RestList:
                jsonType = rests.jsonifyMyself()
                JsonRestList.append(jsonType)
        return jsonify(JsonRestList)
    else:
        #Food Type will be looked and based on the food type
        #and the rests that have that food it will be displayed
        return {"error" : "No Restaurants Available"},400

@app.route("/restaurants/rating", methods=['PUT'])
def giveRating():
    RestNameStartsWith = str(request.form['restName'])
    RatingValue = str(request.form['rating'])
    UserId = str(request.form.get('userId',''))
    RestList = FAHandler.DoLookupForRests(RestNameStartsWith)

    if not UserId:
        UserId = FAHandler.getAnonymousUserId()
    if RestList:
        if len(RestList)>1:
            return {"error" : "Multiple Restaurants"},400
        FAHandler.setRestsRating(RestList, RatingValue, UserId)
        return {"error" : "Thank you for your ratings"},200
    else:
        return {"error" : "No Restaurants in such name"},400

@app.route("/restaurants/rating", methods=['GET'])
def getAllRatings():
    RestNameStartsWith = str(request.form['restName'])
    RestList = FAHandler.DoLookupForRests(RestNameStartsWith)
    if RestList:
        if len(RestList)>1:
            return {"error" : "Multiple Restaurants"},400
        ratinginJson = FAHandler.seeAllRatings(RestList)
        return jsonify(ratinginJson),200

    else:
        return {"error" : "No Restaurants in such name"},400

@app.route("/user", methods=['GET'])
def getAllUsers():
    UserList = FAHandler.GetUsers()

    JsonList = []
    for user in UserList:
        JsonList.append(user.jsonifyMyself())
    if JsonList:
        return jsonify(JsonList),200
    return jsonify([]),200

@app.route("/user", methods=['POST'])
def createUser():
    userName = str(request.form['name'])
    FAHandler.AddUser(userName)
    return "OK. Ive Added a user",200

if __name__ == "__main__":
    FAHandler.FeedData()
    app.run(port='3000',debug = True)