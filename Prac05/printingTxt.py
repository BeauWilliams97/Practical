__author__ = "Beau Williams"
temp_file = open("temp.txt", "r")
user_name = temp_file.read().strip()
print("Your name is: ",user_name)
temp_file.close()
