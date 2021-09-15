import random
from enum import Enum
from typing import Callable, NamedTuple

from parsing import amazon, msft, rakuten


class Item(NamedTuple):
    url: str
    checker: Callable


class Target(Enum):
    MSFT = Item(
        'https://www.microsoft.com/ja-jp/store/collections/xboxconsoles/pc', msft.out_of_stock)
    # msft alternative URL: https://www.xbox.com/ja-jp/configure/942j774tp9jn
    RAKUTEN = Item(
        'https://books.rakuten.co.jp/rb/16465628/?bkts=1', rakuten.out_of_stock)
    AMAZON1 = Item('https://www.amazon.co.jp/dp/B08GG1VG23',
                   amazon.out_of_stock)
    AMAZON2 = Item('https://www.amazon.co.jp/dp/B08GG459RG',
                   amazon.out_of_stock)

    @classmethod
    def rand_iter(cls):
        tgt_list = list(cls)
        yield from random.sample(tgt_list, len(tgt_list))