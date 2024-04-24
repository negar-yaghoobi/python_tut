number = int(input('enter the number:'))
if number % 5 == 0 and number % 3 == 0:
    print('The number is divisible by 15')
elif number % 3 == 0 :
    print('The number is divisible by 3')
elif number % 5 == 0 :
    print('The number is divisible by 5')
else:
    print('The number is not divisible by any')
    