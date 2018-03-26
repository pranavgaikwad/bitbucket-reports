import re
import json
from stats.users import Users
from gitclient import GitClient
from stats.stats import UserStats
from utils.timeutils import TimeUtils
from utils.requestutils import BitbucketRequests

class Commits(GitClient):
    """ all operations on commits """

    def __init__(self, repo):
        super(Commits, self).__init__(repo)
        self.users = Users()

    def commits(self, days="2018-03-12", branches=None):
        ''' returns commits since specified days on given branches '''
        ''' uses all branches if branches not specified '''
        since = TimeUtils().past(days=120)
        self._load_heads()
        counted_commits = []
        if branches is None:
            branches = self.repo.branches
        for branch in branches:
            i = 1   # skip 
            commit = self._get_one(branch=branch.name)
            while (commit is not None) and (commit.committed_datetime > since):
                if commit.hexsha not in counted_commits:
                    counted_commits.append(commit.hexsha)
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

    def _load_heads(self):
        ''' load all remote heads '''
        all_refs = self.repo.remotes.origin.refs
        for ref in all_refs:
            self.repo.create_head(ref.name, ref)
        return self.repo.branches