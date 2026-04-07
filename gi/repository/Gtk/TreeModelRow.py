# encoding: utf-8
# module gi.repository.Gtk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .object import object

class TreeModelRow(object):
    # no doc
    def get_next(self): # reliably restored by inspect
        # no doc
        pass

    def get_parent(self): # reliably restored by inspect
        # no doc
        pass

    def get_previous(self): # reliably restored by inspect
        # no doc
        pass

    def iterchildren(self): # reliably restored by inspect
        # no doc
        pass

    def _convert_negative_index(self, index): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __init__(self, model, iter_or_path): # reliably restored by inspect
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
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setitem__(self, key, value): # reliably restored by inspect
        # no doc
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
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

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 1169, '__init__': <function TreeModelRow.__init__ at 0x000002bfcebd1fe0>, 'path': <property object at 0x000002bfcebd69d0>, 'next': <property object at 0x000002bfcebd6a20>, 'previous': <property object at 0x000002bfcebd6a70>, 'parent': <property object at 0x000002bfcebd6ac0>, 'get_next': <function TreeModelRow.get_next at 0x000002bfcebd2350>, 'get_previous': <function TreeModelRow.get_previous at 0x000002bfcebd2400>, 'get_parent': <function TreeModelRow.get_parent at 0x000002bfcebd24b0>, '__getitem__': <function TreeModelRow.__getitem__ at 0x000002bfcebd2560>, '__setitem__': <function TreeModelRow.__setitem__ at 0x000002bfcebd2610>, '_convert_negative_index': <function TreeModelRow._convert_negative_index at 0x000002bfcebd26c0>, 'iterchildren': <function TreeModelRow.iterchildren at 0x000002bfcebd2770>, '__static_attributes__': ('iter', 'model'), '__dict__': <attribute '__dict__' of 'TreeModelRow' objects>, '__weakref__': <attribute '__weakref__' of 'TreeModelRow' objects>, '__doc__': None})"
    __firstlineno__ = 1169
    __static_attributes__ = (
        'iter',
        'model',
    )


