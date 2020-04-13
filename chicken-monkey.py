# **************************** Challenge: ChickenMonkey ****************************
"""
Author: Trinity Terry
pyrun: python chicken-monkey.py
"""

# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
    # For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number.
    # For the multiples of seven (7, 14, 21, etc.) print "Monkey".
    # For numbers which are multiples of both five and seven print "ChickenMonkey".
def chicken_monkey(num):
    item = ""
    if num % 5 == 0:
        item = "Chicken"
    if num % 7 == 0:
        item = f"{item}Monkey"
    
    if item == "":
        item = num
    print(item)  
for i in range(100):
    chicken_monkey(i + 1)