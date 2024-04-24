word = input('enter the word:')
length = len(word)
length = str(length)
length_y = length[-1]
#print(length_y)

even = ['0', '2', '4', '6', '8']
if length_y in even:
    print('even')
else:
    print('odd')