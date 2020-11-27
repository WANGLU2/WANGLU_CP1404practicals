"""
CP1404/CP5632 - Practical
Loops
"""
# loops Example:
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# loops Question a
for i in range(0,110,10):
    print(i, end=' ')
print()

# loops Question b
for i in range(20,0,-1):
    print(i, end=' ')
print()

# loops Question c
stars_number = int(input('Number of stars: '))
for i in range(stars_number):
    print('*', end='')
print()

# loops Question d
stars_number = int(input('Number of stars: '))
for i in range(1, stars_number + 1):
    print('*' * i)
print()
