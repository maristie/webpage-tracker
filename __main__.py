import asyncio

from tracker.model.targets import Target
from tracker.scheduler import Scheduler
from tracker.util.requester import Requester

asyncio.run(Scheduler().start(Requester(), Target))
