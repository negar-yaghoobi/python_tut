i = 0 
while i < 10 :
    #print(i)
    if i == 5:
        i +=1
        continue
    print(i)
    i +=1
    
print('end')

print('---------------------------')

j = 0
for j in [1,3,4,5,6,80]:
    if j == 5:
        continue
    print(j)
print('end')