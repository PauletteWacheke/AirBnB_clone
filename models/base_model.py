#!/usr/bin/python3
"""
Defines class baseModel

"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base model class

    """
    def __init__(self, *args, **kwargs):
        """initialize ID with a new UUID if not provided"""
        if not kwargs.get("id"):
            self.id = str(uuid.uuid4())
        """initialize created_at with current datetime if not provided"""
        if not kwargs.get("created_at"):
            self.created_at = datetime.now()
        """initialize updated_at with current datetime if not provided"""
        if not kwargs.get("updated_at"):
            self.updated_at = datetime.now()

    def __str__(self):
        """string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the updated_at attribbute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """convert instance attributes to a dictionary for serialization"""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return (instance_dict)
