import asyncio
import random
from typing import Counter

DELTA = 3


class Throttler:
    def __init__(self):
        self._cnt = Counter()
        self._lock = asyncio.Lock()

    async def set(self, obj, limit=10):
        async with self._lock:
            self._cnt[obj] = limit + random.randrange(0, DELTA)

    async def test(self, obj):
        async with self._lock:
            if obj not in self._cnt:
                return True
            self._cnt -= Counter({obj: 1})
            return False
