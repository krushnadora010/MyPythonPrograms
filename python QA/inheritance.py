class Person():
    def __init__(self,name,id,age):
        self.name=name
        self.id = id
        self.age = age
    def Display(self):
        print("my name is: ", self.name)
        print("my age is: ",self.id)
        print("my age is: ", self.age)

p=Person("krushna",1,22)
p.Display()            
        