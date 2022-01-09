from fastapi import APIRouter

from core.redis import redis_cache

router = APIRouter()


@router.get("/")
async def read_root():
    value = await redis_cache.get("test_key")
    if not value:
        await redis_cache.set("test_key", "test_value")
        value = "not from cache"

    return {"Hello": value}
