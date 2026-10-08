# Worksheet 1.2: Task 1 Solution

import sys

grade = 0

try:
    grade = int(input("Enter an integer grade from 0 to 100"))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if grade < 0 or grade > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

result = ""
if grade >= 0 and grade <= 39:
    result = "Fail"
elif grade >= 40 and grade <= 69:
    result = "Pass"
else:
    result = "Distinction"

print(f"{grade} is a {result}")