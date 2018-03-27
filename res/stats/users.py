from stats import UserStats
from utils.cache import UserStatCache

class Users:
    """ User Statistics """
    def __init__(self):
        '''  '''
        self.users = {}
        self._load_from_cache()

    def update(self, user, key, value=None):
        ''' updates user stat, creates if doesn't exist '''
        try:
            stat = self.users[user]
        except:
            self.users[user] = UserStats()
        
        self.users[user].add(key, value)

    def _load_from_cache(self):
        ''' loads users from cache '''
        cache = UserStatCache().load()
        if cache is not None:
            self.users = cache

    def _update_cache(self):
        ''' updates cache with new dict '''
        UserStatCache().save(self.users)