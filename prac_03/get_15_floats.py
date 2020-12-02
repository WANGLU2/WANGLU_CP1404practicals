import random
def main():
    out_file = open("temps_input.txt", "w")

    i = 0
    while i < 15:
        i += 1
        temperature = random.uniform(-200, +200)
        print(temperature, file=out_file)


main()



