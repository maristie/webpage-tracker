import asyncio
import itertools
import random

from . import task
from .model.targets import Target
from .util.requester import Requester

DELAY = 15


async def main(req: Requester):
    for tgt in itertools.cycle(Target):
        await task.create_task(req, tgt)
        await asyncio.sleep(DELAY + random.uniform(-1.25, 5))
