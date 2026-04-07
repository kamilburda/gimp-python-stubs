# encoding: utf-8
# module gi.repository.Gegl
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Metadata(__gobject.GInterface):
    # no doc
    def get_resolution(self, unit, x, y): # real signature unknown; restored from __doc__
        """ get_resolution(self, unit:Gegl.ResolutionUnit, x:float, y:float) -> bool """
        return False

    def iter_get_value(self, iter, value): # real signature unknown; restored from __doc__
        """ iter_get_value(self, iter:Gegl.MetadataIter, value:GObject.Value) -> bool """
        return False

    def iter_init(self, iter): # real signature unknown; restored from __doc__
        """ iter_init(self, iter:Gegl.MetadataIter) """
        pass

    def iter_lookup(self, iter, key): # real signature unknown; restored from __doc__
        """ iter_lookup(self, iter:Gegl.MetadataIter, key:str) -> bool """
        return False

    def iter_next(self, iter): # real signature unknown; restored from __doc__
        """ iter_next(self, iter:Gegl.MetadataIter) -> str """
        return ""

    def iter_set_value(self, iter, value): # real signature unknown; restored from __doc__
        """ iter_set_value(self, iter:Gegl.MetadataIter, value:GObject.Value) -> bool """
        return False

    def register_map(self, file_module, flags, map): # real signature unknown; restored from __doc__
        """ register_map(self, file_module:str, flags:int, map:list) """
        pass

    def set_resolution(self, unit, x, y): # real signature unknown; restored from __doc__
        """ set_resolution(self, unit:Gegl.ResolutionUnit, x:float, y:float) -> bool """
        return False

    def unregister_map(self): # real signature unknown; restored from __doc__
        """ unregister_map(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(Metadata), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglMetadata (3652621152)>, '__dict__': <attribute '__dict__' of 'Metadata' objects>, '__weakref__': <attribute '__weakref__' of 'Metadata' objects>, '__doc__': None, '__gsignals__': {}, 'get_resolution': gi.FunctionInfo(get_resolution), 'iter_get_value': gi.FunctionInfo(iter_get_value), 'iter_init': gi.FunctionInfo(iter_init), 'iter_lookup': gi.FunctionInfo(iter_lookup), 'iter_next': gi.FunctionInfo(iter_next), 'iter_set_value': gi.FunctionInfo(iter_set_value), 'register_map': gi.FunctionInfo(register_map), 'set_resolution': gi.FunctionInfo(set_resolution), 'unregister_map': gi.FunctionInfo(unregister_map)})"
    __gdoc__ = 'Interface GeglMetadata\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglMetadata (3652621152)>'
    __info__ = InterfaceInfo(Metadata)


