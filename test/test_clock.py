from skeleton_greeter.greeter import clock


class TestClock:

    def test_clock_testing_mode(self):
        assert 14 <= clock('TESTING').get_time() <= 16