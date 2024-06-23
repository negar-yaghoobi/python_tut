import random

choice = random.choice(range(1,1000))

count = 0
while count != 3 :
    print(choice)
    if choice in [1,2,4]:
        count +=1
    if choice %2 != 0 :
        choice = choice * 3 + 1
    else:
        choice = choice // 2


print(f'sum : {sum}')