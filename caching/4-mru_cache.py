#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
    """

    def __init__(self):
        """ Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            mru_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(mru_key))
            del self.cache_data[mru_key]
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
