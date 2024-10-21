def add_one(num):
    return num +11

print(add_one(10))

print(30 * '--')
#=====================================  send function to input another function

def func():
    print('this is my function')

def do_something(a):
    a()  # call function

do_something(func)

#=====================================  send function to input another function
print(30 * '--')


def func():
    print('this is my function')

def do_something(a):
    print('this is the first line of run do_something function')
    a()  # call function
    print('this is the last line of run do_something function')

do_something(func)


#========================================== send function and input arguments to inputs another function 
print(30 * '--')

def run_func_with_two_args(your_function, a, b):
    print('start')
    print(your_function(a, b))
    print('end')

def add_two_numbers(x, y):
    return x + y

run_func_with_two_args(add_two_numbers, 110, 22)

#========================================== send function and input arguments to inputs another function 
print(30 * '--')

def run_func_with_two_args(your_function, a, b, another_function):
    print('start')
    print(your_function(a, b))
    print('end')
    another_function()

def add_two_numbers(x, y):
    return x + y

def say_hello():
    print('hello')

run_func_with_two_args(add_two_numbers, 110, 22, say_hello)
