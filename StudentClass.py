from datetime import date


class Student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__registration = ''

    def calc_age(self):
        today = date.today()
        today_year = today.year
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = today_year - dob_year

    def registration(self):
        if self.__classification == 'senior':
            self.__registration = '4/1 thru 4/3'
        elif self.__classification == 'junior':
            self.__registration = '4/4 thru 4/6'
        elif self.__classification == 'sophmore':
            self.__registration = '4/7 thru 4/9'
        elif self.__classification == 'freshman':
            self.__registration = '4/10 thru 4/12'
        else:
            self.__registration = 'classification not found'

    def get_age(self):
        return self.__age

    def get_registration(self):
        return self.__registration
