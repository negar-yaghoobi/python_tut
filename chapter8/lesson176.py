class Car:
    def __init__(self, car_color, model):
        self.color = car_color
        self.model = model

    def turn_on_lights(self):
        print('lights on.')

    def print_color(self):
        print(f'car`s color is {self.color}')

    def rahnama_zadan(self, right_or_left):
        return f'{right_or_left} is on.'


my_car = Car('blue', 'bmw')

print(my_car.color)
print(my_car.model)
print(my_car.rahnama_zadan('rigth'))
my_car.turn_on_lights()
my_car.print_color()