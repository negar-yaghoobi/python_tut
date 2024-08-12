# =====================================================  self.pi_ 

class Circle:
    pi_ = 3.14   # class attr

    def __init__(self, r):
        self.radius = r

    def environment(self):
        return 2 * self.pi_ * self.radius         # self.pi_ ~ Circle.pi_
    
    def area(self):
        return self.pi_ * (self.radius ** 2)    # self.pi_ ~ Circle.pi_
    
    def calc_diameter(self):
        return self.radius * 2
    

circle_1 = Circle(10)

print(circle_1.area())

circle_1.pi_ = 3.1415

print(circle_1.area())

print(circle_1.environment())
print(circle_1.calc_diameter())


# =====================================================  Circle.pi_
print(30 * '--')


class Circle:
    pi_ = 3.14   # class attr

    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return Circle.pi_ * (self.radius ** 2)    # self.pi_ ~ Circle.pi_
    

circle_1 = Circle(10)

print(circle_1.area())

circle_1.pi_ = 3.1415

print(circle_1.area())
