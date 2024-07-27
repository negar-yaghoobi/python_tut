def add_rec(a):
    if a < 3:
        return add_rec(a+1)
    return a

print(add_rec(1))



#===================================================== factorial function that use recursive function
print(30*'--')

def factorial(number):
    if number ==1:
        return 1
    return factorial(number - 1) * number

print(factorial(4))