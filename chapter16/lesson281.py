import functools

def this_is_mine(input_function):
    @functools.wraps(input_function)
    def wrapper(*args, **kwargs):
        print('this function is created by me')
        input_function(*args, **kwargs)

    return wrapper

@this_is_mine
def say_bye():
    print('bye')

print(say_bye)