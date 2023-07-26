#!/usr/bin/env python3
"""
basic cahing dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """defines basic cashing"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assigns key and item to the dict"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """retrives the value of the key from the dict"""
        if key is None or self.cache_data.get(key) is None:
            return None
