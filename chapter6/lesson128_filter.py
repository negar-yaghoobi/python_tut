#======================================== filter

list_of_scores = [1, 5, 7, 9, 12, 15, 17, 13, 12, 19]

def is_more_than_15(score):
    if (score >=15):
        return True
    return False

print(list(filter(is_more_than_15, list_of_scores)))



print(30 * '--')
#======================================== filter

names = ['ali alavi', 'ana jons', 'baran bara', 'sara', 'reza']

def full_name(name):
    if len(name.split()) > 1:
        return True
    return False

print(list(filter(full_name, names)))



print(30 * '--')
#======================================== filter

names = ['ali', 'ana', 'baran', 'sara', 'reza']
def length(name):
    if len(name) > 3:
        return True
    return False

print(list(filter(length,names)))