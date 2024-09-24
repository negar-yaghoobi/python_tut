def calc_income(income):
    if income < 0 :
        print('invalid income')
        return

    return income * 2

user_income = int(input('Enter your number : '))
print(calc_income(user_income))


#=========================================================== raise 

def calc_income(income):
    if income < 0 :
        raise Exception('income should not be a negetive number!')            # create error
    
    print('first')
    return income * 2

user_income = int(input('Enter your number : '))

try:
    print(calc_income(user_income))
except:
    print('Exeption')

print('second')
