def run_function_for_n_times(n):
    def inner_decorator(original_function):
        def wrapper():
            for i in range(n):
                original_function()

        return wrapper
    
    return inner_decorator

@run_function_for_n_times(3)
def print_a():
    print('a')

@run_function_for_n_times(5)
def print_b():
    print('bb')

print_a()

print_b()