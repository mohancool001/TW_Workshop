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
        RestList = FAHandler.DoLookupForRests(RestNameStartsWith)

        if RestList:
            if len(RestList)>1:
                return {"error" : "Multiple Restaurants"},400
            FAHandler.setRestsRating(RestList, RatingValue)
            return {"error" : "Thank you for your ratings"},200
        else:
            return {"error" : "No Restaurants in such name"},400

if __name__ == "__main__":
    FAHandler.FeedData()
    app.run(port='3000',debug = True)