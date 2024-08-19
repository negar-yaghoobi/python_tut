# polymorphism

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length


    # def area(self):


square = Square('square', 'a', 10)
# square.area()                          # error

#=============================================================== # abstract class
print(30 * '--')

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length


    def area(self):
        return self.side_length ** 2


square = Square('square', 'a', 10)
print(square.area())


#=============================================================== # abstract class
print(30 * '--')

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Circle(Shape):
    pi = 3.14
    def __init__(self, kind, name, r):
        super().__init__(kind, name)
        self.radius = r

    def area(self):                    # override
        return self.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length

    def area(self):                    # override
        return self.side_length ** 2
    
square = Square('square', 'a', 10)
print(square.area())

circle = Circle('circle', 'b', 10)
print(circle.area())


#=============================================================== # polymorphism
print(30 * '--')

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Circle(Shape):
    pi = 3.14
    def __init__(self, kind, name, r):
        super().__init__(kind, name)
        self.radius = r

    def area(self):                    # override
        return self.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length

    def area(self):                    # override
        return self.side_length ** 2

def show_area(s):
    print(s.area())


square = Square('square', 'a', 10)

circle = Circle('circle', 'b', 10)

show_area(square)
show_area(circle)




#===============================================================  # polymorphism
print(30 * '--')

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Circle(Shape):
    pi = 3.14
    def __init__(self, kind, name, r):
        super().__init__(kind, name)
        self.radius = r

    def area(self):                    # override
        return self.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length

    def area(self):                    # override
        return self.side_length ** 2

def show_area(s):
    print(s.area())


square = Square('square', 'a', 10)

circle1 = Circle('circle', 'b', 10)
circle2 = Circle('circle', 'b', 4)

for shape in [square, circle1, circle2]:
    show_area(shape)


#===============================================================  # polymorphism
print(30 * '--')

class Shape:                             # abstract class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of shape class should redefine the area method.')
    
class Circle(Shape):
    pi = 3.14
    def __init__(self, name, r):              # delete kind
        super().__init__('circle', name)       # add string 'circle' as kind
        self.radius = r

    def area(self):                    # override
        return self.pi * (self.radius ** 2)

class Square(Shape):
    def __init__(self, name, side_length):     # delete kind
        super().__init__('square', name)       # add string 'square' as kind
        self.side_length = side_length

    def area(self):                    # override
        return self.side_length ** 2

def show_area(s):
    print(s.area())


square = Square('a', 10)

circle1 = Circle('b', 10)
circle2 = Circle('b', 4)

for shape in [square, circle1, circle2]:
    show_area(shape)