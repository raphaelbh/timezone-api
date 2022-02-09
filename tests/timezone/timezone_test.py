import unittest
import datetime
from app.services import timezone_service

class TimezoneTest(unittest.TestCase):

    def test_timezones_is_not_none(self):
        assert len(timezone_service.timezones()) > 0, "Should be a list with values"

    def test_convert_datetime_with_no_timezone_informed(self):
        current_datetime = datetime.datetime(2011, 11, 4, 13, 5, 23, 283000, tzinfo=datetime.timezone.utc)
        actual = timezone_service.convert_datetime(current_datetime, None)
        expected = { 'UTC': '2021-11-04 13:05:23 UTC+0000' }
        assert all([a == b for a, b in zip(actual, expected)])

    def test_convert_datetime_correct_timezone_informed(self):
        current_datetime = datetime.datetime(2011, 11, 4, 13, 5, 23, 283000, tzinfo=datetime.timezone.utc)
        actual = timezone_service.convert_datetime(current_datetime, 'America/Sao_Paulo') 
        expected = { 'UTC':'2021-11-04 13:05:23 UTC+0000', 'America/Sao_Paulo':'2021-11-04 10:05:23 -03-0300' }
        assert all([a == b for a, b in zip(actual, expected)])

    def test_convert_datetime_invalid_timezone_informed(self):
        current_datetime = datetime.datetime(2011, 11, 4, 13, 5, 23, 283000, tzinfo=datetime.timezone.utc)
        with self.assertRaises(Exception):
            timezone_service.convert_datetime(current_datetime, 'America/Sao_P')

if __name__ == '__main__':
    unittest.main()