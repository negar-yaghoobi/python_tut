#============================================ else in try-except
a = 1
b = int(input('enter a number: '))

try:   # try to run this code
    print(a/b)
except ZeroDivisionError:    # if this exception happended
    print('EXCEPTION')
except ModuleNotFoundError:       #  if this exception happended
    print('another exception')
except Exception:
    print('some other error')
else:       # if there is no error
    print('ELSE')

print('END...')

# ================================================ finally in try_axcept

a = 1
b = int(input('enter a number: '))

try:   # try to run this code
    print(a/b)
except ZeroDivisionError:    # if this exception happended
    print('EXCEPTION')
except ModuleNotFoundError:       #  if this exception happended
    print('another exception')
else:       # if there is no error
    print('ELSE')
finally:
    print('FINALLY')

print('END...')