def this_is_mine(input_function):
    def wrapper(*args, **kwargs):
        print('this function is created by me')
        input_function(*args, **kwargs)

    return wrapper


@this_is_mine
def say_bye():
    print('bye')

@this_is_mine
def multipy_three_numbers(x, y, z):
    print(x * y * z)

@this_is_mine
def add_two_numbers(a, b):
    print(a + b)

say_bye()

#======================================== 
print(30 * '--')


add_two_numbers(1, 2)


#========================================
print(30 * '--')


multipy_three_numbers(11, 2, 3)