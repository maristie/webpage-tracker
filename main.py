import asyncio
import random
from collections import defaultdict

import task
from requester import Requester
from targets import Target

DELAY = 60


async def main(req: Requester):
    while True:
        tgt_by_checker = defaultdict(list)
        for tgt in Target.rand_iter():
            tgt_by_checker[tgt.value.checker].append(tgt)
        await asyncio.gather(*(task.create_intervaled_tasks(req, *task_list) for task_list in tgt_by_checker.values()))
        await asyncio.sleep(DELAY + random.uniform(-5, 20))

asyncio.run(main(Requester()))
