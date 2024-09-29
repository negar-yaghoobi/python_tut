# nemes_file = open('names.txt', 'w')

# for i in range(10):
#     name = input('Enter name: ')
#     nemes_file.write(f'{name}\n')

names_file = open('names.txt', 'r')

names = names_file.read()

names = names.split('\n')

print(names)

while True:
    user_input = input('enter name: ')
    if user_input == 'exit':
        break
    names.append(user_input)
    print(names)

print(names)