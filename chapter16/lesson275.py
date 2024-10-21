#===================================== Defining a function in another function

def something():
    def say_hello(name):
        print( f'hello {name}')
    
    def say_goodbye():
        return 'goodbye'
    
    say_hello('negar')
    return say_goodbye()
    

print(something())