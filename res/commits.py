import re
import json
from utils.timeutils import TimeUtils
from utils.request import BitbucketRequests

class Commits:

    URL = ""

    def __init__(self, username, password):
        self.reqs = BitbucketRequests(username, password)

    def all(self, pagelen=5, page=1):
        ''' returns all commits '''
        url = self.URL + "?page=" + str(page)
        url = url + "&pagelen=" + str(pagelen)
        return self.reqs.get(url).text

