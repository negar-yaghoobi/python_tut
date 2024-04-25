studends = {
    'name' : 'negar',
    'age' : 24,
    'mark' : 20,
    'major': 'computer'
}
for s in studends:
    print(s)

print('------------------------------------')

for s in studends.items():
    print(s)

print('------------------------------------')

for s in studends.values():
    print(s)

print('------------------------------------')

for s in studends.keys():
    print(s)

print('------------------------------------')

for a,b in studends.items():
    print(a)

print('------------------------------------')

for (a,b) in studends.items():
    print(a)