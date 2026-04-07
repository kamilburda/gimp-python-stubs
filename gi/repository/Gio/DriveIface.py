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


class DriveIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        DriveIface()
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

    can_eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_poll_for_media = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_start_degraded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    disconnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eject_with_operation_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    enumerate_identifiers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_sort_key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_start_stop_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_symbolic_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_media = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_volumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_media_check_automatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_media_removable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_removable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_for_media = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    poll_for_media_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stop_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(DriveIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'DriveIface' objects>, '__weakref__': <attribute '__weakref__' of 'DriveIface' objects>, '__doc__': None, 'g_iface': <property object at 0x000001ea7095d4e0>, 'changed': <property object at 0x000001ea7095d5d0>, 'disconnected': <property object at 0x000001ea7095d6c0>, 'eject_button': <property object at 0x000001ea7095d7b0>, 'get_name': <property object at 0x000001ea7095d8a0>, 'get_icon': <property object at 0x000001ea7095d990>, 'has_volumes': <property object at 0x000001ea7095da80>, 'get_volumes': <property object at 0x000001ea7095db70>, 'is_media_removable': <property object at 0x000001ea7095dc60>, 'has_media': <property object at 0x000001ea7095dd50>, 'is_media_check_automatic': <property object at 0x000001ea7095de90>, 'can_eject': <property object at 0x000001ea7095df30>, 'can_poll_for_media': <property object at 0x000001ea7095e020>, 'eject': <property object at 0x000001ea7095e110>, 'eject_finish': <property object at 0x000001ea7095e200>, 'poll_for_media': <property object at 0x000001ea7095e2f0>, 'poll_for_media_finish': <property object at 0x000001ea7095e3e0>, 'get_identifier': <property object at 0x000001ea7095e4d0>, 'enumerate_identifiers': <property object at 0x000001ea7095e5c0>, 'get_start_stop_type': <property object at 0x000001ea7095e6b0>, 'can_start': <property object at 0x000001ea7095e7a0>, 'can_start_degraded': <property object at 0x000001ea7095e890>, 'start': <property object at 0x000001ea7095e980>, 'start_finish': <property object at 0x000001ea7095ea70>, 'can_stop': <property object at 0x000001ea7095eb60>, 'stop': <property object at 0x000001ea7095ec50>, 'stop_finish': <property object at 0x000001ea7095ed40>, 'stop_button': <property object at 0x000001ea7095ee30>, 'eject_with_operation': <property object at 0x000001ea7095ef20>, 'eject_with_operation_finish': <property object at 0x000001ea7095f060>, 'get_sort_key': <property object at 0x000001ea7095f100>, 'get_symbolic_icon': <property object at 0x000001ea7095f1f0>, 'is_removable': <property object at 0x000001ea7095f2e0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(DriveIface)


