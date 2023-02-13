import random


class Insect:
    def __init__(self):
        self.name = ""
        self.wings = '2'
        self.legs = '4'
        self.flight = '0'

    def flight_length(self):
        self.flight = random.randrange(1, 10)

    def get_miles(self):
        return self.flight

    def get_name(self):
        return self.name
