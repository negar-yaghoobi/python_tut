a = 2

def custom_func(num):
    result = a + num
    return result


print(custom_func(110))


print(30 * '--')
#============================================== error : cant change global variable in function

a = 2

def custom_func(num):
    #a = a + num   # error ''cannot access local variable 'a' where it is not associat''
    print(a) 


custom_func(110)


print(30 * '--')
#============================================== can change global in function 

a = 2

def custom_func(num):
    global a
    a = a + num   # a : a global
    print(a) 

print(a)
custom_func(110)
print(a)