from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        print("this is a abstraction method")

class Human(Animal):
    def move(self):
        print("i can walk and run")

class Snake(Animal):
    def move(self):
        print("i can crawl")

class Dog(Animal):
    def move(self):
        print("i can bark")

class lion(Animal):
    def move(self):
        print("i can roar")

h= Human()
h.move()

s=Snake()
s.move()

d= Dog()
d.move()

l=lion()
l.move()




               