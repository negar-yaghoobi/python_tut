class Student:
    def __init__(self, name, family, avr):
        self.name = name
        self.family = family
        self.avr = avr

    def print_information(self):
        print(self.name, self.family, self.avr)

    def change_avr(self, avr):
        self.new_avr = avr
        return self.new_avr
    

std_1 = Student('negar', 'ygh', 15)

std_1.math = 20

print(std_1.math)

std_2 = Student('aaa', 'zzz', 10)

# print(std_2.math)

print(std_1.change_avr(19))