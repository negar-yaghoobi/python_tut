#============================================= read()

file = open('names_2.txt', 'r')

a = file.read()
# print(type(a))
# print(a)

# print(a.split('\n'))

# for line in a.split('\n'):
#     print(line + 'y')
for name in a.split('\n'):                    # The first way is to move line by line on the information of a file
    print(f'hello {name.title()}')

#============================================ readlines()
file = open('names_3.txt', 'r')

b = file.readlines()

print(b)

#=============================================== readline()

# The second way is to move line by line on the information of a file

file = open('names_3.txt', 'r')

while True:
    line = file.readline()
    print(line,end='')
    if line == '':
        break
print('end....')