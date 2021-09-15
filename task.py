import asyncio
import logging
import random
from typing import Tuple

import log_config
from notifier import notify
from requester import Requester
from targets import Target

INTERVAL = 5


async def create_task(req: Requester, tgt: Target):
    text = await req.request(tgt.value.url)
    if text is None:
        return
    if not (res := tgt.value.checker(text)):
        await notify(tgt.name)
    logging.info(
        f'Trying to request {tgt.name}, is out of stock: {res}')


async def create_intervaled_tasks(req: Requester, *tgts: Tuple[Target]):
    n = len(tgts)
    for i in range(n):
        await create_task(req, tgts[i])
        if i == n-1:
            return
        await asyncio.sleep(INTERVAL + random.uniform(0, 5))