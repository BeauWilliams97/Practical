def main():
    words = {"the": 0, "it": 0, "know": 0, "a": 0, "how": 0, "is": 0, "fun": 0}
    user_input = input("Enter a word or sentence: ")
    for key in words.keys():
        if user_input in words.keys():
            words[user_input] += 1
    for word, count in words.items():
        print("{:4} - {:2}".format(word, count))

main()