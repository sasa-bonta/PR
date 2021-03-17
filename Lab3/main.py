from BeerMile import BeerMile

# Sasha sasa123

def chooseOption(x):
    global option
    if x == 1:
        beer_mile.getPage()
        print("\n1: Test login")
        print("2: Test getPage")
        print("3: Test getTop1000")
        option = int(input("Enter the option := "))
        chooseOption(option)

    elif x == 2:
        beer_mile.login()
        print("\n1: Test login")
        print("2: Test getPage")
        print("3: Test getTop1000")
        option = int(input("Enter the option := "))
        chooseOption(option)

    elif x == 3:
        beer_mile.getTop1000()
        print("\n1: Test login")
        print("2: Test getPage")
        print("3: Test getTop1000")
        option = int(input("Enter the option := "))
        chooseOption(option)


option = None

if __name__ == "__main__":

    beer_mile = BeerMile("Sasha", "sasa123")

    print("1: Test getPage")
    print("2: Test login")
    print("3: Test getTop1000")
    option = int(input("Enter the option := "))
    chooseOption(option)


