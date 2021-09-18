import string
from enum import Enum
from typing import Callable, NamedTuple

from tracker import parsing
from tracker.config import URL_PROPS


class Item(NamedTuple):
    url: str
    in_stock: Callable


def _populate_enum(name, props):
    def in_stock_func_by_key(key):
        return getattr(parsing, key.strip(string.digits).lower()).in_stock
    mapping = {k: Item(url=v, in_stock=in_stock_func_by_key(k))
               for k, v in props.items()}
    return Enum(name, mapping)


Target = _populate_enum('Target', URL_PROPS.mapping)
