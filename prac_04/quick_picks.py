import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45
def main():
    number_of_picks = int(input("How many quick picks?"))
    while number_of_picks <= 0:
        print("Number of quick picks have to greater than 0!")
        number_of_picks = int(input("How many quick picks?"))

    for i in range(number_of_picks):
        quick_pick_numbers = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM,MAXIMUM)
            while number in quick_pick_numbers:
                number = random.randint(MINIMUM,MAXIMUM)
            quick_pick_numbers.append(number)
        quick_pick_numbers.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick_numbers))






main()