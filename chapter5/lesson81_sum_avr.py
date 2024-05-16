numbers = [112,23,45,64,78,97,80]
sum_num = 0
count = 0
for num in numbers:
    count = count + 1   # = len(numbers)
    sum_num = num + sum_num    # = sum(numbers)
average = sum_num / count     # = sum(numbers) / len(numbers)
print(f'sum of numbers is {sum_num}.')
print(f'average of numbers is {average}')