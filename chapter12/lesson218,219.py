print('start...')

user_number = int(input('enter number: '))

try:
    print('first...')
    print(100/user_number)
    print('third...')
except:
    print('exception occured')

print('end...')