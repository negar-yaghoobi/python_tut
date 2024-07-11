# Returns the longest string in a list

def longest_string(list_of_string):
    length = 0
    for str in list_of_string:
        if len(str) >= length:
            length = len(str)
            long_str = str

    return long_str,length

print(longest_string(['as','edfc','wegfvqw','a']))



print(30 * '--')
#---------------------------------------------------------- return the name of most mark 

def max_mark(list_of_marks):
    highest_mark = 0
    for name, mark in list_of_marks:
        if mark >= highest_mark:
            highest_mark = mark
            result_name = name
            
    return result_name, highest_mark


list_of_marks = [('ana', 18), ('arvin', 19), ('sara', 11)]

name,mark = max_mark(list_of_marks)
print(name, mark)





