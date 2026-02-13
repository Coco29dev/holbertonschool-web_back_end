#!/usr/bin/python3
""" BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
            key key.
            If key or item is None, this method should not do anything.
            If the number of items in self.cache_data is higher that
            BaseCaching.MAX_ITEMS:
                you must discard the last item put in cache (LIFO algorithm)
                you must print DISCARD: with the key discarded and following
                by a new line
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or doesn't exist, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
