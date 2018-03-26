from stats import UserStats

class Users:
    """ User Statistics """
    def __init__(self):
        '''  '''
        self.users = {}

    def update(self, user, key, value=None):
        ''' updates user stat, creates if doesn't exist '''
        try:
            stat = self.users[user]
        except:
            self.users[user] = UserStats()
        
        self.users[user].add(key, value)