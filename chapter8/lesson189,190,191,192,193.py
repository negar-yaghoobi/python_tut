#======================================================================================= solution 1

class Time:
    def __init__(self, hour, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hour = hour
        self.check_hour()
        self.check_minutes()
        self.check_seconds()

    def check_hour(self):
        if isinstance(self.hour, int):          # check integer nubmer
            if self.hour > 24:
                self.hour = 23
            elif self.hour < 0:
                self.hour = 0
        else:
            self.hour = 0

    def check_minutes(self):
        if isinstance(self.minutes, int):          # check integer nubmer
            if self.minutes > 60:
                self.minutes = 59
            elif self.minutes < 0:
                self.minutes = 0
        else:
            self.minutes = 0

    def check_seconds(self):
        if isinstance(self.seconds, int):        # check integer nubmer
            if self.seconds > 60:
                self.seconds = 59
            elif self.seconds < 0:
                self.seconds = 0
        else:
            self.seconds = 0
    
    def int_to_str(self, in_):
        if in_ < 10:
            in_ = '0' + str(in_)
        else:
            in_ = str(in_)

        return in_

    def __str__(self):
        return f'{self.int_to_str(in_=self.hour)}:{self.int_to_str(in_=self.minutes)}:{self.int_to_str(in_=self.seconds)}'


clock = Time(110, 66, -10 )

print(clock.hour)
print(clock.minutes)
print(clock.seconds)

print(clock)

#======================================================================================= solution 2

class Time:
    def __init__(self, hour, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hour = hour
        self.check_hour()
        self.check_minutes()
        self.check_seconds()

    def check_hour(self):
        if isinstance(self.hour, int):
            if self.hour >= 24 | self.hour < 0 :
                raise ValueError('hours number should be between 0 and 24 .')
        else:
            raise ValueError('input is not number')

    def check_minutes(self):
        if isinstance(self.minutes, int):
            if self.minutes >= 60 | self.minutes < 0:
                raise ValueError('minutes number should be between 0 and 60. ')
        else:
            raise ValueError('input is not number')

    def check_seconds(self):
        if isinstance(self.seconds, int):
            if self.seconds >= 60 | self.seconds < 0:
                raise ValueError('seconds number should be between 0 and 60. ')
        else:
            raise ValueError('input is not number')
    
    def int_to_str(self, in_):        # use 0 before number 0 .. 9
        if in_ < 10:
            in_ = '0' + str(in_)
        else:
            in_ = str(in_)

        return in_

    def __str__(self):
        return f'{self.int_to_str(in_=self.hour)}:{self.int_to_str(in_=self.minutes)}:{self.int_to_str(in_=self.seconds)}'


clock = Time(20, 6, 10 )

print(clock.hour)
print(clock.minutes)
print(clock.seconds)

print(clock)

#============================================================================================= solution 3
class Time:
    def __init__(self, hour, minutes, seconds):
        if hour >= 24:
            raise ValueError('hours number should be less than 24')
        if minutes >= 60:
            raise ValueError('minutes number should be less than 60')
        if seconds >= 60:
            raise ValueError('seconds number should be less than 60')

        self.seconds = seconds
        self.minutes = minutes
        self.hour = hour

    def __str__(self):
        return f'{self.hour:02}:{self.minutes:02}:{self.seconds:02}'

    def __add__(self, other):                              # use for Adding the two objects        ~ # operator overloading with __add__
        if isinstance(other, Time):                        # check that two objects are in same class 

            seconds = self.seconds + other.seconds
            minutes = self.minutes + other.minutes + (seconds // 60)
            hour = self.hour + other.hour + (minutes // 60)
            new_time = Time(hour % 24, minutes % 60, seconds % 60)        # create new object of class time that return  (*)
            return new_time
        
        return NotImplemented
    
    # operator loading ==
    def __eq__(self, other):              
        return (self.hour == other.hour) \
            and (self.minutes == other.minutes) \
            and (self.seconds == other.seconds)
    
    # operator loading >
    def __gt__(self, other):              
        return (self.hour > other.hour) \
                or (self.hour == other.hour and self.minutes > other.minutes) \
                or (self.hour == other.hour and self.minutes == other.minutes and self.seconds > other.seconds)
            

# =================================================== part 1 

clock = Time(10, 6, 0 )
print(clock.hour)
print(clock.minutes)
print(clock.seconds)

print(clock)


#========================================================= part 2      # operator overloading

obj1 = Time(22, 55, 49)
obj2 = Time(22, 55, 49)

# Adding the two objects
result = obj1 + obj2
print(result)                     # result is new object of class time that create in return of __add__ method (*)

# part 3 

print(obj1 == obj2)               # use __eq__ in class for this operator

print(obj1 > obj2)                # use __gt__ in class for this operator



#============================================= dir ()
print(dir(obj1))