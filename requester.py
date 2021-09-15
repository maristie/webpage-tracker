from http import HTTPStatus

import requests

from throttler import Throttler


class Requester:
    HEADERS = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
    }

    def __init__(self):
        self._throttler = Throttler()

    def request(self, url):
        if not self._throttler.test(url):
            return None
        r = requests.get(url, headers=self.HEADERS)
        if r.status_code == HTTPStatus.SERVICE_UNAVAILABLE.value:
            self._throttler.set(url)
        return r.text
