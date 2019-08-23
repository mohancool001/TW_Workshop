from FoodyApp import FoodyApp

def main():
    
    FAHandler = FoodyApp("FoodyApp")
    FAHandler.FeedData()

    SearchLookup = raw_input("Search: ")
    RestList = FAHandler.DoLookup(SearchLookup)

    for rest in RestList:
        print(rest.name + " " + str(rest.FoodTypes))

if __name__ == "__main__":
    main()