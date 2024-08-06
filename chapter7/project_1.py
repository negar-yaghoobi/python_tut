# random password generator

import string
import random

def get_value():
    while True:
        length = input('enter the length of password or type exit : ')
        if length.isdigit():
            return int(length)
        if length == 'exit':
            return 0
    
def get_setting():
    str_ = ''
    options_ = {'lower char' : string.ascii_lowercase,
               'upper char' : string.ascii_uppercase,
               'digits char' : string.digits,
               'sympol char' : string.punctuation,
               'space char' : ' '
               }
    for item in options_.keys():
        user_input = input(f'include {item}? (y : yes , n : no) : ')
        if user_input == 'y' or user_input == 'yes':
            # print(options_[item])
            str_ += options_[item]
    
    return str_

def random_choice(len_=8, setting_=''):
    password = ''
    for i in range(len_):
        if len(setting_) < 1 :
            return None
        char = random.choice(setting_)
        password +=char

    return(str(password))


length_ = get_value()
setting_ = get_setting()
print(random_choice(len_=length_, setting_=setting_))
