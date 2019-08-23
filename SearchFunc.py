from FoodyApp import FoodyApp

def main():
    
    FAHandler = FoodyApp()
    FAHandler.FeedData()

    while(1):
        doWhat = raw_input("Search or Rate?")

        if(int(doWhat) == 1):
                SearchLookup = raw_input("Search: ")
                RestList = FAHandler.DoLookup(SearchLookup)
                FAHandler.printRestsList(RestList)
        else:
                RestName = raw_input("Restaurant Name?")
                RatingValue = raw_input("Whats the Rating?")
                RestList = FAHandler.DoLookup(RestName) # Hopefully only one should return. TODO
                FAHandler.setRestsRating(RestList, RatingValue)

if __name__ == "__main__":
    main()