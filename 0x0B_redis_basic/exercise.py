#!/usr/bin/env python3
"""
Exercise module for Redis basic operations
"""
import redis
import functools
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called

    Args:
        method: The method to wrap

    Returns:
        The wrapped method that increments a counter in Redis
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call count and call the original method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Cache class using Redis"""

    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis with a random key

        Args:
            data: Data to store (str, bytes, int, or float)

        Returns:
            The randomly generated key as a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis and optionally convert it

        Args:
            key: The key to look up
            fn: Optional callable to convert the data

        Returns:
            The data, converted by fn if provided, or None if key not found
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis as a UTF-8 string

        Args:
            key: The key to look up

        Returns:
            The data decoded as a string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis as an integer

        Args:
            key: The key to look up

        Returns:
            The data converted to an int
        """
        return self.get(key, fn=int)
