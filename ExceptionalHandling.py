# if you don't handle exceptions for errors then program terminates unexpectedly.
try:
    # try to enter characters. string is not converted to int. Hence throws errors
    age = int(input("enter age: "))        
    print(age)
except ValueError:
    print("value error occured")
