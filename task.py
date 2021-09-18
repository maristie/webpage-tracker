import asyncio
import logging
import random
from typing import Tuple

from . import log as _
from .model.targets import Target
from .util.notifier import notify
from .util.requester import Requester

INTERVAL = 5


async def create_task(req: Requester, target: Target):
    text = await req.request(target.value.url)
    if text is None:
        return
    if res := target.value.in_stock(text):
        await notify(target.name)
    logging.info(f'{target.name}: Any stock? {res}')


async def create_intervaled_tasks(req: Requester, *targets: Tuple[Target]):
    n = len(targets)
    for i in range(n):
        await create_task(req, targets[i])
        if i == n-1:
            return
        await asyncio.sleep(INTERVAL + random.uniform(0, 5))
