import asyncio
import itertools
import random

import task
from requester import Requester
from targets import Target

DELAY = 15


async def main(req: Requester):
    for tgt in itertools.cycle(Target):
        await task.create_task(req, tgt)
        await asyncio.sleep(DELAY + random.uniform(-1.25, 5))

asyncio.run(main(Requester()))
