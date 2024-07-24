nums = [1, 2, 3, 4, 5]

result = []
for num in nums:
    result.append(num ** 2)

print(result)


print(30 * '--')
#========================================== ~ map

my_num = [1, 2, 3, 4, 5]

def power_two(num):
    return num**2

for num in my_num:
    print(power_two(num))


print(30 * '--')
#======================================== map

my_num = [1, 2, 3, 4, 5]
print(my_num)

def power_two(num):
    return num**2

print(list(map(power_two, my_num)))
print(my_num)


print(30 * '--')
#======================================== map

my_num = [1, 2, 3, 4, 5]
print(my_num)

def power_two(num):
    return num**2

for item in map(power_two, my_num):
    print(item)

print(my_num)


print(30 * '--')
#======================================== map

names = ['ali alavi', 'ana jons', 'baran bara']

def extract_name(full_name):
    return full_name.split()[0]

print(list(map(extract_name, names)))


print(30 * '--')
#======================================== map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def plus_one(number):
    if number % 2 == 0:
        return number + 1
    else:
        return number
        

print(list(map(plus_one, numbers)))
        
    
print(30 * '--')
#======================================== map


names = ['ali', 'ana', 'baran', 'sara', 'reza']

def length(name):
    return(len(name))

print(list(map(length, names)))