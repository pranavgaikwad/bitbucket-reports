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
        to_date   = TimeUtils().now()
        from_date = TimeUtils().past(days=20)

        # cache_from_date = self.users['from']
        # cache_to_date   = self.users['to']

        self._count_commit(branches=branches, from_date=from_date, to_date=to_date)
        
        # self.users.users['from'] = str(from_date)
        # self.users.users['to'] = str(to_date)

        # self.users._update_cache()
        
        return self

    def _count_commit(self, branches, from_date, to_date):
        ''' counts commit if is in defined time range '''
        self._load_heads()

        counted_commits = []

        if branches is None:
            branches = self.repo.branches
        
        for branch in branches:
            i = 1   # skip 
            commit = self._get_one(branch=branch.name)
            while (commit is not None) and (commit.committed_datetime > from_date) and (commit.committed_datetime <= to_date):
                if commit.hexsha not in counted_commits:
                    counted_commits.append(commit.hexsha)
                    self.users.update(user=str(commit.author),key=UserStats.KEY_COMMITS)
                commit = self._get_one(branch=branch.name, skip=i)
                i = i + 1

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