from faker import Faker
from Restaurant import Restaurant
from Food import Food
from FoodType import FoodType

FoodFeed = {
    FoodType[2] :[
    "Idli",
    "Dosa",
    "Vada",
    "Khichidi",
    "Poori"],

    FoodType[3]:[
    "Fried Rice",
    "Noodles",
    "Scheswan Rice",
    "Momos",
    "Wontons"],

    FoodType[4]:[
    "Quindesella",
    "Mexican 2",
    "Mexican 3",
    "Mexican 4",
    "Mexican 5"],

    FoodType[5]:[
    "Pasta",
    "White Sauce",
    "Pizza",
    "LightPasta",
    "MozerallaCheese"],

    FoodType[6]:[
    "CheeseBurger",
    "Fries",
    "FriedCHicked",
    "PotatoWedges",
    "Salads"]
}

RestaurantFeed = [
    "Adyar Ananda Bhavan",
    "Wangs Kitchen",
    "PapaJohnsMexican",
    "OreganosItalia",
    "KFC",
    "FusilliMexicaItalia",
    "BistroCafeChineItalia"
    "ParamountFastfood"
    "MFCChineseAmerica"
    "GreatAlmightChineseMexica"
]



class DataFeeder(object):
    """ Feed Food and Data Names """

    def createRestaurants(self):
        #10 Rests
        RestsFull = [ ]

        for res in range(0,4):
            resObj = Restaurant(RestaurantFeed[res], FoodType[res+1])
            RestsFull.add(resObj)

    def createFood(self, typeofFood):
        # 30 foods
        for ftypes in FoodFeed.keys():
            if ftypes == typeofFood:
                for value in ftypes:
                    yield(ftypes[value])
            