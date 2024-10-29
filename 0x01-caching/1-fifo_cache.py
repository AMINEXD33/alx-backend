#!/usr/bin/python3
""" FIFO CACHING MODULE
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFOCache defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """
        a function that puts a new item into cache
        with respect to the limit specified in MAX_ITEMS
        """
        if key is None or item is None:
            return
        if len(self.cache_data) > FIFOCache.MAX_ITEMS:
            first_key = [ x for x in self.cache_data.keys()][0]
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            self.MAX_ITEMS += 1

    def get(self, key):
        """
        a function that gets a value from cache based on a key
        it return None if the key is None or doesn't exist
        """
        if key in None:
            return None
        data = self.cache_data.get(key)
        return data        