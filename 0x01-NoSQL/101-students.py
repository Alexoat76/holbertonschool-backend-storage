#!/usr/bin/env python3

"""
This module contains the function that returns all students
sorted by average score
"""


# Defining the function top_students with parameter mongo_collection
def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    students = mongo_collection.aggregate(
        [
            {  # Projection to get the average score of the student
                '$project': {
                    '_id': 1,  # The id of the student
                    'name': 1,  # The name of the student
                    'averageScore': {  # The average score of the student
                        '$avg': {
                            '$avg': '$topics.score',
                        },
                    },
                    'topics': 1,  # The list of topics of the student
                },
            },
            {  # Sort the students by average score
                '$sort': {'averageScore': -1},
            },
        ]
    )
    return students  # Return the list of students sorted by average score
