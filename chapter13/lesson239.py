# ========================================== iterate in file with readlines

with open('grades.txt', 'r') as reader:
    for line in reader.readlines():
        print(line,end='')

#=========================================== iterate with list in file
print('\n')
print(30 * '--')

with open('grades.txt', 'r') as reader:
    for line in list(reader):
        print(line,end='')

#=========================================== iterate without list or readlines
print('\n')
print(30 * '--')

with open('grades.txt', 'r') as reader:
    for line in reader:
        print(line,end='')