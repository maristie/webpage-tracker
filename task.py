import asyncio
import logging
import random
from typing import Tuple

from . import config
from .model.targets import Target
from .util.notifier import notify
from .util.requester import Requester

INTERVAL = 5


async def create_task(req: Requester, tgt: Target):
    text = await req.request(tgt.value.url)
    if text is None:
        return
    if res := tgt.value.in_stock(text):
        await notify(tgt.name)
    logging.info(f'{tgt.name}: Any stock? {res}')


async def create_intervaled_tasks(req: Requester, *tgts: Tuple[Target]):
    n = len(tgts)
    for i in range(n):
        await create_task(req, tgts[i])
        if i == n-1:
            return
        await asyncio.sleep(INTERVAL + random.uniform(0, 5))
