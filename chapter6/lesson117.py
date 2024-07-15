# ------------------------------------ **kwargs
def sum_numbers(**kwargs):   
    print(kwargs)

sum_numbers(a=1, b=10, c='aaa')


print(30 * '--')
# ------------------------------------ *args + **kwargs

def sum_numbers(*args, **kwargs):   
    print(args, kwargs)

sum_numbers(10, 1, a=1, b=10, c='aaa')