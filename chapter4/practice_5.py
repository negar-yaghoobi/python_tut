my_list = [11, 23, 45, 677, 83, 90, 110, 514]
length = len(my_list)
print(length)
middle = length//2
if length % 2 != 0 :
    print(my_list[middle])
else:
    print((my_list[middle-1] + my_list[middle])//2)
    