#!/usr/bin/env python3
"""9. Insert a document in Python"""
from pymongo.collection import Collection
from typing import Any


def insert_school(mongo_collection: Collection, **kwargs: dict[str, Any]):
    """Inserts a new document in a collection based on kwargs
    Returns the new _id"""
    result = mongo_collection.insert_one(kwargs)
    return result
