names = []
with open('names_5.txt', 'r') as file:
    for line in file.read().split('\n'):
        names.append(line)

    print('in here')

print(names)
print('end.......')