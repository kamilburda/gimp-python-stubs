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


class Random(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> Gegl.Random
        new_with_seed(seed:int) -> Gegl.Random
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> Gegl.Random """
        pass

    def float(self, x, y, z, n): # real signature unknown; restored from __doc__
        """ float(self, x:int, y:int, z:int, n:int) -> float """
        return 0.0

    def float_range(self, x, y, z, n, min, max): # real signature unknown; restored from __doc__
        """ float_range(self, x:int, y:int, z:int, n:int, min:float, max:float) -> float """
        return 0.0

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def int(self, x, y, z, n): # real signature unknown; restored from __doc__
        """ int(self, x:int, y:int, z:int, n:int) -> int """
        return 0

    def int_range(self, x, y, z, n, min, max): # real signature unknown; restored from __doc__
        """ int_range(self, x:int, y:int, z:int, n:int, min:int, max:int) -> int """
        return 0

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gegl.Random """
        pass

    @classmethod
    def new_with_seed(cls, seed): # real signature unknown; restored from __doc__
        """ new_with_seed(seed:int) -> Gegl.Random """
        pass

    def set_seed(self, seed): # real signature unknown; restored from __doc__
        """ set_seed(self, seed:int) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
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
        """ new() -> Gegl.Random """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Random), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglRandom (3657336096)>, '__dict__': <attribute '__dict__' of 'Random' objects>, '__weakref__': <attribute '__weakref__' of 'Random' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_with_seed': <classmethod(gi.FunctionInfo(new_with_seed))>, 'duplicate': gi.FunctionInfo(duplicate), 'float': gi.FunctionInfo(float), 'float_range': gi.FunctionInfo(float_range), 'free': gi.FunctionInfo(free), 'int': gi.FunctionInfo(int), 'int_range': gi.FunctionInfo(int_range), 'set_seed': gi.FunctionInfo(set_seed), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000001ebdc19cfe0>})"
    __gtype__ = None # (!) real value is '<GType GeglRandom (3657336096)>'
    __info__ = StructInfo(Random)


