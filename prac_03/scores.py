import random
def main():
    out_file = open("results.txt", "w")
    random_time = 4
    i =  0
    while i < random_time:
        i += 1
        print("{} is {}".format(generates_a_random_score(), resul(generates_a_random_score())), file=out_file)


def generates_a_random_score():
    score = random.randrange(1,101)
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