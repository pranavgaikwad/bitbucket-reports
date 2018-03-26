from git import Git
from git import Repo

class GitClient(object):

    def __init__(self, repo):
        self.git = Git()
        self.repo = Repo(repo)