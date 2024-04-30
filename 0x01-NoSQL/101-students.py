#!/usr/bin/env python3
"""14. Top students"""
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    """Returns all students sorted by average score"""
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
