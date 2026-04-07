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


class TimeZone(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(identifier:str=None) -> GLib.TimeZone
        new_identifier(identifier:str=None) -> GLib.TimeZone or None
        new_local() -> GLib.TimeZone
        new_offset(seconds:int) -> GLib.TimeZone
        new_utc() -> GLib.TimeZone
    """
    def adjust_time(self, type, time_): # real signature unknown; restored from __doc__
        """ adjust_time(self, type:GLib.TimeType, time_:int) -> int, time_:int """
        return 0

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def find_interval(self, type, time_): # real signature unknown; restored from __doc__
        """ find_interval(self, type:GLib.TimeType, time_:int) -> int """
        return 0

    def get_abbreviation(self, interval): # real signature unknown; restored from __doc__
        """ get_abbreviation(self, interval:int) -> str """
        return ""

    def get_identifier(self): # real signature unknown; restored from __doc__
        """ get_identifier(self) -> str """
        return ""

    def get_offset(self, interval): # real signature unknown; restored from __doc__
        """ get_offset(self, interval:int) -> int """
        return 0

    def is_dst(self, interval): # real signature unknown; restored from __doc__
        """ is_dst(self, interval:int) -> bool """
        return False

    @classmethod
    def new(cls, identifier=None): # real signature unknown; restored from __doc__
        """ new(identifier:str=None) -> GLib.TimeZone """
        pass

    @classmethod
    def new_identifier(cls, identifier=None): # real signature unknown; restored from __doc__
        """ new_identifier(identifier:str=None) -> GLib.TimeZone or None """
        pass

    @classmethod
    def new_local(cls): # real signature unknown; restored from __doc__
        """ new_local() -> GLib.TimeZone """
        pass

    @classmethod
    def new_offset(cls, seconds): # real signature unknown; restored from __doc__
        """ new_offset(seconds:int) -> GLib.TimeZone """
        pass

    @classmethod
    def new_utc(cls): # real signature unknown; restored from __doc__
        """ new_utc() -> GLib.TimeZone """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.TimeZone """
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
        """ new(identifier:str=None) -> GLib.TimeZone """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TimeZone), '__module__': 'gi.repository.GLib', '__gtype__': <GType GTimeZone (2640520704)>, '__dict__': <attribute '__dict__' of 'TimeZone' objects>, '__weakref__': <attribute '__weakref__' of 'TimeZone' objects>, '__doc__': None, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_identifier': <classmethod(gi.FunctionInfo(new_identifier))>, 'new_local': <classmethod(gi.FunctionInfo(new_local))>, 'new_offset': <classmethod(gi.FunctionInfo(new_offset))>, 'new_utc': <classmethod(gi.FunctionInfo(new_utc))>, 'adjust_time': gi.FunctionInfo(adjust_time), 'find_interval': gi.FunctionInfo(find_interval), 'get_abbreviation': gi.FunctionInfo(get_abbreviation), 'get_identifier': gi.FunctionInfo(get_identifier), 'get_offset': gi.FunctionInfo(get_offset), 'is_dst': gi.FunctionInfo(is_dst), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000018e9fdc1010>})"
    __gtype__ = None # (!) real value is '<GType GTimeZone (2640520704)>'
    __info__ = StructInfo(TimeZone)


