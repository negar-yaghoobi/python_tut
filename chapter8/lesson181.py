class House:
    country = 'iran'         # create class attribute
    x = 1100                 # create class attribute

    def __init__(self, color, rooms, a):
        self.color = color           # create a instance attribute
        self.rooms = rooms           # create a instance attribute
        self.a = a                   # create a instance attribute

    def house_description(self):
        return self.a
    
house_1 = House('qq', 2, 23)

print(house_1.a)

del house_1.a

#print(house_1.a)             # error     because just there is a attribute with this name

house_2 = House('ww', 4, 45)
print(house_2.a)

house_2.country = 'zzz'    # create a instance attribute

print(house_2.country)

print(house_1.country)

del house_2.country        # delete instance attribute

print(house_2.country)    # not error because there are two attributes with this name and now use class attribute