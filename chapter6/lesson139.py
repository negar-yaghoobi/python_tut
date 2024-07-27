def max_min_sum_len(*args):
    list_number = list(args)
    return f'min:{min(list_number)}, max:{max(list_number)}, sum:{sum(list_number)}, length:{len(list_number)}'
    
print(max_min_sum_len(10, 11, 12, 13, 14, 15, 32, 0, 1, 2, 90))
    
