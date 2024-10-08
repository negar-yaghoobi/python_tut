#================================================= solution 1
file_text = ''
with open('file_1.txt', 'r') as reader:
    file_text = reader.read()

with open('file_2.txt', 'w') as writer:
    writer.write(file_text)


#================================================= solution 2

with open('file_1.txt', 'r') as reader, open('file_2.txt', 'w') as writer:
    writer.write(reader.read())