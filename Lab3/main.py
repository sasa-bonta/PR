from BeerMile import BeerMile

# Sasha sasa123
# About beer mile: https://www.youtube.com/watch?v=GZIqx7hldmI&ab_channel=YuriTheProfessional
# http://www.freeproxylists.net/
# Teodor, multumesc pentru proxy!!!

def displayOptions():
    print("\n1: Test getPage")
    print("2: Test login")
    print("3: Test getTop1000")
    print("4: Test loginCookies")
    print("5: Test headRequest")
    print("6: Test optionsRequest")
    y = int(input("Enter the option := "))
    return y

def chooseOption(x):
    global option
    if x == 1:
        beer_mile.getPage()
        option = displayOptions()
        chooseOption(option)

    elif x == 2:
        beer_mile.login()
        option = displayOptions()
        chooseOption(option)

    elif x == 3:
        beer_mile.getTop1000()
        option = displayOptions()
        chooseOption(option)

    elif x == 4:
        beer_mile.getLoginCookies()
        option = displayOptions()
        chooseOption(option)
    elif x == 5:
        beer_mile.headRequest()
        option = displayOptions()
        chooseOption(option)
    elif x == 6:
        beer_mile.optionsRequest()
        option = displayOptions()
        chooseOption(option)

option = None

if __name__ == "__main__":

    beer_mile = BeerMile("Sasha", "sasa123")
    option = displayOptions()
    chooseOption(option)


