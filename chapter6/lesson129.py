#======================================== ~lambda

list_of_scores = [1, 2, 20, 15, 7, 3, 4, 5, 17]

def is_more_than_10(score): return score >= 10

print(list(filter(is_more_than_10, list_of_scores)))


print(30 * '--')
#======================================== lambda

list_of_scores = [1, 2, 20, 15, 7, 3, 4, 5, 17]

x = lambda score: score >= 10

print(list(filter(x, list_of_scores)))


print(30 * '--')
#======================================== lambda

list_of_scores = [1, 2, 20, 15, 7, 3, 4, 5, 17]


print(list(filter(lambda score: score >= 10, list_of_scores)))



print(30 * '--')
#======================================== lambda

list_of_scores = [1, 2, 20, 15, 7, 3, 4, 5, 17]

print(list(map(lambda num: num + 1, list_of_scores )))




print(30 * '--')
#======================================== lambda

list_of_numbers = [1, 2, 20, 15]

for i in map(lambda num: 'a'*num, list_of_numbers):
    print(i)