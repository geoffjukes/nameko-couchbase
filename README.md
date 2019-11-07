# About

Nameko Dependency for Couchbase.

## Usage
```python
from nameko.rpc import rpc
from nameko_couchbase import Couchbase


class MyService(object):
    name = "my_service"

    redis = Couchbase('bucket_name')

    @rpc
    def set_thing(self, key, value):
        self.couchbase.upsert(key, value)
        return "Set {} to {}".format(key, value)

    @rpc
    def get_thing(self, key):
        value = self.couchbase.ket(key)
        return "{} is {}}".format(key, value)
```
Couchbase URI is set in your config file
```yaml
AMQP_URI: 'amqp://guest:guest@localhost'
COUCHBASE_URI: 'couchbase://user:password@localhost'
```