def words_input():              #  get input from user
    user_input = ''
    list_word = []
    while user_input != 'done':
        user_input = input('enter words : ')
        if user_input != 'done':
            list_word.append(user_input)

    return list_word


def avr_length(list_word) :          # calcute average length of words in list
    length = 0
    for word in list_word :
        length = length + len(word)

    avr = length / len(list_word)

    return avr
    
list_word = words_input()
print(avr_length(list_word))         # ~ print(avr_length(words_input()))