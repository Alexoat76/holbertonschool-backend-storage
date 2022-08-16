#!/usr/bin/env python3

"""
This script contains a function that inserts a new document in
a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    """
    if mongo_collection is None:  # if the collection is None return None
        return None
    # insert the new document in the collection
    return mongo_collection.insert_one(kwargs).inserted_id
