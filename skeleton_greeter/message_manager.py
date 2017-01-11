
GREETING_MSG = 'hello world from flask'

class messageManager(object):

    def __init__(self, name, clock):
        self.name = name
        self.clock = clock

    def message(self):
        if 14 <= self.clock.get_time() <= 16:
            return 'zzz'
        if self.name:
            return GREETING_MSG + ' ' + self.name
        else:
            return '%s' % GREETING_MSG