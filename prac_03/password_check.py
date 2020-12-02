def main():
    MINIMUM_LENGTH = 6
    password = get_password(MINIMUM_LENGTH)
    while not len(password) >= MINIMUM_LENGTH:
        password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password(MINIMUM_LENGTH):
    password = input('Please enter a password of at least {} characters: '.format(MINIMUM_LENGTH))
    return password


main()

