from models.singleton import Singleton


@Singleton
class MongoClient(object):
    def __init__(self, client=None):
        self._client = client

    def get_client(self):
        return self._client