# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()
n = len(numbers)
print("Minimum =", min(numbers))
print("Maximum =", max(numbers))
print("Mean =", sum(numbers) / len(numbers))

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("Median =", median)

