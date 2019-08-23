from faker import Faker
from Restaurant import Restaurant
from Food import Food
import copy
from FoodType import FoodType

FoodFeed = {
    FoodType.Indian :[
    "Idli",
    "Dosa",
    "Vada",
    "Khichidi",
    "Poori"],

    FoodType.Chinese:[
    "Fried Rice",
    "Noodles",
    "Scheswan Rice",
    "Momos",
    "Wontons"],

    FoodType.Mexican:[
    "Quindesella",
    "Mexican 2",
    "Mexican 3",
    "Mexican 4",
    "Mexican 5"],

    FoodType.Italian:[
    "Pasta",
    "White Sauce",
    "Pizza",
    "LightPasta",
    "MozerallaCheese"],

    FoodType.American:[
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
    "BistroCafeChineItalia",
    "ParamountFastfood",
    "MFCChineseAmerica",
    "GreatAlmightChineseMexica",
]

class DataFeeder(object):
    """ Feed Food and Data Names """

    def createRestaurants(self):
        #10 Rests
        fullRestaurants = []

        fullRestaurants.append(Restaurant(RestaurantFeed[0], [FoodType.Indian.name  ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[1], [FoodType.Chinese.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[2], [FoodType.Mexican.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[3], [FoodType.Italian.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[4], [FoodType.American.name]))
        fullRestaurants.append(Restaurant(RestaurantFeed[5], [FoodType.Mexican.name, FoodType.Italian.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[6], [FoodType.Chinese.name, FoodType.Italian.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[7], [FoodType.Indian.name,  FoodType.Chinese.name ]))
        fullRestaurants.append(Restaurant(RestaurantFeed[8], [FoodType.Chinese.name, FoodType.American.name]))
        fullRestaurants.append(Restaurant(RestaurantFeed[9], [FoodType.Chinese.name, FoodType.Mexican.name ]))
        return fullRestaurants

    def addFoodsToRests(self, resObject):
        """ ADD the food based on the type the rest serves """
        for foodType in FoodFeed.keys():
            if foodType.name in resObject.FoodTypes:
                if resObject.FoodItems:
                    resObject.FoodItems.append(FoodFeed[foodType])
                else:
                    resObject.FoodItems = copy.deepcopy(FoodFeed[foodType])
            