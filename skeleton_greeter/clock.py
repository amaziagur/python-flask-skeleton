import datetime
from random import randint


class clock(object):
    def __init__(self, mode=None):
        self.mode = mode

    def get_time(self):
        if self.mode :
            return randint(14,16)
        else:
            now = datetime.datetime.now()
        return now.hour