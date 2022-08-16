#!/usr/bin/env python3
"""
This project module contains a Python script that provides
some stats about Nginx logs stored in MongoDB.
"""

# Import the MongoDB client.
from pymongo import MongoClient


def stats_logs() -> None:
    """
    Function that provides some stats about Nginx logs
    stored in MongoDB.
    Returns:
        Stats about Nginx logs.
    """
    # List of HTTP methods.
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    myclient = MongoClient("mongodb://localhost:27017/")
    my_database = myclient["logs"]  # Get the database "logs".
    nginx = my_database["nginx"]  # Get the collection "nginx".
    # Count the number of logs.
    print("{} logs".format(nginx.count_documents({})))
    print("Methods:")  # Print the HTTP methods used.

    for method in methods:  # For each HTTP method.
        # Print the number of logs for each method and the total.
        print(
            "\tmethod {}: {}".format(
                method, nginx.count_documents({"method": method}))
        )
        # Print the number of status checks.
    print(
        "{} status check".format(
            nginx.count_documents({"method": "GET", "path": "/status"}))
    )


if __name__ == "__main__":
    stats_logs()
