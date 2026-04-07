# encoding: utf-8
# module gi.repository.GLib
# by generator 1.147
# no doc

# imports
from gi._gi import Pid, spawn_async

from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GLib as __gi_overrides_GLib
import gi._gi as __gi__gi


from .RuntimeError import RuntimeError

class GError(RuntimeError):
    # no doc
    def add_note(self, *args, **kwargs): # real signature unknown
        """ Add a note to the exception """
        pass

    def copy(self): # reliably restored by inspect
        # no doc
        pass

    def matches(self, domain, code): # reliably restored by inspect
        # no doc
        pass

    def new_literal(domain, message, code): # reliably restored by inspect
        # no doc
        pass

    def with_traceback(self, *args, **kwargs): # real signature unknown
        """ Set self.__traceback__ to tb and return self. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """
        Default object formatter.
        
        Return str(self) if format_spec is empty. Raise TypeError otherwise.
        """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, message=None, domain=None, code=0): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __cause__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __suppress_context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __traceback__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __annotations__ = {
        'code': 'int',
        'domain': 'str',
        'message': 'str',
    }
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.GLib', '__annotations__': {'message': 'str', 'domain': 'str', 'code': 'int'}, '__init__': <function GError.__init__ at 0x0000018e9e4ff950>, '__str__': <function GError.__str__ at 0x0000018e9e6096f0>, '__repr__': <function GError.__repr__ at 0x0000018e9e609850>, 'copy': <function GError.copy at 0x0000018e9e6099b0>, 'matches': <function gerror_matches at 0x0000018e9fdc33d0>, 'new_literal': <staticmethod(<function gerror_new_literal at 0x0000018e9fdc3530>)>, '__static_attributes__': ('code', 'domain', 'message'), '__weakref__': <attribute '__weakref__' of 'Error' objects>, '__doc__': None, '__gtype__': <GType GError (2636579888)>})"
    __gtype__ = None # (!) real value is '<GType GError (2636579888)>'
    __static_attributes__ = (
        'code',
        'domain',
        'message',
    )


