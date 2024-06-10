# for i in range(3):
#     print('i loop starts')
#     for j in range(4):
#         print('j loop starts')
#         print(i,j)

print('-------------------------')

nested_list = [[1,2,3],[-1,-2,-3],[-5,30,-40]]

for i in nested_list:
    for j in i :
        print(j)