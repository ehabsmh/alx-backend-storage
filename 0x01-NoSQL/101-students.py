#!/usr/bin/env python3
"""14. Top students"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
