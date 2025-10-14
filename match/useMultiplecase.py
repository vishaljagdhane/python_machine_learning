print("Try to multiple case in match case program other programing switch cases ")
taking_value = str(input("Enter a number: "))
match taking_value:
    case "vishal"|"Vishal":
        print("You have entered vishal {name} there is no case sensitivity in match case".format(name=taking_value))
    case _:
        print("You have entered other than vishal {name}".format(name=taking_value))
