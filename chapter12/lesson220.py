print('start...')
try:
    print('first...')
    import mymodule

    print(2/0)

    nums = [12, 4, 'hello']
    print(nums[10])

except ModuleNotFoundError:
    print('ModuleNotFoundError')
except ZeroDivisionError:
    print('ZeroDivisionError')

print('end...')