letter = input('enter one letter : ')

if len(letter) > 1:
    print('the length of the letter greater than 1 .')
else:
    if letter.isalpha() :
        if letter in ['a','A','o','O','i','I','e','E','u','U']:
            print('the letter is vowel')
        else:
            print('the letter is not vowel')
    else:
        print('letter is not in a..z')
