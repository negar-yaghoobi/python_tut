def divisor(number):
    number_divisor = []
    for i in range(1,number+1):
        if number % i == 0:
            number_divisor.append(i)
        else:
            continue
    return number_divisor


print(divisor(100))
