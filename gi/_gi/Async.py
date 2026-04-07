# encoding: utf-8
# module gi._gi
# by generator 1.147
# no doc

# imports
from gobject import GBoxed, GInterface, GPointer, GType, Warning

import enum as __enum
import gi as __gi
import gobject as __gobject


from .object import object

class Async(object):
    # no doc
    def add_done_callback(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, *args, **kwargs): # real signature unknown
        pass

    def exception(self, *args, **kwargs): # real signature unknown
        pass

    def remove_done_callback(self, *args, **kwargs): # real signature unknown
        pass

    def result(self, *args, **kwargs): # real signature unknown
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        """ Called when the instance is about to be destroyed. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    cancellable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Gio.Cancellable associated with the task."""

    _asyncio_future_blocking = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _finish_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _loop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



