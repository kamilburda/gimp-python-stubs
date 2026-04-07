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


class AppInfoIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        AppInfoIface()
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

    add_supports_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    can_remove_supports_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    do_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    equal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_commandline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_display_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_executable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_supported_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    launch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    launch_uris = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    launch_uris_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    launch_uris_finish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_supports_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_as_default_for_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_as_default_for_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_as_last_used_for_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    should_show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supports_uris = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(AppInfoIface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'AppInfoIface' objects>, '__weakref__': <attribute '__weakref__' of 'AppInfoIface' objects>, '__doc__': None, 'g_iface': <property object at 0x000001ea70409fd0>, 'dup': <property object at 0x000001ea7040a0c0>, 'equal': <property object at 0x000001ea7040a1b0>, 'get_id': <property object at 0x000001ea7040a2a0>, 'get_name': <property object at 0x000001ea7040a390>, 'get_description': <property object at 0x000001ea7040a480>, 'get_executable': <property object at 0x000001ea7040a570>, 'get_icon': <property object at 0x000001ea7040a660>, 'launch': <property object at 0x000001ea7040a750>, 'supports_uris': <property object at 0x000001ea7040a840>, 'supports_files': <property object at 0x000001ea7040a930>, 'launch_uris': <property object at 0x000001ea7040aa20>, 'should_show': <property object at 0x000001ea7040ab10>, 'set_as_default_for_type': <property object at 0x000001ea7040ac00>, 'set_as_default_for_extension': <property object at 0x000001ea7040ad40>, 'add_supports_type': <property object at 0x000001ea7040ade0>, 'can_remove_supports_type': <property object at 0x000001ea7040af20>, 'remove_supports_type': <property object at 0x000001ea7040afc0>, 'can_delete': <property object at 0x000001ea7040b0b0>, 'do_delete': <property object at 0x000001ea7040b1a0>, 'get_commandline': <property object at 0x000001ea7040b290>, 'get_display_name': <property object at 0x000001ea7040b380>, 'set_as_last_used_for_type': <property object at 0x000001ea7040b4c0>, 'get_supported_types': <property object at 0x000001ea7040b560>, 'launch_uris_async': <property object at 0x000001ea7040b650>, 'launch_uris_finish': <property object at 0x000001ea7040b740>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(AppInfoIface)


