#!/usr/bin/env python3

from collections import OrderedDict

class DefaultOrderedDict(OrderedDict):
    '''Extends OrderedDict with the ability to specify the default value generator.
    Example:
    # To create a DefaultOrderedDict that returns 100 as default value.
    d = DefaultOrderedDict(lambda _: 100)
    # To create a DefaultOrderedDict that generates square of the key as default value
    d = DefaultOrderedDict(lambda k: k*k)
    '''
    default_value_func = None
    def __init__(self, default_value_func):
        '''default_value_func is a function that returns the default value.'''
        self.default_value_func = default_value_func

    def __missing__(self, key):
        v = self.default_value_func(key)
        self.__setitem__(key, v)
        return v
