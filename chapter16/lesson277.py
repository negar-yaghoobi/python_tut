#======================================== decorator

# decorator
def my_decorator(input_func):
    def wrapper():
        print('start...')
        input_func()
        print('end...')

    return wrapper

# use decorator
@my_decorator
def say_hello():
    print('hello')

# without decorator
def say_good_morning():
    print('good morning')

say_hello()