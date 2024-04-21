import random
person_choice = input('enter rock or paper or scissor : (r , p , s)')
ai_choice = random.choice(['s', 'r', 'p'])
print(ai_choice)

if person_choice in ['s', 'r', 'p']:
    if (person_choice == 's' and ai_choice == 'p') or (person_choice == 'r' and ai_choice == 's') or (person_choice == 'p' and ai_choice == 'r'):
        print('you Win')
    elif person_choice == ai_choice :
        print('you equal')
    else :
        print('you lose')
else :
    print('your choice is false')