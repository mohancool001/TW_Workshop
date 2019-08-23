from FoodType import FoodType
class Food(object):
    """ Food class """
    id = 0
    name = ""
    typeOfFood = FoodType.default
    picUrl = ""

    def __init__(self, name, typeofFood):
        self.name = name
        self.typeOfFood = typeofFood

    def addPicUrl(self, url):
        self.picUrl = url