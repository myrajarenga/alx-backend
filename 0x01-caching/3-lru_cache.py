#!/usr/bin/env python3
"""
implimentig Least recently used in caching alibrary
LRU
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU class in caching libaray"""
    def __init__(self):
        super().__init__()
        self.access_order = OrderedDict()

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            """Get the least recently used key (LRU)"""
            lru_key, _ = self.access_order.popitem(last=False)
            print("DISCARD:", lru_key)
            del self.cache_data[lru_key]

        self.cache_data[key] = item
        self.access_order[key] = None

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                    key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_order.move_to_end(key)

        return self.cache_data[key]
