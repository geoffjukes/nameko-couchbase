from urllib.parse import urlparse, urlencode

from nameko.extensions import DependencyProvider
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

COUCHBASE_KEY = 'COUCHBASE'


class Couchbase(DependencyProvider):

    def __init__(self, bucket):
        self.cluster = None
        self.authenticator = None
        self.bucket = bucket

    def setup(self):
        config = self.container.config[COUCHBASE_KEY]
        uri = urlparse(config['URI'])
        params = urlencode(config.get('CLIENT_CONFIG'), {})
        self.authenticator = PasswordAuthenticator(uri.username, uri.password)
        self.cluster = Cluster('{}://{}?{}'.format(uri.scheme, uri.hostname, params))

    def start(self):
        self.cluster.authenticate(self.authenticator)

    def stop(self):
        self.cluster = None

    def kill(self):
        self.cluster = None

    def get_dependency(self, worker_ctx):
        return self.cluster.open_bucket(self.bucket)
