#!/usr/bin/env python3
"""
Implimenting most recently used in caching library
MRU
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """mru class in caching librsry"""
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
            """Get the most recently used key (MRU)"""
            mru_key, _ = self.access_order.popitem(last=True)
            print("DISCARD:", mru_key)
            del self.cache_data[mru_key]

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
