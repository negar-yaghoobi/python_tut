class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Dot(new_x, new_y)
         
    def __str__(self):
        return f'({self.x}, {self.y})'
    

def sum_two_numbers(a, b):
    result = a + b
    return result

p, q = 4, -1

a = Dot(sum_two_numbers(p, q), 2)
b = Dot(10, 3)

print(a + b)