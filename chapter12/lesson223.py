try:
    print(2/0)
except ZeroDivisionError as e:
    print('Exception', e)

#===============================================
try:
    print(2/0)
except Exception as e:
    print('Exception', e)