class Person(object):

	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def show_person_details(self):
		print(self.name)
		print(self.idnumber)


class Employee(Person):
	def __init__(self, name, idnumber, salary,post):
		Person.__init__(self, name, idnumber)
		self.salary = salary
		self.post= post
		

	def show_employee_details(self):
		print("employee salary is ", self.salary)
		print("employee post is ",self.post)
        
	    
a = Employee('Rahul', 886012, 200000, "software engineer")
a.show_person_details()
a.show_employee_details()
