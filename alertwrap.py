from datetime import datetime


class AlertWrap:
    def __init__(self, model_alert):
        """
        Wraps an Alert object from the database to allow processing.

        :param model_alert:
        """
        self.alert = model_alert

    @property
    def message(self):
        return self.alert.message

    @property
    def issue_time(self):
        return self.alert.issue_time

    def is_due(self, current_time=None):
        """
        Works out whether alert is due.

        The current time can be passed in to allow testing with selected values.  If not then use now()

        :param current_time:
        :return:
        """
        if current_time is None:
            current_time = datetime.now()
        if self.issue_time >= current_time:
            return True
        else:
            return False
