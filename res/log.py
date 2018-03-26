import re
from stats.users import Users
from gitclient import GitClient
from stats.stats import UserStats

class Log(GitClient):

    PATTERN_AUTHOR = r'Author: (.*) <(.*)>(.*)'

    def __init__(self, repo):
        super(Log, self).__init__(repo)
        self.users = Users()

    def log(self):
        for branch in self.repo.branches:
            self.repo.git.checkout(branch.name)
            log = str(self.repo.git.log())
            lines = log.split('\n')
            i = 1
            for line in lines:
                i = i + 1
                authors = re.search(self.PATTERN_AUTHOR, line)
                if authors is not None:
                    author_name = authors.group(1)
                    author_email = authors.group(2)
                    self.users.update(user=str(author_name), key=UserStats.KEY_COMMITS)
        return self

    def heads(self):
        ''' heads '''
        all_refs = self.repo.remotes.origin.refs
        for ref in all_refs:
            self.repo.create_head(ref.name, ref)

        return self.repo.branches