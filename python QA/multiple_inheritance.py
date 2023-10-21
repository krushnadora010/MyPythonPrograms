'''in multiple inheritance, the child inherits from more than  1 parent'''

class Parent1():
    def assign_str_one(self,str1):
        self.str1=str1
    def show_str_one(self):
        return self.str1

class Parent2():
    def assign_str_two(self,str2):
        self.str2=str2
    def show_str_two(self):
        return self.str2

class Child(Parent1,Parent2):
    def assign_str_three(self,str3):
        self.str3=str3
    def show_str_three(self):
        return self.str3
    
c=Child()
c.assign_str_one("i am a string of a parent one") 
c.assign_str_two("i am a string of a parent two") 
c.assign_str_three("i am a string of a child") 

c.show_str_one()
c.show_str_two()
c.show_str_three()



