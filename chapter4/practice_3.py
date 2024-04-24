price = int(input('enter the price:'))

if price >= 0:
    if price > 1000:
        print('too expensive')
    elif price > 500 and price <= 1000:
        print('expensive')
    elif price > 100 and price <= 500:
        print('normal')
    else:
        print('inexpensive')
else:
    print('the price cannot be negative')