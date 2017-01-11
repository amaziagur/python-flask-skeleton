from skeleton_greeter.clock import clock
from skeleton_greeter.message_manager import messageManager

MESSAGE_CONTENT = 'hello world from flask'

class TestMessageManager:

    def test_general_greeting(self):
        assert messageManager(None, clock()).message() == MESSAGE_CONTENT

    def test_personal_greeting(self):
        assert messageManager('crazylabz', clock()).message() == MESSAGE_CONTENT + ' crazylabz'

    def test_zzz_greeting_at_noon_time(self):
        assert messageManager('crazylabz', clock('TESTING')).message() == 'zzz'