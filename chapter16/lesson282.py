def message_decorator(func):  
    def wrapper():  
        print("Before function execution!")  
        func()  
        print("After function execution!")  
    return wrapper

@message_decorator  
def display_message():  
    print("Inside the function!") 
     
display_message()