def main():
    words = {"the": 0, "it": 0, "know": 0, "a": 0, "how": 0, "is": 0, "fun": 0}
    user_input = input("Enter a word or sentence: ")
    user_input_words = user_input.lower().split()
    string_examination(user_input_words, words)
    for word, count in words.items():
        print("{:4} - {:2}".format(word, count))

def string_examination(user_input_words, words):
    for word in user_input_words:
        if word in words:
            words[word] += 1

main()