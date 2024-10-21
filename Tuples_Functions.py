# Tuples are immutable. once they are created, they can't be modified

data = ('vishnu', 20, 'rams')
print(data, data[0], 'vishnu' in data, 'sneha' in data)


def MyFunction(name = "sneha"):
    print(name)
    return 10
print(MyFunction("vishnu"))
print(MyFunction())