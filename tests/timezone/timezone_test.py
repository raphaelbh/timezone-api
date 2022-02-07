import unittest
from app.timezone import timezone

class TimezoneTest(unittest.TestCase):

    def test_timezones_is_not_none(self):
        assert len(timezone.timezones()) > 0, "Should be a list with values"

    def test_now_is_not_none(self):
        assert timezone.now() != None, "Should have the current date"

if __name__ == '__main__':
    unittest.main()