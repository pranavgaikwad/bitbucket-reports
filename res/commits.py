import re
import json
from git import Repo
from utils.timeutils import TimeUtils
from utils.requestutils import BitbucketRequests

class Commits:

    def __init__(self, repo):
        self.repo = Repo(repo)

    def commits(self, since=""):
        i = 1   # skip
        since = TimeUtils().past(days=20)
        commit = self._get_one()
        while (commit is not None) and (commit.committed_datetime > since):
            print str(commit.author) + " : " + str(commit.message)
            commit = self._get_one(skip=i)
            i = i + 1

    def _get_one(self, skip=0):
        ''' returns single commit using skip '''
        commits = list(self.repo.iter_commits(max_count=1, skip=skip))
        if commits:
            return commits[0]
        return None

    def _info(self, commit):
        ''' returns a dictionary filled with information about particular commit '''
        info = {}
        pass
