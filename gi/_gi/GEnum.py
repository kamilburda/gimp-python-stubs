# encoding: utf-8
# module gi._gi
# by generator 1.147
# no doc

# imports
from gobject import GBoxed, GInterface, GPointer, GType, Warning

import enum as __enum
import gi as __gi
import gobject as __gobject


class GEnum(__enum.IntEnum):
    # no doc
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def _value_repr_(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Convert to a string according to format_spec. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _hashable_values_ = []
    _member_map_ = {}
    _member_names_ = []
    _member_type_ = int
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = True
    _value2member_map_ = {}
    __firstlineno__ = 51
    __gtype__ = None # (!) real value is '<GType GEnum (48)>'
    __static_attributes__ = ()


