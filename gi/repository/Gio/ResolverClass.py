# encoding: utf-8
# module gi.repository.Gio
# by generator 1.147
# no doc

# imports
from gi.repository.GioWin32 import (NetworkMonitorClass, 
    NetworkMonitorPrivate, Win32InputStream, Win32InputStreamClass, 
    Win32InputStreamPrivate, Win32NetworkMonitor, Win32OutputStream, 
    Win32OutputStreamClass, Win32OutputStreamPrivate, 
    registry_settings_backend_new)

from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class ResolverClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ResolverClass()
    """
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

    lookup_by_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_address_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_address_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name_with_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name_with_flags_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_by_name_with_flags_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_records_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_records_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_service_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lookup_service_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reload = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ResolverClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ResolverClass' objects>, '__weakref__': <attribute '__weakref__' of 'ResolverClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000001ea709b96c0>, 'reload': <property object at 0x000001ea709b97b0>, 'lookup_by_name': <property object at 0x000001ea709b98a0>, 'lookup_by_name_async': <property object at 0x000001ea709b9990>, 'lookup_by_name_finish': <property object at 0x000001ea709b9a80>, 'lookup_by_address': <property object at 0x000001ea709b9b70>, 'lookup_by_address_async': <property object at 0x000001ea709b9c60>, 'lookup_by_address_finish': <property object at 0x000001ea709b9da0>, 'lookup_service': <property object at 0x000001ea709b9e40>, 'lookup_service_async': <property object at 0x000001ea709b9f30>, 'lookup_service_finish': <property object at 0x000001ea709ba020>, 'lookup_records': <property object at 0x000001ea709ba110>, 'lookup_records_async': <property object at 0x000001ea709ba200>, 'lookup_records_finish': <property object at 0x000001ea709ba2f0>, 'lookup_by_name_with_flags_async': <property object at 0x000001ea709ba430>, 'lookup_by_name_with_flags_finish': <property object at 0x000001ea709ba520>, 'lookup_by_name_with_flags': <property object at 0x000001ea709ba610>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ResolverClass)


