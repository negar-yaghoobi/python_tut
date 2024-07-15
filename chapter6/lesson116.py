def sum_num(num1, num2):
    result = num1 + num2
    return result

num1 = int(input('enter num 1 : '))
num2 = int(input('enter num 2 : '))

print(f'sum numbers = {sum_num(num1, num2)}')



#========================================================
print(30 * '--')


def sum_num(num1, num2, num3):
    result = num1 + num2 + num3
    return result

num1 = int(input('enter num 1 : '))
num2 = int(input('enter num 2 : '))
num3 = int(input('enter num 3 : '))

print(f'sum numbers = {sum_num(num1, num2, num3)}')



print(30 * '--')
#======================================================== *args

def print_numbers(*args):
    for n in args:
        print(n)


print_numbers(1, 3, 4, 5, 6, 7, 'a')


print(30 * '--')
#======================================================== *args

def sum_numbers(*args):
    result_sum = 0
    for n in args:
        result_sum += n
    return result_sum

print(sum_numbers(1, 3, 4, 5, 6, 7))


print(30 * '--')
#======================================================== *args ~ *x

def sum_numbers(*x):
    result_sum = 0
    for n in x:
        result_sum += n
    return result_sum

print(sum_numbers(1, 3, 4, 5, 6, 7))