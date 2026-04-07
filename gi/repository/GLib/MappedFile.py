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


class MappedFile(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(filename:str, writable:bool) -> GLib.MappedFile
        new_from_fd(fd:int, writable:bool) -> GLib.MappedFile
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_bytes(self): # real signature unknown; restored from __doc__
        """ get_bytes(self) -> GLib.Bytes """
        pass

    def get_contents(self): # real signature unknown; restored from __doc__
        """ get_contents(self) -> str or None """
        return ""

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    @classmethod
    def new(cls, filename, writable): # real signature unknown; restored from __doc__
        """ new(filename:str, writable:bool) -> GLib.MappedFile """
        pass

    @classmethod
    def new_from_fd(cls, fd, writable): # real signature unknown; restored from __doc__
        """ new_from_fd(fd:int, writable:bool) -> GLib.MappedFile """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.MappedFile """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new(filename:str, writable:bool) -> GLib.MappedFile """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(MappedFile), '__module__': 'gi.repository.GLib', '__gtype__': <GType GMappedFile (2640520128)>, '__dict__': <attribute '__dict__' of 'MappedFile' objects>, '__weakref__': <attribute '__weakref__' of 'MappedFile' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_fd': <classmethod(gi.FunctionInfo(new_from_fd))>, 'free': gi.FunctionInfo(free), 'get_bytes': gi.FunctionInfo(get_bytes), 'get_contents': gi.FunctionInfo(get_contents), 'get_length': gi.FunctionInfo(get_length), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GMappedFile (2640520128)>'
    __info__ = StructInfo(MappedFile)


