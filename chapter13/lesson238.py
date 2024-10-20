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


#================================================= another solution

print('--- Current grades: ---')

with open('grades.txt', 'r') as grades_file:
    all_data = grades_file.read()
    print(all_data)

new_grades = []

yes_no_new_grades = input('Do you want add new grades?')

if yes_no_new_grades == 'yes':
    while True:
        name = input('Enter name: ')

        if name == 'exit':
            break

        grade = input('Enter grade: ')
        new_grades.append({
            'name': name,
            'grade': int(grade)
        })

with open('grades.txt', 'a') as grades_file:
    for student_grade in new_grades:
        grades_file.write(f"\n{student_grade['name']} {student_grade['grade']}")

all_student_grades = []
with open('grades.txt', 'r') as reader:
    all_data = reader.read()
    for line in all_data.split('\n'):
        x = line.split(' ')
        name = x[0]
        grade = x[1]
        all_student_grades.append(grade)
    
print(sum(all_student_grades)/len(all_student_grades))