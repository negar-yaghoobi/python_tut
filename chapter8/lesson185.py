# method resolution

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
    def __init__(self, name, family, uni, department = 'pp'):       # default value for department
        super().__init__(name, family)
        self.dept = department                         # create new attribute in subclass(student)
        self.uni = uni
    
    def working_info(self):
        return f'i am working in {self.uni} university at {self.dept} department'

class Sample(Teacher):
    pass


help(Sample) 