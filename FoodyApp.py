from Restaurant import Restaurant
from Food import Food
from DataFeeder import DataFeeder


class FoodyApp(object):
    """ Main Fooody App Functionality Rests Here """
    name = "FoodyApp"
    def __init__(self, name):
        self.name = name
        pass

    def FeedData(self):
        pass

    def DoLookup(self, searchTerm):
        rObj = Restaurant("A", ["Type"])
        res = [rObj]
        return res
