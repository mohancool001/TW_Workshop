from FoodyApp import FoodyApp

def main():
    
    FAHandler = FoodyApp()
    FAHandler.FeedData()

    SearchLookup = raw_input("Search: ")
    RestList = FAHandler.DoLookup(SearchLookup)

    for rest in RestList:
        print(str(rest.id) + " " + rest.name + " " + str(rest.FoodTypes) + " " + str(rest.FoodItems))

if __name__ == "__main__":
    main()