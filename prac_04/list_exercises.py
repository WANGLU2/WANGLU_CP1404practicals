def main():
    numbers = []
    for number in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is", numbers[0])
    print("The last numner is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / 5 )
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    user_input_name = input("Please enter your name: ")
    if user_input_name in usernames:
        print("Access granted")
    else:
        print("Access denied")



main()