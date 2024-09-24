#=========================================================== create error by using assert

def calc_income(income):
    assert income>=0, 'income should not be a negetive number!'


    print('first')
    return income * 2

user_income = int(input('Enter your number : '))
print(calc_income(user_income))

print('second')

#=========================================================== handling error 

def calc_income(income):
    assert income>=0, 'income should not be a negetive number!'


    print('first')
    return income * 2

user_income = int(input('Enter your number : '))

try:
    print(calc_income(user_income))
except:
    print('Exeption')

print('second')