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


class VolumeMonitorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        VolumeMonitorClass()
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

    adopt_orphan_mount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_connected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_disconnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_eject_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    drive_stop_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_connected_drives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mounts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_mount_for_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_volume_for_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_supported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_pre_unmount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mount_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    volume_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _g_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VolumeMonitorClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'VolumeMonitorClass' objects>, '__weakref__': <attribute '__weakref__' of 'VolumeMonitorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000001ea709fad90>, 'volume_added': <property object at 0x000001ea709fae80>, 'volume_removed': <property object at 0x000001ea709faf70>, 'volume_changed': <property object at 0x000001ea709fb060>, 'mount_added': <property object at 0x000001ea709fb150>, 'mount_removed': <property object at 0x000001ea709fb240>, 'mount_pre_unmount': <property object at 0x000001ea709fb330>, 'mount_changed': <property object at 0x000001ea709fb420>, 'drive_connected': <property object at 0x000001ea709fb510>, 'drive_disconnected': <property object at 0x000001ea709fb600>, 'drive_changed': <property object at 0x000001ea709fb6f0>, 'is_supported': <property object at 0x000001ea709fb7e0>, 'get_connected_drives': <property object at 0x000001ea709fb8d0>, 'get_volumes': <property object at 0x000001ea709fb9c0>, 'get_mounts': <property object at 0x000001ea709fbab0>, 'get_volume_for_uuid': <property object at 0x000001ea709fbba0>, 'get_mount_for_uuid': <property object at 0x000001ea709fbc90>, 'adopt_orphan_mount': <property object at 0x000001ea709fbd80>, 'drive_eject_button': <property object at 0x000001ea709fbe70>, 'drive_stop_button': <property object at 0x000001ea709fbf60>, '_g_reserved1': <property object at 0x000001ea709fc090>, '_g_reserved2': <property object at 0x000001ea709fc180>, '_g_reserved3': <property object at 0x000001ea709fc270>, '_g_reserved4': <property object at 0x000001ea709fc360>, '_g_reserved5': <property object at 0x000001ea709fc450>, '_g_reserved6': <property object at 0x000001ea709fc540>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(VolumeMonitorClass)


