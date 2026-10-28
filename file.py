from mypackage.calculator import add, subtract
# 1. INHERITANCE

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

d1 = Dog()
d1.eat()
d1.bark()


# 2. COMPOSITION

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

c1 = Car()
c1.start_car()


# 3. PACKAGING



print(add(10, 20))
print(subtract(20, 10))

