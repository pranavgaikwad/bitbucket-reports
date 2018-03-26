class Stats(object):
    """ All statistics """

    def __init__(self):
        self.stats = {}

    def add(self, key, value):
        self.stats[key] = value

    def get(self, key):
        stat = None
        try:
            stat = self.stats[key]
        except:
            pass
        return stat

class UserStats(Stats):
    """ User specific stats """

    KEY_COMMITS = "commits"

    def __init__(self):
        super(UserStats, self).__init__()
        self._default()

    def _default(self):
        ''' fills stats object with default values '''
        self.stats[self.KEY_COMMITS] = 0

    def add(self, key, value):
        if key == self.KEY_COMMITS:
            self._add_commit()
            
    def _add_commit(self):
        super(UserStats, self).add(self.KEY_COMMITS, self.get(self.KEY_COMMITS) + 1)