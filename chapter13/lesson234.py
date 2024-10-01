#========================================================== close() method

names_file = open('names.txt', 'r')

names = names_file.read()

names_file.close()

names = names.split('\n')

print(names)

while True:
    user_input = input('enter name: ')
    if user_input == 'exit':
        break
    names.append(user_input)
    print(names)

print(names)

#========================================================== close ()method in try-finally

names_file = open('names.txt', 'r')

try:
    names = names_file.read()
    
    names = names.split('\n')

    print(names)

    while True:
        user_input = input('enter name: ')
        if user_input == 'exit':
            break
        names.append(user_input)
        print(names)

finally:
    names_file.close()
