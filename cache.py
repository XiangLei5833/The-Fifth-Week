import json
from functools import wraps

class RedisCache:
    def __init__(self, redis_client):
        self._redis = redis_client

    def cache(self, timeout=0):
        def outer(func):
            @wraps(func)
            def inner(*args, **kwargs):
                if timeout == 0:
                    return func(*args, **kwargs)
                key = func.__name__
                value = self._redis.get(key)
                if value:
                    return json.loads(value)
                else:
                    value = func(*args, **kwargs)
                    self._redis.setex(key, timeout, json.dumps(value))
            return inner
        return outer
