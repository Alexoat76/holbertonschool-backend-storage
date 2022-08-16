#!/usr/bin/env python3
"""
This script provides some stats about
Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def stats_logs() -> None:
    """
    This function provides some stats about
    Nginx logs stored in MongoDB
    """
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']  # List of HTTP methods
    client = MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
    db = client.logs  # Select the database
    nginx = db.nginx  # Select the collection
    print("{}logs".format(nginx.count_documents({})))  # Count number of logs
    print("Methods:")  # Print the methods used

    for method in methods:  # For each method in the list
        print("{}: {}".format(
            method, nginx.count_documents({'method': method})
            ))

    print("{} status checks".format(
        nginx.count_documents({"method": "GET", "path": "/status"})
        ))


if __name__ == "__main__":
    stats_logs()
