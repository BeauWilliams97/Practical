MIN_LENGTH = 2
MAX_LENGTH = 6
REQUIRED_INTEGER = 1
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}",format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: {} ".format(password))


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        if SPECIAL_CHARACTERS in char:
            count_special += 1
    if count_lower >= 1 and count_upper >= 1 and count_digit >= 1:
        return True
    else:
        return False
main()
