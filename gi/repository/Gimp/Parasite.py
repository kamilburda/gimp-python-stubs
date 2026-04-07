# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Parasite(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        Parasite()
        new(name:str, flags:int, data:list=None) -> Gimp.Parasite
    """
    def compare(self, b): # real signature unknown; restored from __doc__
        """ compare(self, b:Gimp.Parasite) -> bool """
        return False

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gimp.Parasite """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> list """
        return []

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def has_flag(self, flag): # real signature unknown; restored from __doc__
        """ has_flag(self, flag:int) -> bool """
        return False

    def is_persistent(self): # real signature unknown; restored from __doc__
        """ is_persistent(self) -> bool """
        return False

    def is_type(self, name): # real signature unknown; restored from __doc__
        """ is_type(self, name:str) -> bool """
        return False

    def is_undoable(self): # real signature unknown; restored from __doc__
        """ is_undoable(self) -> bool """
        return False

    @classmethod
    def new(cls, name, flags, data=None): # real signature unknown; restored from __doc__
        """ new(name:str, flags:int, data:list=None) -> Gimp.Parasite """
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Parasite), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpParasite (2360868928)>, '__dict__': <attribute '__dict__' of 'Parasite' objects>, '__weakref__': <attribute '__weakref__' of 'Parasite' objects>, '__doc__': None, 'name': <property object at 0x000001268f52d6c0>, 'flags': <property object at 0x000001268f52d7b0>, 'size': <property object at 0x000001268f52d8a0>, 'data': <property object at 0x000001268f52d990>, 'new': <classmethod(gi.FunctionInfo(new))>, 'compare': gi.FunctionInfo(compare), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_data': gi.FunctionInfo(get_data), 'get_flags': gi.FunctionInfo(get_flags), 'get_name': gi.FunctionInfo(get_name), 'has_flag': gi.FunctionInfo(has_flag), 'is_persistent': gi.FunctionInfo(is_persistent), 'is_type': gi.FunctionInfo(is_type), 'is_undoable': gi.FunctionInfo(is_undoable)})"
    __gtype__ = None # (!) real value is '<GType GimpParasite (2360868928)>'
    __info__ = StructInfo(Parasite)


