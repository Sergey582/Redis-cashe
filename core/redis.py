import aioredis

from core.settings import REDIS_URL

redis_cache = aioredis.from_url(REDIS_URL)
