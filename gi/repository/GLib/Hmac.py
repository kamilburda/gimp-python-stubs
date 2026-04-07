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


class Hmac(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(digest_type:GLib.ChecksumType, key:list) -> GLib.Hmac or None
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GLib.Hmac """
        pass

    def get_digest(self, buffer): # real signature unknown; restored from __doc__
        """ get_digest(self, buffer:list) """
        pass

    def get_string(self): # real signature unknown; restored from __doc__
        """ get_string(self) -> str """
        return ""

    @classmethod
    def new(cls, digest_type, key): # real signature unknown; restored from __doc__
        """ new(digest_type:GLib.ChecksumType, key:list) -> GLib.Hmac or None """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.Hmac """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def update(self, data): # real signature unknown; restored from __doc__
        """ update(self, data:list) """
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
        """ new(digest_type:GLib.ChecksumType, key:list) -> GLib.Hmac or None """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Hmac), '__module__': 'gi.repository.GLib', '__gtype__': <GType GHmac (2640519552)>, '__dict__': <attribute '__dict__' of 'Hmac' objects>, '__weakref__': <attribute '__weakref__' of 'Hmac' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'copy': gi.FunctionInfo(copy), 'get_digest': gi.FunctionInfo(get_digest), 'get_string': gi.FunctionInfo(get_string), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'update': gi.FunctionInfo(update), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GHmac (2640519552)>'
    __info__ = StructInfo(Hmac)


