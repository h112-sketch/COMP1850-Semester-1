from data import Dataset

filename = input("Enter filename: ")
dataset = Dataset(filename)

print("Size:", len(dataset))
print("Mean:", dataset.mean())
print("Median:", dataset.median())

print("Values:")
for value in dataset:
    print(value)
