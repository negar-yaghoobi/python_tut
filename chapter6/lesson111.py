#-------------------------------------------------------- tuple unpacking

marks = [('ana',18), ('arvin',19), ('sara',20)]

for name, mark in marks:
    print(name, mark)



print(30 *'--')
#-------------------------------------------------------- tuple unpacking and return in function

def calc_sum_sub(num1, num2):
    sum_result = num1 + num2
    sub_result = num1 - num2
    return (sum_result, sub_result)   # return tuple


print(calc_sum_sub(10,4))


#-------------------------------------------------
print(30 *'--')


def calc_sum_sub(num1, num2):
    sum_result = num1 + num2
    sub_result = num1 - num2
    return (sum_result, sub_result)  # ~ return sum_result, sub_result


result = calc_sum_sub(10,4)
print(result[0])
print(result[1])

#------------------------------------------------- tuple unpaching in function
print(30 *'--')

def calc_sum_sub(num1, num2):
    sum_result = num1 + num2
    sub_result = num1 - num2
    return (sum_result, sub_result)


(a,b) = calc_sum_sub(10,4)    # tuple unpaching
print(a, b)


#------------------------------------------------- # calcute min and max numbers in list
print(30 *'--')

def calc_max_min(list_of_numbers):
    max_of_number = max(list_of_numbers)
    min_of_number = min(list_of_numbers)
    return (max_of_number, min_of_number)


(max_list, min_list) = calc_max_min([1,2,2,34,64,7])
print(f'max is : {a} , min is : {b}')