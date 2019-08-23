import Food
import copy
class Restaurant(object):
    """ Restaurent class """

    id = 0
    name = ""
    FoodItems = []
    FoodTypes = []

    def __init__(self, name, typesofFood):
        self.name = name
        self.FoodTypes = copy.deepcopy(typesofFood)
    
    def addFoodItems(self, foodItem):
        self.FoodItems.add(foodItem)