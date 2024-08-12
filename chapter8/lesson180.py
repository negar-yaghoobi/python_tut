# ======================================================  kind of attributes

# ================================ 1 : instance attribute

class House:
    def __init__(self, color, nums_of_rooms, area):
        self.color = color              # instance attribute
        self.rooms = nums_of_rooms      # instance attribute
        self.area = area                # instance attribute
    
    def house_description(self):
        print(self.color, self.area, self.rooms)


house_1 = House('blue', 3, 120)
sum_house = House('red', 2, 30)

print(house_1.area)
print(house_1.color)
print(house_1.rooms)

house_1.color = 'jgcvj'
print(sum_house.area)
sum_house.house_description()
print(house_1.color)
print(sum_house.color)


# =============================== 2 : class attributes
print(30 * '--')


class Houses:
    country = 'iran'         #  class attributes
    x = 20                   #  class attribute
    def house_description(self):
        print(self.color, self.area, self.rooms)


house_11 = Houses()
sum_house_1 = Houses()

print(house_11.country)
print(sum_house_1.country)

house_11.y = 1000       # instance attribute
sum_house_1.country = 'usa'

print(house_11.y)         # add new attribute to this object
# print(sum_houseu.y)    # error

print(sum_house_1.country)
print(house_11.country)