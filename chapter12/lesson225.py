class NegetiveIncomeError(Exception):           # creating a new type of error by using inheritance
    pass

class NegetiveAgeError(Exception):              # creating a new type of error by using inheritance
    def __init__(self, message, age):
        self.message = message
        self.age = age

# creating error by using raise
def check_age(age):
    if age < 0 :
        raise NegetiveAgeError('your age can not be negetive', age)
    
    return age * 2

# creating error by using raise
def check_income(num):
    if num < 0 :
        raise NegetiveIncomeError('your income can not be negetive')
    
    return num

user_income = int(input('Enter your income: '))
user_age = int(input('Enter your age: '))

# handle error
try:
    check_age(user_age)
except NegetiveAgeError as e:
    print(e.message, e.age)