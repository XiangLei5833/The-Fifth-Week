import redis
from cache import RedisCache

r = redis.StrictRedis(host='127.0.0.1', port=6379)
cache = RedisCache(r)

@cache.cache(timeout=10)
def execute():
    a = {'name':'test'}
    return a
