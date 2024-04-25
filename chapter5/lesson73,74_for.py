names = ['negar', 'sajad', 'aaa' , 'sss']
for name in names:
    print(name)

print('-----------------------------------------')
for i in [11, 2, 3, 4, 5, 6, 76] :
    print(i*2)

print('-----------------------------------------')
my_str = 'i love you sajad'
for j in my_str:
    print(j)

print('-----------------------------------------')
my_tuple = (11 ,2, 23, 4, 'hello')
for t in my_tuple:
    print(t , '123')

print('-----------------------------------------')
numbers = [23, 354, 354, 5467, 567, 678, 90]
for num in numbers:
    if num % 2 == 0:
        print(num, 'even')
    else:
        print(num, 'odd')

print('-----------------------------------------')
my_str = 'i love you'
count = 0
for char in my_str:
    if char == 'o':
        count +=1
print(count)
