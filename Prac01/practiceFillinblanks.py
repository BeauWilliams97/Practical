finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter result: "))
        if result == int():
            pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:{}".format(result))
