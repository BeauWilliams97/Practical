__author__ = "Beau Williams"
temp_file = open("temp.txt", "w")
user_name = input(str("What's your name: "))
print(user_name, file=temp_file)
temp_file.close()
