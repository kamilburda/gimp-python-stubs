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


class IOExtensionPoint(__gi.Struct):
    # no doc
    def get_extensions(self): # real signature unknown; restored from __doc__
        """ get_extensions(self) -> list """
        return []

    def get_extension_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_extension_by_name(self, name:str) -> Gio.IOExtension """
        pass

    def get_required_type(self): # real signature unknown; restored from __doc__
        """ get_required_type(self) -> GType """
        pass

    def implement(self, extension_point_name, type, extension_name, priority): # real signature unknown; restored from __doc__
        """ implement(extension_point_name:str, type:GType, extension_name:str, priority:int) -> Gio.IOExtension """
        pass

    def lookup(self, name): # real signature unknown; restored from __doc__
        """ lookup(name:str) -> Gio.IOExtensionPoint """
        pass

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Gio.IOExtensionPoint """
        pass

    def set_required_type(self, type): # real signature unknown; restored from __doc__
        """ set_required_type(self, type:GType) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(IOExtensionPoint), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'IOExtensionPoint' objects>, '__weakref__': <attribute '__weakref__' of 'IOExtensionPoint' objects>, '__doc__': None, 'get_extension_by_name': gi.FunctionInfo(get_extension_by_name), 'get_extensions': gi.FunctionInfo(get_extensions), 'get_required_type': gi.FunctionInfo(get_required_type), 'set_required_type': gi.FunctionInfo(set_required_type), 'implement': <staticmethod(gi.FunctionInfo(implement))>, 'lookup': <staticmethod(gi.FunctionInfo(lookup))>, 'register': <staticmethod(gi.FunctionInfo(register))>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(IOExtensionPoint)


