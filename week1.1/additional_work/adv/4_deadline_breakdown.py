"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining_input = int(input("Minutes remaining until the deadline: "))
days = minutes_remaining_input // 1440
remaining = minutes_remaining_input % 1440
hours = remaining // 60
remaining = minutes_remaining_input % 60
minutes = remaining
print(f"{days} days, {hours} hours, {minutes} minutes!")
# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead
