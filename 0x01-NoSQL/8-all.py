#!/usr/bin/env python3
"""8. List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection:
    Returns an empty list if no document in the collection"""
    documents = mongo_collection.find()
    if not documents:
        return []
    
    return documents
