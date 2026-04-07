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


class Sequence(__gi.Struct):
    # no doc
    def append(self, data=None): # real signature unknown; restored from __doc__
        """ append(self, data=None) -> GLib.SequenceIter """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:GLib.Func, user_data=None) """
        pass

    def foreach_range(self, begin, end, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach_range(begin:GLib.SequenceIter, end:GLib.SequenceIter, func:GLib.Func, user_data=None) """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self, iter): # real signature unknown; restored from __doc__
        """ get(iter:GLib.SequenceIter) """
        pass

    def get_begin_iter(self): # real signature unknown; restored from __doc__
        """ get_begin_iter(self) -> GLib.SequenceIter """
        pass

    def get_end_iter(self): # real signature unknown; restored from __doc__
        """ get_end_iter(self) -> GLib.SequenceIter """
        pass

    def get_iter_at_pos(self, pos): # real signature unknown; restored from __doc__
        """ get_iter_at_pos(self, pos:int) -> GLib.SequenceIter """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def insert_before(self, iter, data=None): # real signature unknown; restored from __doc__
        """ insert_before(iter:GLib.SequenceIter, data=None) -> GLib.SequenceIter """
        pass

    def insert_sorted(self, data=None, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ insert_sorted(self, data=None, cmp_func:GLib.CompareDataFunc, cmp_data=None) -> GLib.SequenceIter """
        pass

    def insert_sorted_iter(self, data=None, iter_cmp, cmp_data=None): # real signature unknown; restored from __doc__
        """ insert_sorted_iter(self, data=None, iter_cmp:GLib.SequenceIterCompareFunc, cmp_data=None) -> GLib.SequenceIter """
        pass

    def is_empty(self): # real signature unknown; restored from __doc__
        """ is_empty(self) -> bool """
        return False

    def lookup(self, data=None, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ lookup(self, data=None, cmp_func:GLib.CompareDataFunc, cmp_data=None) -> GLib.SequenceIter or None """
        pass

    def lookup_iter(self, data=None, iter_cmp, cmp_data=None): # real signature unknown; restored from __doc__
        """ lookup_iter(self, data=None, iter_cmp:GLib.SequenceIterCompareFunc, cmp_data=None) -> GLib.SequenceIter or None """
        pass

    def move(self, src, dest): # real signature unknown; restored from __doc__
        """ move(src:GLib.SequenceIter, dest:GLib.SequenceIter) """
        pass

    def move_range(self, dest, begin, end): # real signature unknown; restored from __doc__
        """ move_range(dest:GLib.SequenceIter, begin:GLib.SequenceIter, end:GLib.SequenceIter) """
        pass

    def prepend(self, data=None): # real signature unknown; restored from __doc__
        """ prepend(self, data=None) -> GLib.SequenceIter """
        pass

    def range_get_midpoint(self, begin, end): # real signature unknown; restored from __doc__
        """ range_get_midpoint(begin:GLib.SequenceIter, end:GLib.SequenceIter) -> GLib.SequenceIter """
        pass

    def remove(self, iter): # real signature unknown; restored from __doc__
        """ remove(iter:GLib.SequenceIter) """
        pass

    def remove_range(self, begin, end): # real signature unknown; restored from __doc__
        """ remove_range(begin:GLib.SequenceIter, end:GLib.SequenceIter) """
        pass

    def search(self, data=None, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ search(self, data=None, cmp_func:GLib.CompareDataFunc, cmp_data=None) -> GLib.SequenceIter """
        pass

    def search_iter(self, data=None, iter_cmp, cmp_data=None): # real signature unknown; restored from __doc__
        """ search_iter(self, data=None, iter_cmp:GLib.SequenceIterCompareFunc, cmp_data=None) -> GLib.SequenceIter """
        pass

    def set(self, iter, data=None): # real signature unknown; restored from __doc__
        """ set(iter:GLib.SequenceIter, data=None) """
        pass

    def sort(self, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ sort(self, cmp_func:GLib.CompareDataFunc, cmp_data=None) """
        pass

    def sort_changed(self, iter, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ sort_changed(iter:GLib.SequenceIter, cmp_func:GLib.CompareDataFunc, cmp_data=None) """
        pass

    def sort_changed_iter(self, iter, iter_cmp, cmp_data=None): # real signature unknown; restored from __doc__
        """ sort_changed_iter(iter:GLib.SequenceIter, iter_cmp:GLib.SequenceIterCompareFunc, cmp_data=None) """
        pass

    def sort_iter(self, cmp_func, cmp_data=None): # real signature unknown; restored from __doc__
        """ sort_iter(self, cmp_func:GLib.SequenceIterCompareFunc, cmp_data=None) """
        pass

    def swap(self, a, b): # real signature unknown; restored from __doc__
        """ swap(a:GLib.SequenceIter, b:GLib.SequenceIter) """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Sequence), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Sequence' objects>, '__weakref__': <attribute '__weakref__' of 'Sequence' objects>, '__doc__': None, 'append': gi.FunctionInfo(append), 'foreach': gi.FunctionInfo(foreach), 'free': gi.FunctionInfo(free), 'get_begin_iter': gi.FunctionInfo(get_begin_iter), 'get_end_iter': gi.FunctionInfo(get_end_iter), 'get_iter_at_pos': gi.FunctionInfo(get_iter_at_pos), 'get_length': gi.FunctionInfo(get_length), 'insert_sorted': gi.FunctionInfo(insert_sorted), 'insert_sorted_iter': gi.FunctionInfo(insert_sorted_iter), 'is_empty': gi.FunctionInfo(is_empty), 'lookup': gi.FunctionInfo(lookup), 'lookup_iter': gi.FunctionInfo(lookup_iter), 'prepend': gi.FunctionInfo(prepend), 'search': gi.FunctionInfo(search), 'search_iter': gi.FunctionInfo(search_iter), 'sort': gi.FunctionInfo(sort), 'sort_iter': gi.FunctionInfo(sort_iter), 'foreach_range': <staticmethod(gi.FunctionInfo(foreach_range))>, 'get': <staticmethod(gi.FunctionInfo(get))>, 'insert_before': <staticmethod(gi.FunctionInfo(insert_before))>, 'move': <staticmethod(gi.FunctionInfo(move))>, 'move_range': <staticmethod(gi.FunctionInfo(move_range))>, 'range_get_midpoint': <staticmethod(gi.FunctionInfo(range_get_midpoint))>, 'remove': <staticmethod(gi.FunctionInfo(remove))>, 'remove_range': <staticmethod(gi.FunctionInfo(remove_range))>, 'set': <staticmethod(gi.FunctionInfo(set))>, 'sort_changed': <staticmethod(gi.FunctionInfo(sort_changed))>, 'sort_changed_iter': <staticmethod(gi.FunctionInfo(sort_changed_iter))>, 'swap': <staticmethod(gi.FunctionInfo(swap))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Sequence)


