numbers = [3, 1, 4, 1, 5, 9, 2]
#Without running the code, write down your answers to these questions:
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[:-1] -> [3, 1, 4, 1, 5, 9]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# Write Python expressions (in the same Python file) to achieve the following:
# numbers[0] = "ten"
# numbers[-1] = 1
# numbers[2:]
# 9 in numbers

#Test:
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

numbers[0] = "ten"
print(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(9 in numbers)

