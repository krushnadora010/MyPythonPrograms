from abc import ABC, abstractmethod

class Parent(ABC):
    def parent_property(self):
        print("this is a abstract base class or parent class")

class child(Parent):
    def child_property(self):
        super().parent_property()
        print("this is a sub cllass or child class")

c=child()
c.child_property()