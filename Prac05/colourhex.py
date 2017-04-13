COLOURS = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE": "#7fffd4", "AZURE": "#f0ffff", "BLUE": "#ffebcd"}
colour_name = input("Enter name of colour: ").upper()
while colour_name != "":
    if colour_name in COLOURS:
        print("{:<5s} is {} ".format(colour_name, COLOURS[colour_name]))
    else:
        print("Invalid colour")
    colour_name = input("Enter name of colour: ").upper()