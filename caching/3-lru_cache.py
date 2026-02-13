#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
            key key.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                you must discard the least recently used item (LRU algorithm)
                you must print DISCARD: with the key discarded and following
                by a new line
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[0]
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or doesn't exist, return None.
        """
        if key is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
