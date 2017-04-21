#!/usr/bin/env python3

class Jsonify(object):
    """ Takes a dictionary and creates an attribute mapped recursive class """
    def __init__(self, json):
        self.__dict__ = {}
        for key in json:
            if not type(json[key]) == dict:
                self.__dict__[key] = json[key]
            else:
                self.__dict__[key] = self.__class__(json[key])

