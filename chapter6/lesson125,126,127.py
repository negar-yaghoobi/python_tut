#=========================================================== functional solution

import random

def get_input():
    """this function takes the input from the user and checks its correstness and returns the correct input."""
    
    while True:
        user_input = input('Enter your guess : ')
        if user_input.isalpha():
            return user_input.lower()
        print('your input is wrong. please enter again.')

def get_input_from_list(words):
    user_input = get_input()

    while user_input not in words:
        print('you should guess a word from the given words list!')
        print('please enter a correct word.')
        user_input = get_input()

    return user_input

def print_game_help():
    print('--' * 10)
    print('hi, welcome to the guess game.')
    print(f'all words : {list_of_words}')
    print('please start gussing.')
    print('--' * 10)


def run_game(number_of_rounds, words):
    print_game_help()
    print(f'number of guesses : {number_of_rounds}')

    ai_select = random.choice(words)
    print(ai_select)

    for i in range(number_of_rounds):
        user_input = get_input_from_list(list_of_words)
        
        if ai_select == user_input:
           print('you won !!!!')
           return
        else:
            print('you guessed wrong!')
            print(f'please try again! number of rounds left : {number_of_rounds-1-i}')
    print('you lose!')


list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']
run_game(5, list_of_words)

