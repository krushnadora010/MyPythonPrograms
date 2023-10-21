"""in multi level inheritance , we have parent ,child,grand child relationship"""
class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name  

class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age
   

class Grandchild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender
    
g=Grandchild()
g.get_name("ashok")
g.get_age(40)
g.get_gender("male")
g.show_name()
g.show_age()
g.show_gender()

    
        
                
