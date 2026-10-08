# Worksheet 1.2: Task 2 Solution
import argparse
import statistics

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

def readNumbers():
    with open(args.filename, "r") as f:
        numbers = [float(item) for item in f.read().split()]
    f.close()

    return numbers

def standardDeviation(numbers):
    return statistics.stdev(numbers)

numbers = readNumbers()
numbers.sort()
n = len(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers) / n)
print(numbers[n//2])
print(standardDeviation(numbers))

