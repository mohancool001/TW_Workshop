from Restaurant import Restaurant
from Food import Food
from DataFeeder import DataFeeder
from User import User

class FoodyApp(object):
    """ Main Fooody App Functionality Rests Here """
    dataFeed = ""
    fullRests = []
    fullUsers = []
    def __init__(self):
        self.dataFeed = DataFeeder()
        pass

    def FeedData(self):
        self.fullRests = self.dataFeed.createRestaurants()
        for eachrests in self.fullRests:
            self.dataFeed.addFoodsToRests(eachrests)
        self.AnonyUser = self.dataFeed.createAnonymousUser()
        #self.fullUsers.append(AnonyUser) TODO. Should we do this?
        
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
    def setRestsRating(self, rests, rating, userId):
        rests[0].giveRating(rating, userId)
        pass
    

    """ STAGE 3 """
    def getAnonymousUserId(self):
        return self.AnonyUser.id
    
    def seeAllRatings(self, RestList):
        jsonRatings = []
        for rating in RestList[0].Ratings:
            jsonRatings.append(rating.jsonifyMyself())
        return jsonRatings

    def GetUsers(self):
        return self.fullUsers

    def AddUser(self, userName):
        userobj = User(userName)
        self.fullUsers.append(userobj)