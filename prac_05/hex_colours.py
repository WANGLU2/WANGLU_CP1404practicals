"""
CP1404/CP5632 Practical
Based on the state name example program above, create a program
that allows you to look up hexadecimal colour codes
"""
COLOR_NAME_TO_CODE = {'black': '#000000',
                      'blue1': '#0000ff',
                      'brown': '#a52a2a',
                      'coral': '#ff7f50',
                      'cyan1': '#00ffff',
                      'gray': '#bebebe',
                      'azure1':'#458b74',
                      'beige': '#838b8b',
                      'hotpink': '#ff69b4',
                      'khaki': '#f0e68c'}
print('Hexadecimal colour codes list:')
for key,value in COLOR_NAME_TO_CODE.items():
    print('{0:7} is {1}'.format(key,value))

color_name = input("Enter Color name: ").lower()
while color_name != "":
    if color_name in COLOR_NAME_TO_CODE:
        print(color_name, "is", COLOR_NAME_TO_CODE[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter Color name: ").lower()