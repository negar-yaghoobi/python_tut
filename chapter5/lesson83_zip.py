names = ['ali','sajad']
marks = [23,345]
x = [1,1,2,3,4]

#----------------------------------without pop
print('----------------------------------without pop')

z = list(zip(names,marks,x))
print(z)
for i in z:
    print(i)

print(z)
for i in z:
    print(i)

#----------------------------------with pop
print('----------------------------------with pop')

z = zip(names,marks)
print(list(z))
for i in z:
    print(i)

print(list(z))
for i in z:
    print(i)

#-------------------------------------------
print('----------------------------------------# indexing in zip')

for i in zip(names,marks):
    print(i[1])

#-------------------------------------------
print('----------------------------------------# tuple unpacking')
for i,j in zip(names,marks):
    print(i)

#-------------------------------------------

for name,mark in zip(names,marks):
    print(f'name = {name} , mark = {mark}')