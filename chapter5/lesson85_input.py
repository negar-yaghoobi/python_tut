# user_input = int(input('how many numbers? : '))

# list_numbers=[]

# for i in range(user_input):
#     user_number = int(input('enter your number: '))
#     list_numbers.append(user_number)

# print(list_numbers)

print('---------------------------------------')


# list_number=[]

# while True:
#     user_input = input('enter number')
#     if user_input == 'exit':
#         break
#     list_number.append(int(user_input))
    
# print(list_number)

print('--------------------------------------------')
# avr of marks
list_marks = []

count = 0

while True:
    mark = input('enter the marks : ')
    if mark == 'exit':
        break
    list_marks.append(int(mark))
    count +=1

avr = sum(list_marks)/count
print(f'avr : {avr}')

