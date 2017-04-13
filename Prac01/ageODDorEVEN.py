def main():
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be greater than or equal to 0")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input. Enter a number.")
            age = int(input("Age: "))

def is_number_even(age):
    if age % 2 == 0:
        print("{} is even".format(age))
    else:
        print("{} is odd".format(age))

main()