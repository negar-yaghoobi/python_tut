number_1 = int(input('enter number1:'))
number_2 = int(input('enter number2:'))
choice = input('enter plus or minus or multiply:')

if choice in ['plus', 'minus', 'multiply']:
    if choice == 'plus':
        print(number_1 + number_2)
    elif choice == 'minus':
        print(number_1-number_2)
    else:
        print(number_1*number_2)
else:
    print('your choice is false')