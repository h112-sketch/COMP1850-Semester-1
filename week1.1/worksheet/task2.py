"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Haris Mehmood
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer
try:
    savingAmount = int(input("How much money would you like to save every month"))
except:
    print("Invalid amount")
# Validate that they have entered an integer.

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
annualSavings = savingAmount * 12
# print this out for the user with a suitable message.
print(f"You will save £{annualSavings} a year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
total = annualSavings * 1.008
# print this out in the format £X.XX (to two decimal places).
print(f"With interest you will save £{total:.2f}")
