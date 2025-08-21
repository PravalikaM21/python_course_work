#Class & Object:-
class car:
    # attributes
    name="BMW"
    color="blue"
    fueltype="dieseal"
    # methods
    def move(self):
        print("car is moving")
    def stop(self):
        print("stop the car")
car1=car()
print("car name",car1.name)
print("car color",car1.color)
print("car fueltype",car1.fueltype)
car1.move()
car1.stop()

car2=car()
print("car name",car2.name)
print("car color",car2.color)
print("car fueltype",car2.fueltype)
car2.move()
car2.stop()
#-------------------------------------

class car:
    def __init__(self,name,color,fueltype):
        self.name = name
        self.color = color
        self.fueltype = fueltype
        # methods
    def move(self):
        print("car is moving")
    def stop(self):
        print("stop the car")
# car 1
car1=car("bmw", "black", "petrol")
print("car name",car1.name)
print("car color",car1.color)
print("car fueltype",car1.fueltype)
car1.move()
car1.stop()
# Car 2
car2=car("audi", "white", "dieseal")
print("car name",car2.name)
print("car color",car2.color)
print("car fueltype",car2.fueltype)
car2.move()
car2.stop()




