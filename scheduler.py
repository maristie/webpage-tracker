import asyncio
import itertools
import random
from asyncio.locks import Lock
from typing import Iterable

from . import task
from .model.targets import Target
from .util.requester import Requester


class Scheduler:
    def __init__(self, delay=10, lowerdelta=-1, upperdelta=4):
        self._delay = delay
        self._lowerdelta = lowerdelta
        self._upperdelta = upperdelta
        self._lock = Lock()

    async def _rand(self):
        async with self._lock:
            return random.uniform(self._lowerdelta, self._upperdelta)

    async def start(self, req: Requester, targets: Iterable[Target]):
        for target in itertools.cycle(targets):
            await task.create_task(req, target)
            await asyncio.sleep(self._delay + (await self._rand()))
