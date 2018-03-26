import re
from itertools import izip
from stats.users import Users
from gitclient import GitClient
from stats.stats import UserStats

class Log(GitClient):

    PATTERN_AUTHOR = r'Author: (.*) <(.*)>(.*)\n'
    PATTERN_COMMIT = r'(.*)'

    def __init__(self, repo):
        super(Log, self).__init__(repo)
        self.users = Users()

    def log(self):
        self._load_heads()
        counted_commits = []
        for branch in self.repo.branches:
            print "Counting commits on : " + branch.name
            self.repo.git.checkout(branch.name)
            log = str(self.repo.git.log())
            lines = log.split('commit ')
            i = 1
            for line in lines:
                i = i + 1
                author = re.search(self.PATTERN_AUTHOR, line)
                commit = re.search(self.PATTERN_COMMIT, line.split('\n')[0])
                print author.group(1)
                print commit.group(1)
                break
                # if author is not None and commit is not None:
                #     author_name  = author.group(1)
                #     author_email = author.group(2)
                #     commit_hash  = commit.group(1)
                #     if commit_hash not in counted_commits: 
                #         self.users.update(user=str(author_name), key=UserStats.KEY_COMMITS)
                #         counted_commits.append(commit_hash)
        return self