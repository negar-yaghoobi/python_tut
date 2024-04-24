my_list = [11, 98, 34, -8777, -4, 665, 110, 89, 900]
my_list.sort()
#print(my_list)

middle = (my_list[0] + my_list[-1]) /2
#print(middle)

length = len(my_list)
#print(length)
middle_list = length//2
if length % 2 != 0 :
    avr = my_list[middle_list]
else:
    avr = (my_list[middle_list-1] + my_list[middle_list])//2

#print(avr)

if avr > middle:
    print('the avrage is bigger than the middle')
elif avr < middle:
    print('the avrage is smaller than the middle')
else:
    print('the avrage is equal to the middle')