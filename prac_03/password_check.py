def main():
    MINIMUM_LENGTH = 6
    password = input('Please enter a password of at least {} characters: '.format(MINIMUM_LENGTH))
    while not len(password) >= MINIMUM_LENGTH:
        password = input('Please enter a password of at least {} characters: '.format(MINIMUM_LENGTH))
    print('*' * len(password))

main()

