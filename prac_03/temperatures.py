"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))

        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.

        else:
            print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


print("Thank you.")
main()
