import random
import math
print(random.random())
# Random number b/w 0 to 100
num = int((random.random() * 1000) // 101) # gives random b/w 0 to 99
print(num)

# Randomly pick a number in a range
for i in range(3):
    print(random.randint(10, 20))

# Randomly pick a number from a list
members = ['john', 'marry', 'bob']
leader = random.choice(members)
print(leader)