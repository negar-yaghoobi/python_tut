import random
import string
import os

settings = {
    'lower': True,
    'upper': True,
    'number': True,
    'symbol': True,
    'space': False,
    'length': 8
}

PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30

def clear_screen():
    os.system('cls')

def get_user_password_length(option, default, pw_min_length=
PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):
    while True:
        user_input = input('Enter password length. '
                           f'(Default is {default}) (enter: default) : ')

        if user_input == '':
            return default
        
        if user_input.isdigit():
            user_password_length = int(user_input)
            if pw_min_length <= user_password_length <= pw_max_length:
                return int(user_input)
            print('Invalid input.')
            print('password length should be'
                  f'between {pw_min_length} and {pw_max_length}.')
        else:
            print('Invalid input. You should enter a number.')
        
        print('Please try again.')

def get_yes_or_no_for_settings(option, default):
    while True:
        user_input = input(f'Include {option} ? '
                            f'(Default is {default}) '
                            '(y:yes, n: no, enter: default): ')

        if user_input == '':
            return default
        
        if user_input in ['y', 'n']:    # ~ if user_input == 'Y' or user_input == 'N':
            return user_input == 'y'    # ~ if user_input == 'Y' return true:
        
        print('Invalid input. please try again.')

def get_settings_from_user(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_for_settings(option, default)
            settings[option] = user_choice
        else:
            user_password_length = get_user_password_length(option, default)
            settings[option] = user_password_length

def ask_if_change_settings(settings):
    while True:
        user_answer = input('do you want to change default setting ? (y:yes, n: no, enter: yes):')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('--' * 5, 'çhange settings', '--' * 5, sep='')
                get_settings_from_user(settings)
            break
        else:
            print('invalid input')
            print('please try again.')

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_number():
    return random.choice('0123456789')

def get_random_symbol():
    return random.choice("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")

def generate_random_character(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '

def password_generator(settings):
    fianl_password = ''
    password_length = settings['length']

    choices = list(filter(lambda x: settings[x] == True, ['upper', 'lower', 'symbol', 'number', 'space']))     # ~ choices = []  , for key, value in settings.item():  ,  if value :   # ~ value == True:  ,   choices.append(key)
    
    for i in range(password_length):
        fianl_password += generate_random_character(choices)
    
    return fianl_password

def ask_user_to_generate_another_password():
    while True:
        user_answer = input('regenerate ? (y : yes, n : no, enter: yes) : ')
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                    return False
            return True
        else:
            print('invalid input')
            print('please try again.')

def password_generator_loop(settings):
    while True:
        print('--' * 30)
        print(f'Generated password : {password_generator(settings)}')

        if ask_user_to_generate_another_password() == False:
            break

def run():
    clear_screen()
    get_settings_from_user(settings)
    password_generator_loop(settings)
    print('thank you')

    

run()