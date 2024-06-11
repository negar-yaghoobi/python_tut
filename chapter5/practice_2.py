#================================================================ solution_1

# import random

# number_of_cups = int(input('How many cups? : '))
# chances = int(input('How many chances? : '))


# ai_choice = random.choice(range(1,number_of_cups+1))
# print(f'the right answer is {ai_choice}')

# while chances != 0 :
#     print('-'*30)
#     print(f'{chances} chances left.')
#     guess = int(input(f'Guess [1-{number_of_cups}]: '))
    
#     if ai_choice == guess:
#         print('you guessed right.')
#         print('-'*30)
#         print('you won!')
#         break
#     else:
#         if chances == 1:
#             print('wrong guess.')
#             print('-'*30)
#             print(f'the right answer is {ai_choice}')
#             print('you lost. sorry!')
#         else:
#             print('wrong guess.')
#     chances -=1
    

# #==================================================================== solution_2

# import random
# cups = int(input('How many cups? : '))
# chances = int(input('How many chances? : '))

# ai_goal = random.randint(1,cups)
# line_length = 15

# print('-'*line_length)
# word = 's'

# for i in range(chances):
#     if chances -i == 1:
#         word = ''
#     print(f'{chances - i} chance{word} left.')
#     user_guess = int(input(f'Guess [1-{cups}]: '))

#     if user_guess == ai_goal:
#         print('you guessed right.')
#         break
#     else:
#         print('wrong guess.')
    
#     print('-'*line_length)

# if user_guess == ai_goal:
#     print('-'*line_length)
#     print('you won!')
# else:
#     print(f'the right answer is {ai_choice}')
#     print('you lost. sorry!')


#====================================================================solution_3

import random
cups = int(input('How many cups? : '))
chances = int(input('How many chances? : '))

ai_choice = random.choice(range(1,cups+1))
print(f'the right answer is {ai_choice}')

w = False
for i in range(chances,1,-1):
    print('-'*30)
    print(f'{i} chances left.')
    guess = int(input(f'Guess betwen [1, {cups}]: '))

    if guess == ai_choice:
        w = True
        break
    else:
        print("re de")

if w :
    print('win')
else:
    print('wrong')