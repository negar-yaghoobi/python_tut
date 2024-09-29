file = open('names_4.txt', 'r')

# a = file.readlines()
# print(a)

# while True:
#     line = file.readline()
#     print(line,end='')
#     if line == '':
#         break
# print('end....')

#========================================================

while True:
    line = file.readline()
    if line == '':
        break
    
    print(f'hello {line} ', end='')
    
print('end....')