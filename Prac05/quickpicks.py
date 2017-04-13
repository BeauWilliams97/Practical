import random
user_choice = input("How many quick picks? > ")
for number in user_choice:
    print(random.randint(0, 50))

