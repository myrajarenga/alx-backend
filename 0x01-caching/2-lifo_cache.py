#!/usr/bin/env python3
"""
implimenting last in last out in caching library
LIFO
"""
from base_caching import BaseCaching
from collections import deque


class LIFOCache(BaseCaching):
    """Lifo caching class implimentation"""
    def __init__(self):
        super().__init__()
        self.insertion_order = deque()

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the last key inserted (LIFO)
            last_key = self.insertion_order.pop()
            print("DISCARD:", last_key)
            del self.cache_data[last_key]

        self.cache_data[key] = item
        self.insertion_order.appendleft(key)

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
