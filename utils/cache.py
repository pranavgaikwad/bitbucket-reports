class Cache(object):
    """ generic object cache """

    def __init__(self):
        pass

    def put(self):
        ''' puts new document in cache '''
        pass

    def get(self):
        ''' returns a document from cache '''
        pass


'''
Cache entry would look like this
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

    def __init__(self):
        ''' '''
        pass

    def put(self):
        ''' '''
        pass