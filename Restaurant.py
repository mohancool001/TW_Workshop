import Food
import copy
import uuid
class Restaurant(object):
    """ Restaurent class """

    id = 0
    name = ""
    FoodItems = []
    FoodTypes = []
    Ratings = []
    AvgRating = 0
    NoOfRating = 0

    def __init__(self, name, typesofFood):
        self.id = uuid.uuid4()
        self.name = name
        self.FoodTypes = copy.deepcopy(typesofFood)

    def addFoodItems(self, foodItem):
        self.FoodItems.add(foodItem)
    
    def calcAvgRating(self):
        self.AvgRating = 0 # TODO CALCULATE BASED ON LAST ADDED ALONE
        for r in self.Ratings:
            self.AvgRating = self.AvgRating + int(r)
        
        self.AvgRating = self.AvgRating/len(self.Ratings)

    def giveRating(self,rating):
        self.Ratings.append(int(rating))
        self.calcAvgRating()
        self.NoOfRating = len(self.Ratings)
    
    def jsonifyMyself(self):
        jsontype = {
            "id": self.id,
            "name": self.name,
            "FoodItems": self.FoodItems,
            "FoodTypes": self.FoodTypes,
            "AvgRating": self.AvgRating,
            "NoOfRatings": self.NoOfRating
        }
        return jsontype