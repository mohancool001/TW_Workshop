from Restaurant import Restaurant
from Food import Food
from DataFeeder import DataFeeder


class FoodyApp(object):
    """ Main Fooody App Functionality Rests Here """
    dataFeed = ""
    fullRests = []
    def __init__(self):
        self.dataFeed = DataFeeder()
        pass

    def FeedData(self):
        self.fullRests = self.dataFeed.createRestaurants()
        for eachrests in self.fullRests:
            self.dataFeed.addFoodsToRests(eachrests)
        
    """ STAGE 1 """
    def DoLookupForRests(self, searchTerm):
        selectedRests = []

        for rests in self.fullRests:
            if rests.name.startswith(searchTerm):
                selectedRests.append(rests)
        return selectedRests
        pass

    def DoLookupForFoods(self, searchTerm):
        pass
    
    def printRestsList(self, restList):
        for rest in restList:
            print(str(rest.id) + " " + rest.name + " " + str(rest.AvgRating))
    
    """ STAGE 2 """
    def setRestsRating(self, rests, rating):
        rests[0].giveRating(rating)
        pass