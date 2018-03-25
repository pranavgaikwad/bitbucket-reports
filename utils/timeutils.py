import time
import datetime
from pytz import timezone
from dateutil.parser import parse

class TimeUtils:
    def __init__(self):
        pass

    def now(self):
        ''' current time '''
        return datetime.datetime.now(timezone('UTC'))

    def future(self, by):
        ''' future time by days '''
        pass

    def past(self, days):
        ''' past time by days '''
        return self.now() + datetime.timedelta(days*-1)

    def from_string(self, tm):
        ''' convert string to datetime '''
        return parse(tm)

    def to_string(self, tm):
        ''' converts datetime to string '''
        return tm.strftime("%Y-%m-%dT%s%z")