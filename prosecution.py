a = 3
b = 2

c = a + b

# if/else conditional 
if(c >= 8):
    print('mayor 8')
elif(c >= 5):
    print('mayor a 5 y menor a 8') 
else:
    print('manor a 5')    


# switch/case

# Dictionary Mapping

Sunday = 'Sunday'
Monday = 'Monday'
Tuesday = 'Tuesday'
Wednesday = 'Wednesday'
Thursday = 'Thursday'
Friday = 'Friday'
Saturday = 'Saturday'
IncorrectDay = 'Incorrect day'


def sunday():
    return Sunday

def monday():
    return Monday

def tuesday():
    return Tuesday

def wednesday():
    return Wednesday

def thursday():
    return Thursday

def friday():
    return Friday

def saturday():
    return Saturday

def default():
    return IncorrectDay

switcher = {
    1: sunday,
    2: monday,
    3: tuesday,
    4: wednesday,
    5: thursday,
    6: friday,
    7: saturday,
}    

def switch(dayOfWeek:int):
    return switcher.get(dayOfWeek, default)()

# Using classes
class PythonSwitch:
    def day(self, dayOfWeek):
        default = IncorrectDay
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return Sunday

    def case_2(self):
        return Monday

    def case_3(self):
        return Tuesday

    def case_4(self):
        return Wednesday

    def case_5(self):
       return Thursday

    def case_6(self):
        return Friday

    def case_7(self):
        return Saturday

my_switch = PythonSwitch()
day = 1
print('Dictionary Mapping:',switch(day))
print ('Using classes:',my_switch.day(day))