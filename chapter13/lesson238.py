with open('grades.txt', 'w') as writer:
    writer.write('qqq 10\n')
    writer.write('www 12\n')
    writer.write('eee 15')

with open('grades.txt', 'r') as reader:
    file_info = reader.read()

list_info = file_info.split('\n')
print(list_info)

while True:
    user_input = (input('Do you want to add another name and mark or not? (yes:y or no:n) : ')).lower()
    if user_input in ['y', 'n']:
        if user_input == 'y':
            name = input('please enter the name : ')
            mark = input('please enter the mark : ')
            list_info.append(name + ' ' + mark)
            print(list_info)
            with open('grades.txt', 'a') as file:
                file.write(f'\n{name} {mark}')
        else:
            break
    else:
        print('your input is false')

with open('grades.txt', 'r') as reader:
    finall_file = reader.read()
print(finall_file)

sum_marks = 0
for str in list_info:
    sum_marks += int((str.split())[1])

avr = sum_marks / len(list_info)

print(f'average of marks = {avr}')
