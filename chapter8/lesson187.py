# magic method / dunder method

class Square:
    def __init__(self, side_length):
        self.s = side_length


square = Square(10)

print(square.s)

print(square)             # print address of object


print(30 * '--')
#============================================================== dunder method : __str__


class Square:
    def __init__(self, side_length):
        self.s = side_length

    def __str__(self):
        return f'square with side length of {self.s}'


square = Square(10)

print(square.s)

print(square)            # print sting in __str__()


print(30 * '--')
#============================================================== dunder method : __len__


class Square:
    def __init__(self, side_length):                            # dunder method
        self.s = side_length

    def __str__(self):                                          # dunder method
        return f'square with side length of {self.s}'


square = Square(10)

# print(len(square))       # error


print(30 * '--')
#============================================================== dunder method : __len__


class Square:
    def __init__(self, side_length):                        # dunder method
        self.s = side_length

    def __str__(self):                                      # dunder method
        return f'square with side length of {self.s}'

    def __len__(self):                                      # dunder method
        return self.s

square = Square(10)

print(len(square))      


print(30 * '--')
#============================================================== dunder method : __del__


class Square:
    def __init__(self, side_length):                        # dunder method
        self.s = side_length

    def __str__(self):                                      # dunder method
        return f'square with side length of {self.s}'

    def __len__(self):                                      # dunder method
        return self.s

    def __del__(self):                                      # dunder method
        print(f'square with {self.s}side length is deleted.')


square = Square(10)

del square