file = open('names_2.txt', 'r')

a = file.read()
print(type(a))
print(a)

print(a.split('\n'))

for line in a.split('\n'):
    print(line + 'y')