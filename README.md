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
        value = self.couchbase.get(key)
        return "{} is {}}".format(key, value)
```
Couchbase URI is set in your config file
```yaml
AMQP_URI: 'amqp://guest:guest@localhost'
COUCHBASE:
  URI: 'couchbase://user:password@localhost'
  CLIENT_CONFIG:
    operation_timeout: 10
```