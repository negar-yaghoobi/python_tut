#========================================================================= without function
while True:
    user_input = input('Enter your number: ')
    try:
        user_input = int(user_input)
        break
    except ValueError:
        try:
            user_input = float(user_input)
            break
        except ValueError:
            print('your input is not digit. please enter correct number . ')

print(user_input, type(user_input))

#========================================================================= use function

def check_input(user_input):
    while True:
        try:
            result = int(user_input)
            return result , type(result)
        except ValueError:
            try:
                result = float(user_input)
                return result, type(result)
            except ValueError:
                print('your input is not digit. please enter a valid number . ')
                user_input = input('Enter your number: ')

    

user_input = input('Enter your number: ')
print(check_input(user_input))
