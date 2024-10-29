#!/usr/bin/python3
""" module that contains two caching classes 
"""


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise \
            NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key"""
        raise \
            NotImplementedError("get must be implemented in your cache class")


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

    def get(self, key, item):
        """
        this function get's the value of the key stored
        in the cache
        """
        if key is None or item is None:
            return None
        data = self.cache_data.get(key)
        return data
