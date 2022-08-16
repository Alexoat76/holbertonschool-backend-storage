#!/usr/bin/env python3

"""
This script contains a function that returns the
list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    if mongo_collection is None:  # if the collection is None return None
        return None
    # Return the list of school having a specific topic
    return mongo_collection.find({"topics": topic})
