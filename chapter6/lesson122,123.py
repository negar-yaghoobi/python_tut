a = 3

def my_function():
    a = 11
    b = 2
    print(a)


print(a)     # global scope

my_function()   # local scope

print(a)  # global scope



print(30 * '--')
#======================================

a = 1
b = 2
c = 3

def print_abc():
    a = 55
    print(a)
    b = 66
    print(b)

print(a)
print(b)
print_abc()
print(a)
print(b)



print(30 * '--')
#======================================


a = 1
b = 2


def custom_func():
    a = 55
    print(a)
    
def custom_func2():
    a = 5
    print(a)

print(a)

custom_func()

print(a)

custom_func2()


print(30 * '--')
#======================================


a = 1
b = 2


def custom_func():
    print(a)
    
def custom_func2():
    a = 5
    print(a)

print(a)

custom_func()

print(a)

custom_func2()


print(30 * '--')
#======================================


a = 1
b = 2


def custom_func():
    a = 55
    if True:
        a = 0
        print(a)
    print(a)
    
def custom_func2():
    a = 5
    print(a)

print(a)

custom_func()

print(a)

custom_func2()


print(30 * '--')
#======================================

user_name = 'negar sarmast'

def get_title_case(my_string):
    """return the title case of the input"""
    my_string += 'hello'


    return my_string.title()

print(get_title_case(user_name))


def get_upper_case(my_string):
    """return the upper case of the input"""

    return my_string.upper()


print(get_title_case(user_name))
print(get_upper_case(user_name))



print(30 * '--')
#======================================

user_name = 'negar sarmast'

def get_title_case(my_string):
    """return the title case of the input"""

    return my_string.title()

print(get_title_case(user_name))


def get_upper_case(my_string):
    """return the upper case of the input"""
    my_string += 'hello'

    return my_string.upper()


print(get_title_case(user_name))
print(get_upper_case(user_name))



print(30 * '--')
#======================================

user_name = 'negar sarmast'
a = 1

def custom_func3():
    print(a)

def get_the_first_word(my_string):
    return my_string.split()[0]

def get_upper_case_first_word(my_string):
    """return the upper case of the input"""
    my_string = get_the_first_word(my_string)

    return my_string.upper()



print(get_upper_case_first_word(user_name))


print(30 * '--')
#======================================

user_name = 'negar sarmast'
a = 1

def custom_func3():
    print(a)

def get_upper_case_first_word(my_string):
    """return the upper case of the input"""

    def get_the_first_word1(my_string):
        return my_string.split()[0]
    
    my_string = get_the_first_word1(my_string)

    return my_string.upper()


#print(get_the_first_word1(user_name))   # error!!!!!!!!!!    local scope
print(get_upper_case_first_word(user_name))