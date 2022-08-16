#!/usr/bin/env python3

"""
This script contains a function that lists all the documents in a collection.
"""


def list_all(mongo_collection):
    """
    Lists all the documents in a collection.
    """
    if mongo_collection is None:  # if the collection is None return None
        return []
    # return the list of all the documents in the collection
    return list(mongo_collection.find({}))
