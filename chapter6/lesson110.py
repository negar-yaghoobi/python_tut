def check_any_even_in_list(my_list):
    for num in my_list:
        if num % 2 == 0:
            return 'There is at least one even number in the list'
    
    return 'There are no even numbers in the list'

            


print(check_any_even_in_list([11,229,3,45,5,611]))



#---------------------------------------------------------------------------
print(30*'-')

def split_even_in_list(list_of_number):
    list_of_even_number = []
    for num in list_of_number:
        if num % 2 == 0:
            list_of_even_number.append(num)
    return list_of_even_number

print(f'list_of_even_number is {split_even_in_list([1,2,3,4,511,90])}')

