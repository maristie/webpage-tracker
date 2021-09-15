import random
from typing import Counter

DELTA = 3


class Throttler:
    def __init__(self):
        self._cnt = Counter()

    def set(self, obj, limit=10):
        self._cnt[obj] = limit + random.randrange(0, DELTA)

    def test(self, obj):
        if obj not in self._cnt:
            return True
        self._cnt -= Counter({obj: 1})
        return False
