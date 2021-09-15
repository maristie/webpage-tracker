import asyncio

from .main import main
from .util.requester import Requester

asyncio.run(main(Requester()))
