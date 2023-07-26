#!/usr/bin/env python3
"""
first in the cache gets to be removed first
fifo
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implimenting FIFO"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the first key inserted (FIFO)
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]

        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
