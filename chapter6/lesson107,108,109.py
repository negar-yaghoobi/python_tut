#----------------------------------------------- sum to num and remain another num

def remain(num1, num2, num3):
    re = (num1 + num2) % num3
    return re


print(f'remain1 = {remain(2, 4, 5)}')

print('-'*30)
#----------------------------------------------- sum to num and remain another num

def remain(num1, num2, num3):
    re = (num1 + num3) % num2
    return re


print(f'remain2 = {remain(2, 4, 5)}')


print('-'*30)
#----------------------------------------------- celsius to fahrenheit
# f = (c * 1.8) + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print(f'temp = {celsius_to_fahrenheit(35)} fahrenheit')


print('-'*30)
#----------------------------------------------- fahrenheit to celsius
 
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


print(f'temp = {fahrenheit_to_celsius(95)} celsius ')


print('-'*30)
#----------------------------------------------- string between something

def make_string(middle, side):
    print(f'{side} {middle} {side}')


make_string('hello' , '---')

str_1 = 'hi'
str_2 = '***'

make_string(str_1 , str_2)



print('-'*30)
#----------------------------------------------- string between something


def make_string(middle, side):
    return f'{side} {middle} {side}'



print(make_string('by' , '---'))


print('-'*30)
#----------------------------------------------- sum of list

def calc_list_sum(my_list):
    result = 0
    for num in my_list:
        result = num + result

    return result


list_1 = [11, 2, 3, 4, 5, 6, 7, 8, 9]
print(calc_list_sum(list_1))


print('-'*30)
#----------------------------------------------- pass in function

def do_something():
    pass

print('hello')


print('-'*30)
#----------------------------------------------- None type

def do_something_1(name):
    print(name)

result = do_something_1('negar')
print(result)

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_1

def check_odd_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(check_odd_even(110))

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_2

def check_odd_even(number):
    result = False
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result

print(check_odd_even(110))

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_3

def check_odd_even(number):
    result = False
    if number % 2 == 0:
        result = True

    return result

print(check_odd_even(110))

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_4

def check_odd_even(number):
    result = number % 2 == 0

    return result

print(check_odd_even(110))

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_4

def check_odd_even(number):
    result = number % 2 == 0

    return result

print(check_odd_even(110))

print('-'*30)
#----------------------------------------------- check_odd_even of numbers   solution_4

def check_odd_even(number):
    number % 2 == 0

    return number % 2 == 0

print(check_odd_even(110))


print('-'*30)
#----------------------------------------------- check_evens numbers in list

def count_even(list_numbers):
    count = 0
    for i in list_numbers:
        if i % 2 == 0:
            count+=1
    return count

print(count_even([11,3,4,5,65,68,90]))
