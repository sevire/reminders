from datetime import datetime
from unittest import TestCase

from ddt import ddt, data, unpack

from alertwrap import AlertWrap
from database import Alert


def parse_datetime(datetime_string):
    datetime_value = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S.%f')
    return datetime_value


test_alert_data = [
    ('Test Message 1', parse_datetime("2021-05-21 12:00:00.0"))
]


def alert_generator():
    for entry in test_alert_data:
        yield entry, 'message', entry[0]
        yield entry, 'issue_time', entry[1]


@ddt
class TestAlert(TestCase):

    @data(*alert_generator())
    @unpack
    def test_alert(self, parameters, test_field_name, test_field_value):
        """
        Tests that when an alert is created as a model item, the values supplied are correctly returned by the class.

        It feels like this test isn't really testing anything as I put a value in and get the same value out.  But
        I feel that I need to check that by putting into a model and maybe a database and then reading out again
        there isn't anything weird that happens to the value.

        :return:
        """
        message, issue_time = parameters
        model_alert = Alert(message=message, issue_time=issue_time)
        alert = AlertWrap(model_alert)

        value = getattr(alert, test_field_name)

        self.assertEqual(test_field_value, value)

