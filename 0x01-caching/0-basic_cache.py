#!/usr/bin/env python3
""" module that contains two caching classes
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def put(self, key, item):
        """
        put a value in the cache, the function does nothing if
        key or item is None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        this function get's the value of the key stored
        in the cache
        """
        if key is None:
            return None
        data = self.cache_data.get(key)
        return data
