list_y = [1,2,3,4,5,6,7,8,9]
for i in enumerate(list_y):
    print(i)

print('-----------------------------------------')

list_x = [1,2,3,4,5,6,7,8,9]
for index,num in enumerate(list_x):
    list_x [index] = list_x[index]+1
print(list_x)

print('-----------------------------------------')

list_x = [1,2,3,4,5,6,7,8,9]
for index,num in enumerate(list_x):
    list_x [index] = list_x[index]+1
    print(f'index : {index}, num : {num}')

print('-----------------------------------------')

names = ['ali','amir','negar','zahra']
ages = [11,23,34,45]
marks = [10,15,20,18]
for index, name in enumerate(names):
    print(f'name = {name} , age = {ages[index]} , mark = {marks[index]}')