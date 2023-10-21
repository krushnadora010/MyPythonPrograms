class Vehicle:

    def __init__(self,mileage,cost):
        self.mileage= mileage
        self.cost= cost
        
    def show_vehicle_details(self):
        print("mileage of vehicle is ",self.mileage)  
        print("cost of vehicle is ",self.cost)
        print(" i am a vehicle")

v=Vehicle(40,200000)  
v.show_vehicle_details()

class Car(Vehicle):

    def show_car_details(self):
        print("i am a car")

c=Car(50,150000)
c.show_vehicle_details() 
c.show_car_details()       