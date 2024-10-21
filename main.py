# print("hello world", "vishnu" * 10)
# name = input("enter your name? ")
# age = int(input("enter age? "))
# salary = float(input("enter sal? "))
# print(name, age, salary, type(age), type(salary))
# if you don't assign a multiline string to a variable then it will become a multi-line comment.
multiLineString = ''' Hello jon, 
How are you

This is a beautiful multiline string
'''
print(multiLineString)
name = 'vishnu'
print(name[1:-1])

# Formatted String. similar to `${name} is vishnu` in javascript
first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a Coder'
# lower, upper methods does not modify the original string. it returns new string.
# converts first letter of each word to uppercase
print(message, len(message), message.lower(), message.upper(), message.title())
print(message.find('hn'))

course = 'Python for Beginners'
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course, 'python' in course)
# 10 / 3 gives 3.333 (floating point)
# 10 // 3 gives 3 (result is always a integer)
# 10 **3  power operator

x = 10
print(abs(x))

import math
print(math.cos(x))

if x > 0: 
    print("greater")
elif x< 0:
    print("less than")
else:
    print("equals to 0")

if x > 0 or x < 0:
    print("x is not equal to 0")
else: 
    print("x is equal to 0")
# logical operators syntax: and, or, not

i = 0
while (i <= 10):
    print(i)
    i = i +1