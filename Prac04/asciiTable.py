__author__ = "Beau Williams"


LOWER = 33
UPPER = 127
def main():
    character_input = str(input("Enter a character: "))
    while len(character_input) != 1:
        print("Invalid input. Enter a single character")
        character_input = str(input("Enter a character: "))

    number_input = get_number(LOWER, UPPER)
    print("Character: {0:>5} ASCII:     {1:>2}".format(character_input, ord(character_input)))
    print("Number:    {0:>5} Character: {1:>2}".format(number_input, chr(number_input)))

def get_number(LOWER, UPPER):
    valid_input = False
    while not valid_input:
        try:
            number_input = int(input("Enter a number: "))
            if number_input < LOWER or number_input > UPPER:
                print("Invalid number. Input must be between {} & {}".format(LOWER, UPPER))
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Enter a number.")
            number_input = int(input("Number:"))
        return number_input


main()
