#!/usr/bin/env python3

"""
Module for inserting a new document in a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs
    """

    resultat = mongo_collection.insert_one(kwargs)

    return resultat.inserted_id
