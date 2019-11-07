from urllib.parse import urlparse

from nameko.extensions import DependencyProvider
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

COUCHBASE_KEY = 'COUCHBASE_URI'


class Couchbase(DependencyProvider):

    def __init__(self, bucket):
        self.cluster = None
        self.authenticator = None
        self.bucket = bucket

    def setup(self):
        c = urlparse(self.container.config[COUCHBASE_KEY])
        self.authenticator = PasswordAuthenticator(c.username, c.password)
        self.cluster = Cluster('{}://{}'.format(c.scheme,c.hostname))

    def start(self):
        self.cluster.authenticate(self.authenticator)

    def stop(self):
        self.cluster = None

    def kill(self):
        self.cluster = None

    def get_dependency(self, worker_ctx):
        return self.cluster.open_bucket(self.bucket)
