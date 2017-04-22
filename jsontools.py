#!/usr/bin/env python3
from json import loads

class Jsonify(object):
    """ Takes a dictionary and creates an attribute mapped recursive class """
    def __init__(self, json):
        self.__dict__ = {}
        if type(json) == str:
            pass
        elif type(json) == dict:
            json = json.__str__().replace("'",'"')
        else:
            raise Exception('Invalid type "{}"'.format(type(json)))
        json = loads(json)
        for key in json:
            if not type(json[key]) == dict:
                self.__dict__[key] = json[key]
            else:
                self.__dict__[key] = self.__class__(json[key])
