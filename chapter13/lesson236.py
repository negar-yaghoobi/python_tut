f = open('names_6.txt', 'w')

# f.writelines(['str1', 'str2'])

# add \n after names of list in file name_6.txt

names = ['john', 'joe', 'david']

f.writelines(map(lambda name: name+'\n', names))               # the first way

f.write('\n'.join(names))                                      # the second way
