user_name = input('enter your username : ')
password = input('enter your password : ')
if user_name == password:
    print('the two values should not be equal.')
elif len(password) < 8:
    print('the length of the password must be at least 8 characters.')
elif len(password) > 20 :
    print('the length of the password must be at most 20 characters.')
elif len(user_name) < 4 :
    print('the length of the username must be at least 4 characters.')
else:
    print('the entries are correct and username and password has been saved.')