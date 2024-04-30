#!/usr/bin/env python3
"""11. Where can I learn Python?"""
from pymongo.collection import Collection
from typing import List


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[object]:
    """Returns the list of school having a specific topic"""

    return mongo_collection.find({"topics": topic})
