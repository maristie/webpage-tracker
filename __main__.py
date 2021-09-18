import asyncio

from .model.targets import Target
from .scheduler import Scheduler
from .util.requester import Requester

asyncio.run(Scheduler().start(Requester(), Target))
