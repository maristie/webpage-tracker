import random
from time import sleep

from log_config import logging
from notifier import notify
from requester import Requester
from target_urls import TargetUrl

SHORT_DELAY = 5  # seconds
DELAY = 60  # seconds

requester = Requester()

while True:
    for name, url in TargetUrl.rand_url_iter():
        sleep(SHORT_DELAY + random.uniform(-1, 5))
        text = requester.request(url)
        if text is None:
            continue
        if not (res := TargetUrl[name].value.checker(text)):
            notify(name)
        logging.info(f'trying to request {name}, out of stock: {res}')
    sleep(DELAY + random.uniform(-5, 20))