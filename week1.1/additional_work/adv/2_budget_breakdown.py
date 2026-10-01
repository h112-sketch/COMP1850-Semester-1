"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = float(input("Travel cost in pounds: "))
food_cost_input = float(input("Food cost in pounds: "))
accommodation_cost_input = float(input("Accommodation cost in pounds: "))

total = travel_cost_input + food_cost_input + accommodation_cost_input
print(f"Total: {travel_cost_input + food_cost_input + accommodation_cost_input}")
print(f"Three costs by category: Travel Food Accomadation: {travel_cost_input, food_cost_input, accommodation_cost_input}")

# TODO: convert each value to a number type that supports decimals
# TODO: calculate the total and the average spend per category
# TODO: print the three costs, the total, and the average
# Extension: format the totals to two decimal places
