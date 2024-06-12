secret_string = '84,113,120,120,123,58'

text_list = secret_string.split(',')
print(text_list)

text = []
for num in text_list:
    text.append(chr(int(num)-12))

text_orginal = ''.join(text)

print(text_orginal)


#============================================= 2

secret_string = '84,113,120,120,123,58'

string_list = []

for num_str in secret_string.split(','):
    string_list.append(chr(int(num_str)-12))

print(''.join(string_list))
