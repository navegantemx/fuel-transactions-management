from flask import flash
from bson.objectid import ObjectId
import bson
from typing import Tuple


def handle_mongo_errors(func, mongo_collection, object_id: str) -> Tuple:
    """
    Execute generic functions, handle object not found exceptions
    """
    error = True
    try:
        return func(mongo_collection, object_id), False
    except bson.errors.InvalidId as e:
        flash("Couldn't find object you were looking for.", 'error')
        # TODO: Replace print with logging
        print(e)
    return None, error


def find_object(mongo_collection, object_id: str):
    """
    Generic function to find any object in any collection
    """
    return mongo_collection.find_one({"_id": ObjectId(object_id)})