def say_hello():
    print('hello')

def another_func():
    print('hi')
    say_hello()
    print('goodbye')

another_func()

#====================================
print(30 * '--')

def say_hello():
    print('hello')

def say_gn():
    print('goodnight')

def another_func(say_hello, say_gn):
    print('hi')
    say_hello()
    print('goodbye')
    say_gn()


another_func(say_hello, say_gn)

#======================================== decorator
print(30 * '--')


def say_hello():
    print('hello')

def my_decorator(input_func):
    def wrapper():
        print('start...')
        input_func()
        print('end...')

    return wrapper

a = my_decorator(say_hello)
a()
