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


class ByteArray(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        ByteArray()
    """
    def append(self, array, data): # real signature unknown; restored from __doc__
        """ append(array:list, data:list) -> list """
        return []

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self, array, free_segment): # real signature unknown; restored from __doc__
        """ free(array:list, free_segment:bool) -> list or None """
        return []

    def free_to_bytes(self, array): # real signature unknown; restored from __doc__
        """ free_to_bytes(array:list) -> GLib.Bytes """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> list """
        return []

    def new_take(self, data): # real signature unknown; restored from __doc__
        """ new_take(data:list) -> list """
        return []

    def prepend(self, array, data): # real signature unknown; restored from __doc__
        """ prepend(array:list, data:list) -> list """
        return []

    def ref(self, array): # real signature unknown; restored from __doc__
        """ ref(array:list) -> list """
        return []

    def remove_index(self, array, index_): # real signature unknown; restored from __doc__
        """ remove_index(array:list, index_:int) -> list """
        return []

    def remove_index_fast(self, array, index_): # real signature unknown; restored from __doc__
        """ remove_index_fast(array:list, index_:int) -> list """
        return []

    def remove_range(self, array, index_, length): # real signature unknown; restored from __doc__
        """ remove_range(array:list, index_:int, length:int) -> list """
        return []

    def set_size(self, array, length): # real signature unknown; restored from __doc__
        """ set_size(array:list, length:int) -> list """
        return []

    def sized_new(self, reserved_size): # real signature unknown; restored from __doc__
        """ sized_new(reserved_size:int) -> list """
        return []

    def sort(self, array, compare_func): # real signature unknown; restored from __doc__
        """ sort(array:list, compare_func:GLib.CompareFunc) """
        pass

    def sort_with_data(self, array, compare_func, user_data=None): # real signature unknown; restored from __doc__
        """ sort_with_data(array:list, compare_func:GLib.CompareDataFunc, user_data=None) """
        pass

    def steal(self, array): # real signature unknown; restored from __doc__
        """ steal(array:list) -> list """
        return []

    def unref(self, array): # real signature unknown; restored from __doc__
        """ unref(array:list) """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ByteArray), '__module__': 'gi.repository.GLib', '__gtype__': <GType GByteArray (2640521280)>, '__dict__': <attribute '__dict__' of 'ByteArray' objects>, '__weakref__': <attribute '__weakref__' of 'ByteArray' objects>, '__doc__': None, 'data': <property object at 0x0000018e9ff07740>, 'len': <property object at 0x0000018e9ff076f0>, 'append': <staticmethod(gi.FunctionInfo(append))>, 'free': <staticmethod(gi.FunctionInfo(free))>, 'free_to_bytes': <staticmethod(gi.FunctionInfo(free_to_bytes))>, 'new': <staticmethod(gi.FunctionInfo(new))>, 'new_take': <staticmethod(gi.FunctionInfo(new_take))>, 'prepend': <staticmethod(gi.FunctionInfo(prepend))>, 'ref': <staticmethod(gi.FunctionInfo(ref))>, 'remove_index': <staticmethod(gi.FunctionInfo(remove_index))>, 'remove_index_fast': <staticmethod(gi.FunctionInfo(remove_index_fast))>, 'remove_range': <staticmethod(gi.FunctionInfo(remove_range))>, 'set_size': <staticmethod(gi.FunctionInfo(set_size))>, 'sized_new': <staticmethod(gi.FunctionInfo(sized_new))>, 'sort': <staticmethod(gi.FunctionInfo(sort))>, 'sort_with_data': <staticmethod(gi.FunctionInfo(sort_with_data))>, 'steal': <staticmethod(gi.FunctionInfo(steal))>, 'unref': <staticmethod(gi.FunctionInfo(unref))>})"
    __gtype__ = None # (!) real value is '<GType GByteArray (2640521280)>'
    __info__ = StructInfo(ByteArray)


