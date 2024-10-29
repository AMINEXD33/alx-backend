#!/usr/bin/env python3
""" FIFO CACHING MODULE
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFOCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        a function that puts a new item into cache
        with respect to the limit specified in MAX_ITEMS
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        a function that gets a value from cache based on a key
        it return None if the key is None or doesn't exist
        """
        if key in None:
            return None
        return self.cache_data.get(key)
