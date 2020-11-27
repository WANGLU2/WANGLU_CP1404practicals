# Program 1
out_file = open("name.txt","w")
name = input("Enter your name please:")
print("Your name is:",name,file=out_file)
out_file.close()


#Program 2

file = open("name.txt","r")
name = file.read().strip()
print("Your name is:",name)
file.close()

#Program 3
in_file = open("numbers.txt","r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
result = number_1 + number_2
print(result)

in_file.close()

#Program 4
in_file = open("numbers.txt.","r")
total = 0
for line in in_file:
    number = int(line)
    total +=number
print(total)
in_file.close()
