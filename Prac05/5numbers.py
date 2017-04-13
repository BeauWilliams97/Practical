number_list = []
for numbers in range(5):
    user_choice = input(int("Number: "))
    number_list.append(user_choice)
print("The first number is {}".format(number_list[0]))
print("The last number is", number_list[-1])
print("The smallest number is", min(number_list))
print("The largest number is", max(number_list))
print("The average of the numbers is", sum(number_list) / len(number_list))