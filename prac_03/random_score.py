import random
def main():

    print(generates_a_random_score())
    print(result(generates_a_random_score()))


def generates_a_random_score():
    score = random.randrange(1, 101)
    return score


def result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")

    else:
        print("Bad")


main()