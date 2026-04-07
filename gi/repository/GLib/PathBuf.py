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


class PathBuf(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PathBuf()
    """
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_to_path(self): # real signature unknown; restored from __doc__
        """ clear_to_path(self) -> str or None """
        return ""

    def equal(self, v1, v2): # real signature unknown; restored from __doc__
        """ equal(v1, v2) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def free_to_path(self): # real signature unknown; restored from __doc__
        """ free_to_path(self) -> str or None """
        return ""

    def init(self): # real signature unknown; restored from __doc__
        """ init(self) -> GLib.PathBuf """
        pass

    def init_from_path(self, path=None): # real signature unknown; restored from __doc__
        """ init_from_path(self, path:str=None) -> GLib.PathBuf """
        pass

    def pop(self): # real signature unknown; restored from __doc__
        """ pop(self) -> bool """
        return False

    def push(self, path): # real signature unknown; restored from __doc__
        """ push(self, path:str) -> GLib.PathBuf """
        pass

    def set_extension(self, extension=None): # real signature unknown; restored from __doc__
        """ set_extension(self, extension:str=None) -> bool """
        return False

    def set_filename(self, file_name): # real signature unknown; restored from __doc__
        """ set_filename(self, file_name:str) -> bool """
        return False

    def to_path(self): # real signature unknown; restored from __doc__
        """ to_path(self) -> str or None """
        return ""

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

    dummy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PathBuf), '__module__': 'gi.repository.GLib', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PathBuf' objects>, '__weakref__': <attribute '__weakref__' of 'PathBuf' objects>, '__doc__': None, 'dummy': <property object at 0x0000018ea007a430>, 'clear': gi.FunctionInfo(clear), 'clear_to_path': gi.FunctionInfo(clear_to_path), 'free': gi.FunctionInfo(free), 'free_to_path': gi.FunctionInfo(free_to_path), 'init': gi.FunctionInfo(init), 'init_from_path': gi.FunctionInfo(init_from_path), 'pop': gi.FunctionInfo(pop), 'push': gi.FunctionInfo(push), 'set_extension': gi.FunctionInfo(set_extension), 'set_filename': gi.FunctionInfo(set_filename), 'to_path': gi.FunctionInfo(to_path), 'equal': <staticmethod(gi.FunctionInfo(equal))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PathBuf)


