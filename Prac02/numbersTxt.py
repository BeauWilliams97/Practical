__author__ = "Beau Williams"
file = open("numbers.txt", "r")
number_one = int(file.readline())
number_two = int(file.readline())
print(number_one + number_two)
file.close()
