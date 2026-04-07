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


class TlsBackend(__gobject.GInterface):
    # no doc
    def get_certificate_type(self): # real signature unknown; restored from __doc__
        """ get_certificate_type(self) -> GType """
        pass

    def get_client_connection_type(self): # real signature unknown; restored from __doc__
        """ get_client_connection_type(self) -> GType """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.TlsBackend """
        pass

    def get_default_database(self): # real signature unknown; restored from __doc__
        """ get_default_database(self) -> Gio.TlsDatabase """
        pass

    def get_dtls_client_connection_type(self): # real signature unknown; restored from __doc__
        """ get_dtls_client_connection_type(self) -> GType """
        pass

    def get_dtls_server_connection_type(self): # real signature unknown; restored from __doc__
        """ get_dtls_server_connection_type(self) -> GType """
        pass

    def get_file_database_type(self): # real signature unknown; restored from __doc__
        """ get_file_database_type(self) -> GType """
        pass

    def get_server_connection_type(self): # real signature unknown; restored from __doc__
        """ get_server_connection_type(self) -> GType """
        pass

    def set_default_database(self, database=None): # real signature unknown; restored from __doc__
        """ set_default_database(self, database:Gio.TlsDatabase=None) """
        pass

    def supports_dtls(self): # real signature unknown; restored from __doc__
        """ supports_dtls(self) -> bool """
        return False

    def supports_tls(self): # real signature unknown; restored from __doc__
        """ supports_tls(self) -> bool """
        return False

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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(TlsBackend), '__module__': 'gi.repository.Gio', '__gtype__': <GType GTlsBackend (1848623504)>, '__dict__': <attribute '__dict__' of 'TlsBackend' objects>, '__weakref__': <attribute '__weakref__' of 'TlsBackend' objects>, '__doc__': None, '__gsignals__': {}, 'get_default': <staticmethod(gi.FunctionInfo(get_default))>, 'get_certificate_type': gi.FunctionInfo(get_certificate_type), 'get_client_connection_type': gi.FunctionInfo(get_client_connection_type), 'get_default_database': gi.FunctionInfo(get_default_database), 'get_dtls_client_connection_type': gi.FunctionInfo(get_dtls_client_connection_type), 'get_dtls_server_connection_type': gi.FunctionInfo(get_dtls_server_connection_type), 'get_file_database_type': gi.FunctionInfo(get_file_database_type), 'get_server_connection_type': gi.FunctionInfo(get_server_connection_type), 'set_default_database': gi.FunctionInfo(set_default_database), 'supports_dtls': gi.FunctionInfo(supports_dtls), 'supports_tls': gi.FunctionInfo(supports_tls)})"
    __gdoc__ = 'Interface GTlsBackend\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GTlsBackend (1848623504)>'
    __info__ = InterfaceInfo(TlsBackend)


