# **************************** Challenge: Cash to Coins ****************************
"""
Author: Trinity Terry
pyrun: python cash-to-coins.py
"""
import math
# Now do the reverse. Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

def calc_coins(cash):
    piggyBank = {
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0
    }
    cents = cash * 100

    piggyBank["quarters"] = math.floor(cents // 25)
    cents -= piggyBank["quarters"] * 25

    piggyBank["dimes"] = math.floor(cents // 10)
    cents -= piggyBank["dimes"] * 10

    piggyBank["nickels"] = math.floor(cents // 5)
    cents -= piggyBank["nickels"] * 5

    piggyBank["pennies"] = math.floor(cents)
    print("real: ", piggyBank)

print("test: ", { 'quarters': 34, 'dimes': 1, 'nickels': 1, 'pennies': 4 })
calc_coins(8.69)