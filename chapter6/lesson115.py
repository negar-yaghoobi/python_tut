# ------------------------------------------   مقداردهی ترتیبی

def my_func(language, eye_color, age):
    print('my language is {}'.format(language))
    print('my eye_color is {}'.format(eye_color))
    print('my age is {}'.format(age))


my_func('farsi', 'blue', 100)


print(30 * '--')
# ------------------------------------------ named argument

def my_func(language, eye_color, age):
    print('my language is {}'.format(language))
    print('my eye_color is {}'.format(eye_color))
    print('my age is {}'.format(age))


my_func(age=100, language='farsi', eye_color= 'blue')


print(30 * '--')
# ------------------------------------------ مقداردهی ترکیبی

def my_func(language, eye_color, age):
    print('my language is {}'.format(language))
    print('my eye_color is {}'.format(eye_color))
    print('my age is {}'.format(age))


my_func('farsi', age=100, eye_color= 'blue')