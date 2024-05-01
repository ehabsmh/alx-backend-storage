#!/usr/bin/env python3
"""0. Writing strings to Redis"""
import redis
from uuid import UUID, uuid4
from typing import Union


class Cache:
    """Representing caching in memory"""
    def __init__(self):
        """Stores an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    # ________________________________________________________________________________

    def store(self: "Cache", data: Union[str, bytes, int, float]):
        """Generates a random key and assign a value to it
        Returns the key"""
        key: UUID = str(uuid4())
        self._redis.set(key, data)
        return key
