import asyncio
import random
from typing import Counter


class Throttler:

    def __init__(self, delta=3):
        self._cnt = Counter()
        self._lock = asyncio.Lock()
        self._delta = delta

    async def set(self, obj, limit=10):
        async with self._lock:
            self._cnt[obj] = limit + random.randrange(0, self._delta)

    async def test(self, obj):
        async with self._lock:
            if obj not in self._cnt:
                return True
            self._cnt -= Counter({obj: 1})
            return False
