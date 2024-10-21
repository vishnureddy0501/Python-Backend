numbers = [10, 10, 40, 30]
uniqueNumbers = []
for item in numbers:
    if item not in uniqueNumbers:
        uniqueNumbers.append(item)
print(uniqueNumbers)