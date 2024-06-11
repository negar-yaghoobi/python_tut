text = list(input('enter string: '))
print(text)

list_save =[]
for char in text:
    list_save.append(str(ord(char) + 12))

print(','.join(list_save))


#=========================================