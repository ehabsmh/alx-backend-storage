#!/usr/bin/env python3
"""0. Writing strings to Redis"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Representing caching in memory"""
    def __init__(self) -> None:
        """Stores an instance of the Redis client as a private variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    # ________________________________________________________________________________

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key and assign a value to it
        Returns the key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
