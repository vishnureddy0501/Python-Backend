class Point:
    z = 100
    def __init__(self, x, y):
        # this is constructor
        self.x = x
        self.y = y
        print("constructor called after the object initialization")
    def move(self):
        print("move", self.z)
    def draw(self):
        print("draw")
point1 = Point(10, 20)
point1.move()
print(point1.x, point1.y)
point1.x = 11
print(point1.x, point1.y)


class Mammal: 
    def eat(self):
        print("Mammal is eating")

class Dog(Mammal): # dog inherits Mammal
    pass # placeholder if nothing to write here
class Cat(Mammal): # cat inherits Mammal
    pass # placeholder if nothing to write here

dog = Dog()
cat = Cat()
cat.eat()
dog.eat()


class A:
    def get(self):
        print("A's get method")

class B(A):
    def get(self):
        print("B's get method")
        super().get()

class C(A):
    def get(self):
        print("C's get method")
        super().get()

class D(B, C):
    def get(self):
        print("D's get method")
        super(B, self).get() # it means consider the classes after B in the method resolution order

d = D()
d.get()
# printing the method resolution order of a class.
print(D.mro())