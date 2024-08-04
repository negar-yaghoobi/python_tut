#============================================== solution 1

def is_perfect(number):
    sum_divs = 0
    for i in range(1,number):
        if number % i == 0:
            sum_divs += i
        else:
            continue 
    if sum_divs == number:
        return True
    else:
        return False
    

print(is_perfect(6))


#============================================== solution 2
print(30*'--')

def divisor(number):
    number_divisor = []
    for i in range(1,number+1):
        if number % i == 0:
            number_divisor.append(i)

    return number_divisor

def is_perfect(number):
    sum_divs = sum(divisor(number)) - number
    print(f'sum of divisors of {number} is {sum_divs}')
    return number == sum_divs
    

print(is_perfect(6))