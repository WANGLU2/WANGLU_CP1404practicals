"""
CP1404/CP5632 - Practical
Shop calculator program to determine total (discounted) price
"""

total_price = 0
item_number = int(input('number of items: '))
while item_number <= 0:
    print('The number of items should be > or = 1 : ')
    item_number = int(input('number of items: '))
for i in range(item_number):
    item_price = float(input('Price of item: '))
    total_price += item_price
if total_price > 100:
    total_price = total_price * 0.9
print('Total price for {} items is ${:.2f}'.format(item_number,total_price))
