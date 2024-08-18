# inheritance

class Student:
    def __init__(self, name, family, major, uni):
        self.name = name
        self.family = family
        self.major = major
        self.university = uni

    def who_am_i(self):
        return f'name : {self.name} family : {self.family}'


class Teacher:
    def __init__(self, name, family, department, uni):
        self.name = name
        self.family = family
        self.department = department
        self.university = uni

    def who_am_i(self):
        return f'name : {self.name} family : {self.family} . i am a teacher at {self.university} university.'


sara_stu = Student('sara','xxx','qqq', 'www')
david_stu = Student('david', 'yyy','eee', 'rrr')

john = Teacher('john','doe', 'math', 'mit')
print(john.who_am_i())

print(sara_stu.who_am_i())
print(david_stu.who_am_i())

#=========================================================================== # inheritance
print(30* '--')

class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def full_name(self):
        return self.name.title() + ' ' + self.family.title()

class Student(Person):           # inheritance
    pass

ali_stu = Student('ali','ccc')
print(ali_stu.full_name())

#=========================================================================== # inheritance  create new attribute
print(30* '--')

class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def full_name(self):
        return self.name.title() + ' ' + self.family.title()

class Student(Person):           # inheritance
    def __init__(self, name, family, major):
        Person.__init__(self, name, family)          # call attribute that there are in Superclass(person)
        self.major = major                           # create new attribute in subclass(student)
        

ali_stu = Student('ali','ccc','gfc')
print(ali_stu.full_name())


#=========================================================================== # inheritance create new attribute with super()
print(30* '--')

class Person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

    def full_name(self):
        return self.name.title() + ' ' + self.family.title()

class Student(Person):           # inheritance

    def __init__(self, name, family, major, university):
        super().__init__(name, family)          # call attribute that there are in Superclass(person) with method super()
        self.major = major                           # create new attribute in subclass(student)
        self.university = university

    def full_name(self):
        return f'{self.name} {self.family}. i am studying in {self.major}.'

    def return_university(self):
        return f'i am studying in {self.university}. '
    
class Teacher(Person):
    def __init__(self, name, family, uni, department):
        super().__init__(name, family)
        self.dept = department                         # create new attribute in subclass(student)
        self.uni = uni
    
    def working_info(self):
        return f'i am working in {self.uni} university at {self.dept} department'

    

ali_stu = Student('ali', 'ccc', 'gvujy', 'zzz')
print(ali_stu.full_name())
print(ali_stu.return_university())

print(30* '--')

david = Teacher('david', 'xx', 'zxc', 'qqq')
print(david.full_name())
print(david.working_info())