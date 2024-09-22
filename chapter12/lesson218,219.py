print('start...')

user_number = int(input('enter number: '))

try:
    print('first...')
    print(100/user_number)
    print('third...')
except:
    print('exception occured')

print('end...')

# ================================================
print(30 * '--')


nums = [100, -10, 30, 46, 11]

print(f'list of numbers: {nums}')
print('select one of them with it\'s index.')


index = int(input('enter index: '))


def some_error():
    print(2 / 0)


def get_number_of_list_with_index(list_of_items, index):
    return list_of_items[index]


try:
    some_error()
    print(get_number_of_list_with_index(nums, index))
except:
    print('invalid index...')

print('some other code runnig...')