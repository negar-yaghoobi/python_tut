import lesson198_2
def show_message():
    print('this is show_message function.')

lesson198_2.function1()

lesson198_2.function3()

obj1 = lesson198_2.My_class(10)

print(obj1)
print(lesson198_2.my_number)

#=========================================

class Car:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'this is car object {self.a}'

