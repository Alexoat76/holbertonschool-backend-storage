#!/usr/bin/env python3

"""
This script contains a function that changes all topics of a
school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    if mongo_collection is None:  # if the collection is None return None
        return None
    # Update the document in the collection
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
