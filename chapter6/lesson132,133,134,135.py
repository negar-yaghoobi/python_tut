a = 3
b = [1, 2, 3]
a = b
b[0] = 12
a[1] = 10

print(a)
print(b)


#========================================================
print(30 * '--')

c = 3
x = [1, 2, 3]
c = x
c = 12
x = [10,20,33]

print(x)
print(c)

#========================================================
print(30 * '--')


a = {
    'a': 1,
    'b': 2
}
b = a
b['c'] = 12
a['a'] = 10

print(a)
print(b)


#========================================================
print(30 * '--')

c = 3
x = 1
c = x
c = 12


print(x)
print(c)



#======================================================== function and input argument: list تغییر جزیی
print(30 * '--')


def custom(num_list):
    a = 2
    num_list.append(1000)
    print(num_list)

grades = [12, 23, 34, 45]
print(grades)
custom(grades)
print(grades)


#======================================================== function and input argument: dictionary تعییر جزیی
print(30 * '--')

def custom(a):
    my_string = 'value1'
    a['key1'] = my_string
    print(a)

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}
print(my_dict)
custom(my_dict)
print(my_dict)


#======================================================== function and input argument: dictionary  تغییر کلی
print(30 * '--')


def custom(a):
    my_string = 'value1'
    a = my_string
    print(a)

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}
print(my_dict)
custom(my_dict)
print(my_dict)


#======================================================== function and input argument: list and .copy()     (1)
print(30 * '--')

a = [1,2,3]
b = a.copy()

b[1] = ['x']
a[0] = 'z'
print(a)
print(b)

#======================================================== function and input argument: dictionary and .copy()    (1)
print(30 * '--')


def custom(a):
    my_string = 'value1'
    a['key1'] = my_string
    print(a)

my_dict = {
    'k1': 'v1',
    'k2': 'v2'
}
print(my_dict)
custom(my_dict.copy())
print(my_dict)


#======================================================== function and input argument: list    (2)
print(30 * '--')


def custom(num_list):
    copy_num_list = num_list.copy()
    a = 2
    copy_num_list.append(1000)
    print(copy_num_list)

grades = [12, 23, 34, 45]
print(grades)
custom(grades)
print(grades)
