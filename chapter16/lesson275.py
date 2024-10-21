#===================================== Defining a function in another function

def something_1():
    def say_hello(name):
        print( f'hello {name}')
    
    def say_goodbye():
        return 'goodbye'
    
    say_hello('negar')
    return say_goodbye()
    

print(something_1())

#===================================== Access to an internal function defined in another function, in the main program

def something_2():
    def add_two_numbers(x, y):
        return x + y
    
    return add_two_numbers

a = something_2()

print(a)

print(a(2, 3))