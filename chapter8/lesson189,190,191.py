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
        if isinstance(self.hour, int):
            if self.hour > 24:
                self.hour = 23
            elif self.hour < 0:
                self.hour = 0
        else:
            self.hour = 0

    def check_minutes(self):
        if isinstance(self.minutes, int):
            if self.minutes > 60:
                self.minutes = 59
            elif self.minutes < 0:
                self.minutes = 0
        else:
            self.minutes = 0

    def check_seconds(self):
        if isinstance(self.seconds, int):
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

