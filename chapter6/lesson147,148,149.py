#======================================================== solution 1


def diamond(diameter):
    if diameter % 2 == 0 :
        diameter +=1
    my_str = '*'
    for i in range(1,diameter+1,2):
        print((my_str*i).center(diameter))
    for j in range(diameter-2,0,-2):
        print((my_str*j).center(diameter))
        
number_of_star = int(input('enter number : '))
diamond(number_of_star)


#======================================================== solution 2
print(30*'--')

def diamond(diameter):
    if diameter % 2 == 0 :
        diameter +=1
    my_str = '*'
    for i in range(diameter):
        if i < diameter / 2:
            print((my_str*(i*2 + 1)).center(diameter))
        else:
            print((my_str*((diameter-i)*2 -1)).center(diameter))
        
number_of_star = int(input('enter number : '))
diamond(number_of_star)


#======================================================== solution 3
print(30*'--')


def print_star_line(number_of_stars,total_stars):
    number_of_space = (total_stars - number_of_stars) // 2
    print(' ' * number_of_space,end='')
    print('*' * number_of_stars,end='')
    print(' ' * number_of_space)


def draw_diamond(num):
    print()
    number_of_stars = None
    for i in range(num):
        if i < num / 2:
            number_of_stars = i * 2 + 1
        else:
            number_of_stars = (num - i) * 2 - 1
        print_star_line(number_of_stars, num)

number_of_stars = int(input('enter number : '))
draw_diamond(number_of_stars)