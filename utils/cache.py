import os 
import pickle

class Cache(object):
    """ generic object cache """

    def __init__(self, cache):
        self.cache = cache
        if os.path.exists(cache):
            try:
                self.load()
            except IOError:
                self._new()
        else:
            self._new()

    def _new(self):
        ''' creates new cache file '''
        self.save({})

    def load(self):
        ''' loads cache into dict '''
        try:
            with open(self.cache, 'rb') as handle:
                unserialized_data = pickle.load(handle)
            return unserialized_data
        except:
            raise IOError("Corrupted cache.")

    def save(self, d):
        os.remove(self.cache)
        try:
            with open(self.cache, 'wb') as handle:
                pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)
            return
        except:
            raise IOError("Corrupted cache.")

'''
Cache entry would look like this\ 
:

'repo' : {
            user : <>
            from : <>
            to : <>
            commits : <>
         }, 
         {
            user : <>, 
            from : <>, 
            to : <>,
            commits : <>
         }

'''

class UserStatCache(Cache):
    """ commits cache """

    DEFAULT = os.path.realpath(os.getcwd() + "/../") + '/.userstat.cache'

    def __init__(self, cache=None):
        if cache is None:
            cache = UserStatCache.DEFAULT
        super(UserStatCache, self).__init__(cache=cache)

