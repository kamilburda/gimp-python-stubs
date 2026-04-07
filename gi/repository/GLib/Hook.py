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


class Hook(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        Hook()
    """
    def compare_ids(self, sibling): # real signature unknown; restored from __doc__
        """ compare_ids(self, sibling:GLib.Hook) -> int """
        return 0

    def destroy(self, hook_list, hook_id): # real signature unknown; restored from __doc__
        """ destroy(hook_list:GLib.HookList, hook_id:int) -> bool """
        return False

    def destroy_link(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ destroy_link(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def free(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ free(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def insert_before(self, hook_list, sibling=None, hook): # real signature unknown; restored from __doc__
        """ insert_before(hook_list:GLib.HookList, sibling:GLib.Hook=None, hook:GLib.Hook) """
        pass

    def insert_sorted(self, hook_list, hook, func): # real signature unknown; restored from __doc__
        """ insert_sorted(hook_list:GLib.HookList, hook:GLib.Hook, func:GLib.HookCompareFunc) """
        pass

    def prepend(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ prepend(hook_list:GLib.HookList, hook:GLib.Hook) """
        pass

    def unref(self, hook_list, hook): # real signature unknown; restored from __doc__
        """ unref(hook_list:GLib.HookList, hook:GLib.Hook) """
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hook_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    prev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Hook), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'Hook' objects>, '__weakref__': <attribute '__weakref__' of 'Hook' objects>, '__doc__': None, 'data': <property object at 0x0000018e9ff8a070>, 'next': <property object at 0x0000018e9ff8a160>, 'prev': <property object at 0x0000018e9ff8a250>, 'ref_count': <property object at 0x0000018e9ff8a340>, 'hook_id': <property object at 0x0000018e9ff8a430>, 'flags': <property object at 0x0000018e9ff8a520>, 'func': <property object at 0x0000018e9ff8a610>, 'destroy': <staticmethod(gi.FunctionInfo(destroy))>, 'compare_ids': gi.FunctionInfo(compare_ids), 'destroy_link': <staticmethod(gi.FunctionInfo(destroy_link))>, 'free': <staticmethod(gi.FunctionInfo(free))>, 'insert_before': <staticmethod(gi.FunctionInfo(insert_before))>, 'insert_sorted': <staticmethod(gi.FunctionInfo(insert_sorted))>, 'prepend': <staticmethod(gi.FunctionInfo(prepend))>, 'unref': <staticmethod(gi.FunctionInfo(unref))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(Hook)


