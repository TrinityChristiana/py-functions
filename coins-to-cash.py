# **************************** Challenge: Coins to Cash ****************************
"""
Author: Trinity Terry
pyrun: python coins-to-cash.py
"""

# Create a function that will take all your coins and convert it to the cash amount.


# The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
def calc_dollars(**coins):
    dollarAmount = 0
    dollarAmount += (coins["pennies"] * .01) + (coins["nickels"] * .05) + \
        (coins["dimes"] * .10) + (coins["quarters"] * .25)
    print(f"${dollarAmount}")

calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
# The output would be 8.07 when the function is executed with those arguments.
