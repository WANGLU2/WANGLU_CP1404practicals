def main():
    out_file = open("temps_output.txt", "w")
    in_file = open("temps_input.txt", "r")

    for line in in_file:
        Fahrenheit  = float(line)
        print(convert_fahrenheit_to_celsius(Fahrenheit), file=out_file)



    in_file.close()


def convert_fahrenheit_to_celsius(Fahrenheit):
    celsius = 5 / 9 * (Fahrenheit - 32)
    return celsius
main()