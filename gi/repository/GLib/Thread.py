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


class Thread(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Thread()
        new(name:str=None, func:GLib.ThreadFunc, data=None) -> GLib.Thread
        try_new(name:str=None, func:GLib.ThreadFunc, data=None) -> GLib.Thread
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def exit(self, retval=None): # real signature unknown; restored from __doc__
        """ exit(retval=None) """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def join(self): # real signature unknown; restored from __doc__
        """ join(self) """
        pass

    @classmethod
    def new(cls, name=None, func, data=None): # real signature unknown; restored from __doc__
        """ new(name:str=None, func:GLib.ThreadFunc, data=None) -> GLib.Thread """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Thread """
        pass

    def self(self): # real signature unknown; restored from __doc__
        """ self() -> GLib.Thread """
        pass

    @classmethod
    def try_new(cls, name=None, func, data=None): # real signature unknown; restored from __doc__
        """ try_new(name:str=None, func:GLib.ThreadFunc, data=None) -> GLib.Thread """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def yield_(self): # real signature unknown; restored from __doc__
        """ yield_() """
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

    func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    joinable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Thread), '__module__': 'gi.repository.GLib', '__gtype__': <GType GThread (2640518592)>, '__dict__': <attribute '__dict__' of 'Thread' objects>, '__weakref__': <attribute '__weakref__' of 'Thread' objects>, '__doc__': None, 'func': <property object at 0x0000018ea0050d60>, 'data': <property object at 0x0000018ea0050b30>, 'joinable': <property object at 0x0000018ea0050ea0>, 'priority': <property object at 0x0000018ea0050f40>, 'new': <classmethod(gi.FunctionInfo(new))>, 'try_new': <classmethod(gi.FunctionInfo(try_new))>, 'get_name': gi.FunctionInfo(get_name), 'join': gi.FunctionInfo(join), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'error_quark': <staticmethod(gi.FunctionInfo(error_quark))>, 'exit': <staticmethod(gi.FunctionInfo(exit))>, 'self': <staticmethod(gi.FunctionInfo(self))>, 'yield_': <staticmethod(gi.FunctionInfo(yield))>})"
    __gtype__ = None # (!) real value is '<GType GThread (2640518592)>'
    __info__ = StructInfo(Thread)


