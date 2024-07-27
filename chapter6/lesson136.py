user_number = int(input('enter your number : '))

def factorial_number(number):
    factorial = 1
    if number == 0:
        print(factorial)
    else:
        while number > 0:
            factorial = number * factorial
            number -= 1

    print(factorial)


factorial_number(user_number)


#======================================================
print(30*'--')

def factorial(n):
    result = 1

    for i in range (1, n+1):
        result *= i

    print(result)

factorial(user_number)


