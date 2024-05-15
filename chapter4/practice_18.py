word = input('enter the word : ')
length = len(word)
j = int(length/2)

if length % 2 == 0 :
    i = int((length/2)-1)
    mid = word[i:j+1]
    print(mid)
else:
    mid = word[j]
    print(mid)