import requests

class BitbucketRequests:

    URL = "https://api.bitbucket.org/2.0/"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _headers(self):
        return {
            'User-Agent' : 'Bitbucket Reports App',
            'Content-Type': 'application/json'
        }

    def _auth(self):
        ''' HTTP auth '''
        return requests.auth.HTTPBasicAuth(self.username, self.password) 

    def get(self, url):
        ''' get request with some custom params and auth '''
        headers = self._headers()
        authent = self._auth()
        return requests.get(BitbucketRequests.URL + url, auth=authent, headers=headers)

