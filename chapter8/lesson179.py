#===================================== self
# def print_details(self,a):
#         return f'color: {self.color}, model: {self.model} {a}'

class Cars:
    def __init__(self, color,model):     # constructor
        self.color = color     # instance attribute
        self.model = model
    def print_details(self,a):
        return f'color: {self.color}, model: {self.model} {a}'
car_1 = Cars('red', 'bmw')              # instance
car_2 = Cars('yellow', 'xxx')


print(car_1.print_details(20))    # ~ print(Cars.print_details(car_1, 20))
# print(print_details(car_1, 20))  # error

print(Cars.print_details(car_1, 20))     