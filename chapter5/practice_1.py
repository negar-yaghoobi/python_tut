number = int(input('enter number : '))

for i in range(2,number):
    if number % i == 0:
        print(f'{number} is not prime.')
        print(f'{number} % {i}')
        break
    else:
        if i < number-1:
            continue
        else:
            print(f'{number} is prime.')


#===================================================== another solution

number = int(input('enter number : '))

is_prime = True
for i in range(2,number):
    if number % i == 0:
        is_prime = False
        print(f'{number} % {i}')
        break

if is_prime == True:
    print(f'{number} is prime.')
else:
    print(f'{number} is not prime.')