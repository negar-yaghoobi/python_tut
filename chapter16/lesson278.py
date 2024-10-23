def run_twice(input_func):
    def wrapper():
        for i in range(2):
            input_func()
    return wrapper

@run_twice
def say_hello():
    print('hello')

@run_twice
def something():
    a = 11 + 2
    print(f'python is great! {a}')


say_hello()

something()