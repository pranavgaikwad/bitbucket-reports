import re
import json
from stats.users import Users
from gitclient import GitClient
from stats.stats import UserStats
from utils.timeutils import TimeUtils
from utils.requestutils import BitbucketRequests

class Commits(GitClient):
    def __init__(self, repo):
        super(Commits, self).__init__(repo)
        self.users = Users()

    def commits(self, days="2018-03-12", branches=None):
        since = TimeUtils().past(days=20) # TimeUtils().from_string(since)
        if branches is None:
            branches = self.repo.branches
        for branch in branches:
            i = 1   # skip 
            print branch.name
            commit = self._get_one(branch=branch.name)
            while (commit is not None) and (commit.committed_datetime > since):
                # print str(branch.name) + str(commit.author) + " : " + str(commit.message)
                self.users.update(user=str(commit.author),key=UserStats.KEY_COMMITS)
                commit = self._get_one(branch=branch.name, skip=i)
                i = i + 1
        return self

    def _get_one(self, branch, skip=0):
        ''' returns single commit using skip '''
        commits = list(self.repo.iter_commits(branch, max_count=1, skip=skip))
        if commits:
            return commits[0]
        return None
