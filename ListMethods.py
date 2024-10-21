numbers = [1, 2, 3, 1, 2]
numbers2 = numbers # same memory allocation for the lists.
numbers3 = numbers.copy() # different memory allocation
numbers.append(10)
numbers.insert(2, 50)
numbers.clear() # removes all the items
numbers.pop() # removes last number from array
if 2 in numbers:
    # safe to use this. if 2 in not present then it will throw console error.
    print(numbers.index(2)) # index of first occurance of 2
print(numbers.count(1)) # number of times 1 present in the list

numbers.sort() # remember print after sorting
print(numbers, numbers2, numbers3)
