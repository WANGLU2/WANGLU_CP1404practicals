import random
def main():

    print(generates_a_random_score())
    print(result(generates_a_random_score()))


def generates_a_random_score():
    score = random.randrange(1, 101)
    return score


def resul(score):
    if score >=90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()