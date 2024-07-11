def is_even(number):
    if number% 2 == 0:
        return True
    
    return False

def return_all_even_number_of_list(num_list):
    result = []
    for num in num_list:
        if is_even(num):
            result.append(num)
    return(result)



print(return_all_even_number_of_list([111,2,3,3,67,6,8,54,99,2]))
