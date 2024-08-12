#================================== pass in class

class Car:
    pass


car_1 = Car()
car_2 = Car()

print(car_1)
print(car_2)

print(car_2 == car_1)

car_3 = car_1
print(car_1 == car_3)


#==================================  encapsulation
print(30 * '--')

class Cars:
    def __init__(self, color,model):     # constructor
        self.color = color     # instance attribute
        self.model = model
    def print_details(self):
        print(self.color)
        print(self.model)

car_4 = Cars('red', 'bmw')              # instance
car_5 = Cars('yellow', 'xxx')

print(car_4.color)
print(car_4.model)

car_5.print_details()