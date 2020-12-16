"""
CP1404/CP5632 Practical
Write a program that stores
users' emails (unique keys) and names (values) in a dictionary.
"""
def get_name(email):
    prefix = email.split('@')[0]
    name_part = prefix.split('.')
    name = ''.join(name_part).title()
    return name

def main():
    email_to_name = {}
    email = input('Email: ')
    while not email == '':
        name = get_name(email)
        check = input('Is your name {0}?(Y/N)'.format(name)).upper()
        if check == 'N':
            name = input('Name:')
        if check != 'N' and check != 'Y':
            print('Please enter (Y/N)!')
            continue

        email_to_name[email] = name
        email = input('Email: ')

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))

main()













