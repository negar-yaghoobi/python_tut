number_1 = int(input('enter number1:'))
number_2 = int(input('enter number2:'))

sum = number_1 + number_2
if sum >=0 and sum <=20:
    if sum > 18 and sum <= 20:
        print(20)
    elif sum > 15 and sum <= 18:
        print(18)
    elif sum > 10 and sum <= 15:
        print(15)
    else:
        print('you didnot get enough marks')
else:
    print('numbers are false')