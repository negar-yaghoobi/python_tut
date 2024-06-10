# Game : Rock , Scissors , Paper

# import random

# list_choices = ['r','s','p']

# choice_meaning = {
#     's' : 'Scissors',
#     'p' : 'Paper' ,
#     'r' : 'Rock'
# }

# while True:
#     user_choice = input('select from Rock , Scissors , Paper : (r,s,p)')

#     ai_choice = random.choice(list_choices)

#     if user_choice in list_choices:
#         print(f'your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
#         if user_choice ==  ai_choice :
#             print('tie')
#         elif user_choice == 's' and ai_choice == 'p':
#             user_score +=1
#             print('you won!')
#         elif user_choice == 'p' and ai_choice == 'r':
#             user_score +=1
#             print('you won!')
#         elif user_choice == 'r' and ai_choice == 's':
#             user_score +=1
#             print('you won!')
#         else:
#             ai_score +=1
#             print('you lost!')
#     else:
#         print('input is invalid.')

print('---------------------------------------------------')

# import random

# list_choices = ['r','s','p']

# choice_meaning = {
#     's' : 'Scissors',
#     'p' : 'Paper' ,
#     'r' : 'Rock'
# }

# user_score = 0
# ai_score = 0

# for i in range(5):
#     user_choice = input('select from Rock , Scissors , Paper : (r,s,p)')

#     ai_choice = random.choice(list_choices)

#     if user_choice in list_choices:
#         print(f'your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
#         if user_choice ==  ai_choice :
#             print('tie')
#         elif user_choice == 's' and ai_choice == 'p':
#             user_score +=1
#             print('user_score +1')
#         elif user_choice == 'p' and ai_choice == 'r':
#             user_score +=1
#             print('user_score +1')
#         elif user_choice == 'r' and ai_choice == 's':
#             user_score +=1
#             print('user_score +1')
#         else:
#             ai_score +=1
#             print('ai_score +1!')
#     else:
#         print('input is invalid.')

#     print(f'user score : {user_score} / ai score : {ai_score}')
#     print('\n','-'*15,'\n' )

# if user_score > ai_score :
#     print(f'user won with score : {user_score}')
# elif user_score < ai_score:
#     print(f'ai won with score : {ai_score}')
# else :
#     print(f'it\'s a tie. score : {user_score}')

print('---------------------------------------------------')

import random

list_choices = ['r','s','p']

choice_meaning = {
    's' : 'Scissors',
    'p' : 'Paper' ,
    'r' : 'Rock'
}

user_score = 0
ai_score = 0

i = 0
while i < 5:
    user_choice = input('select from Rock , Scissors , Paper : (r,s,p)')

    ai_choice = random.choice(list_choices)

    if user_choice in list_choices:
        print(f'your choice is {choice_meaning[user_choice]}. AI choice is {choice_meaning[ai_choice]}.')
        i +=1
        if user_choice ==  ai_choice :
            print('tie')
        elif user_choice == 's' and ai_choice == 'p':
            user_score +=1
            print('user_score +1')
        elif user_choice == 'p' and ai_choice == 'r':
            user_score +=1
            print('user_score +1')
        elif user_choice == 'r' and ai_choice == 's':
            user_score +=1
            print('user_score +1')
        else:
            ai_score +=1
            print('ai_score +1!')
    else:
        print('input is invalid.')

    print(f'user score : {user_score} / ai score : {ai_score}')
    print('\n','-'*15,'\n' )

if user_score > ai_score :
    print(f'user won with score : {user_score}')
elif user_score < ai_score:
    print(f'ai won with score : {ai_score}')
else :
    print(f'it\'s a tie. score : {user_score}')