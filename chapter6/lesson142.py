def find_largest_string(*args):
    max_length = len(args[0])
    largest_string = args[0]

    for i in args:
        if len(i) > max_length:
            max_length = len(i)
            largest_string = i

    return largest_string, max_length


print(find_largest_string('ajtc', 'aa', 'aaajn.k,hgk', 'zz', 'xxx', 'q', 'wert'))


#+============================================================
print(30*'--')

def find_largest_string(*args):
    largest_string = args[0]

    for i in args:
        if len(i) > len(largest_string):
            largest_string = i

    return largest_string, len(largest_string)


print(find_largest_string('ajtc', 'aa', 'aaajn.k,hgk', 'zz', 'xxx', 'q', 'wert'))