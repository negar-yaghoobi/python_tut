word = (input('enter the word')).lower()
word_reverse = word[::-1]
#print(word_reverse)

if word_reverse == word :
    print('this is Palindrome')
else:
    print('this is not Palindrome')
