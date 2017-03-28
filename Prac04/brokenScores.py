def main():
    score = float(input("Enter score: "))
    returned_score = score_storage(score)
    if score > 100 or score < 0:
        print("Invalid score")
    elif score > 50 and score < 90:
        print("Passable. You chose: {}".format(returned_score))
    elif score > 90 and score < 100:
        print("Excellent. You chose: {}".format(returned_score))
    else:
        print("Bad. You chose: {}".format(returned_score))

def score_storage(score):
    return score
main()