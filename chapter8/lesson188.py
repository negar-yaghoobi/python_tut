#=================================================================== 1

class Line:
    def __init__(self, x_1, y_1, x_2, y_2):
        self.x_1 = x_1
        self.y_1 = y_1
        self.x_2 = x_2
        self.y_2 = y_2

    def __str__(self):
        return f'line: a = ({self.x_1}, {self.y_1})  b = ({self.x_2}, {self.y_2})'
    def len_line(self):
        return ((self.y_2 - self.y_1) ** 2 + (self.x_2 - self.x_1) ** 2) ** (1/2)
    
    def slope_line(self):
        return (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
    

line_1 = Line(1, 1, 3 ,3)

print(line_1)
print(line_1.len_line())
print(line_1.slope_line())

#=================================================================== 2
print(30 * '--')

class Line:
    def __init__(self, x, y):
        self.x_1 = x[0]
        self.y_1 = x[1]
        self.x_2 = y[0]
        self.y_2 = y[1]

    def __str__(self):
        return f'line: a = ({self.x_1}, {self.y_1})  b = ({self.x_2}, {self.y_2})'
    def len_line(self):
        return ((self.y_2 - self.y_1) ** 2 + (self.x_2 - self.x_1) ** 2) ** (1/2)
    
    def slope_line(self):
        return (self.y_2 - self.y_1) / (self.x_2 - self.x_1)
    

line_1 = Line((1, 1), (3 ,3))

print(line_1)
print(line_1.len_line())
print(line_1.slope_line())


#=================================================================== 3
print(30 * '--')

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __str__(self):
        return f'line: a = ({self.a[0]}, {self.a[1]})  b = ({self.b[0]}, {self.b[1]})'
    
    def len_line(self):
        return ((self.b[1] - self.a[1]) ** 2 + (self.b[0] - self.a[0]) ** 2) ** (1/2)
    
    def slope_line(self):
        return (self.b[1] - self.a[1]) / (self.b[0] - self.a[0])
    

line_1 = Line((1, 1), (3 ,3))

print(line_1)
print(line_1.len_line())
print(line_1.slope_line())


#=================================================================== 4
print(30 * '--')

class Line:
    def __init__(self, a, b):
        self.a = {'x': a[0], 'y': a[1]}
        self.b = {'x': b[0], 'y': b[1]}


    def __str__(self):
        return f'line: a = ({self.a['x']}, {self.a['y']})  b = ({self.b['x']}, {self.b['y']})'
    
    def len_line(self):
        return ((self.b['y'] - self.a['y']) ** 2 + (self.b['x'] - self.a['x']) ** 2) ** (1/2)
    
    def slope_line(self):
        return (self.b['y'] - self.a['y']) / (self.b['x'] - self.a['x'])
    

line_1 = Line((1, 1), (3 ,3))

print(line_1)
print(line_1.len_line())
print(line_1.slope_line())