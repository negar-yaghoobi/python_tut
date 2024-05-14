letter = (input('enter one letter : ')).lower()

if len(letter) > 1:
    print('the length of the letter greater than 1 .')
else:
    if letter.isalpha() :
        if letter in ['a','o','i','e','u']:
            print('the letter is vowel')
        else:
            print('the letter is not vowel')
    else:
        print('letter is not in a..z')
