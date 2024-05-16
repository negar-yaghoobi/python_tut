number = input('enter the number : ')
number_list = list(number)
# print(number_list)
sum_num = 0
for num in number_list:
    sum_num = sum_num + int(num)

print(sum_num)

print('--------------------------------------------------')
# another solution

number = input('enter the number : ')
sum_num = 0
for num in number:
    sum_num = sum_num + int(num)

print(sum_num)

print('--------------------------------------------------')
# another solution + while that the program to be repeated.
while True:
    user_input = int(input('enter the number :'))
    result = 0 
    while user_input != 0:
        result += user_input % 10
        user_input = user_input //10
    print(result)

