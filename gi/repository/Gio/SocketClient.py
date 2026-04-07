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


class SocketClient(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        SocketClient(**properties)
        new() -> Gio.SocketClient
    """
    def add_application_proxy(self, protocol): # real signature unknown; restored from __doc__
        """ add_application_proxy(self, protocol:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, connectable, cancellable=None): # real signature unknown; restored from __doc__
        """ connect(self, connectable:Gio.SocketConnectable, cancellable:Gio.Cancellable=None) -> Gio.SocketConnection """
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_async(self, connectable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_async(self, connectable:Gio.SocketConnectable, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_data(self, detailed_signal, handler, *data, connect_flags=0): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_finish(self, result:Gio.AsyncResult) -> Gio.SocketConnection """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_host(self, host_and_port, default_port, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_to_host(self, host_and_port:str, default_port:int, cancellable:Gio.Cancellable=None) -> Gio.SocketConnection """
        pass

    def connect_to_host_async(self, host_and_port, default_port, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_to_host_async(self, host_and_port:str, default_port:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_to_host_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_to_host_finish(self, result:Gio.AsyncResult) -> Gio.SocketConnection """
        pass

    def connect_to_service(self, domain, service, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_to_service(self, domain:str, service:str, cancellable:Gio.Cancellable=None) -> Gio.SocketConnection """
        pass

    def connect_to_service_async(self, domain, service, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_to_service_async(self, domain:str, service:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_to_service_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_to_service_finish(self, result:Gio.AsyncResult) -> Gio.SocketConnection """
        pass

    def connect_to_uri(self, uri, default_port, cancellable=None): # real signature unknown; restored from __doc__
        """ connect_to_uri(self, uri:str, default_port:int, cancellable:Gio.Cancellable=None) -> Gio.SocketConnection """
        pass

    def connect_to_uri_async(self, uri, default_port, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ connect_to_uri_async(self, uri:str, default_port:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def connect_to_uri_finish(self, result): # real signature unknown; restored from __doc__
        """ connect_to_uri_finish(self, result:Gio.AsyncResult) -> Gio.SocketConnection """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gio.SocketClientEvent, connectable:Gio.SocketConnectable, connection:Gio.IOStream) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_enable_proxy(self): # real signature unknown; restored from __doc__
        """ get_enable_proxy(self) -> bool """
        return False

    def get_family(self): # real signature unknown; restored from __doc__
        """ get_family(self) -> Gio.SocketFamily """
        pass

    def get_local_address(self): # real signature unknown; restored from __doc__
        """ get_local_address(self) -> Gio.SocketAddress or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protocol(self): # real signature unknown; restored from __doc__
        """ get_protocol(self) -> Gio.SocketProtocol """
        pass

    def get_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ get_proxy_resolver(self) -> Gio.ProxyResolver """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_socket_type(self): # real signature unknown; restored from __doc__
        """ get_socket_type(self) -> Gio.SocketType """
        pass

    def get_timeout(self): # real signature unknown; restored from __doc__
        """ get_timeout(self) -> int """
        return 0

    def get_tls(self): # real signature unknown; restored from __doc__
        """ get_tls(self) -> bool """
        return False

    def get_tls_validation_flags(self): # real signature unknown; restored from __doc__
        """ get_tls_validation_flags(self) -> Gio.TlsCertificateFlags """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gio.SocketClient """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_enable_proxy(self, enable): # real signature unknown; restored from __doc__
        """ set_enable_proxy(self, enable:bool) """
        pass

    def set_family(self, family): # real signature unknown; restored from __doc__
        """ set_family(self, family:Gio.SocketFamily) """
        pass

    def set_local_address(self, address=None): # real signature unknown; restored from __doc__
        """ set_local_address(self, address:Gio.SocketAddress=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protocol(self, protocol): # real signature unknown; restored from __doc__
        """ set_protocol(self, protocol:Gio.SocketProtocol) """
        pass

    def set_proxy_resolver(self, proxy_resolver=None): # real signature unknown; restored from __doc__
        """ set_proxy_resolver(self, proxy_resolver:Gio.ProxyResolver=None) """
        pass

    def set_socket_type(self, type): # real signature unknown; restored from __doc__
        """ set_socket_type(self, type:Gio.SocketType) """
        pass

    def set_timeout(self, timeout): # real signature unknown; restored from __doc__
        """ set_timeout(self, timeout:int) """
        pass

    def set_tls(self, tls): # real signature unknown; restored from __doc__
        """ set_tls(self, tls:bool) """
        pass

    def set_tls_validation_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_tls_validation_flags(self, flags:Gio.TlsCertificateFlags) """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self): # reliably restored by inspect
        """ Deprecated, do not explicitly float GObjects. """
        pass

    def _ref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _ref_sink(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unref(self): # reliably restored by inspect
        """ Deprecated, do not explicitly reference GObjects. """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea70868e50>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SocketClient), '__module__': 'gi.repository.Gio', '__gtype__': <GType GSocketClient (1841600432)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'add_application_proxy': gi.FunctionInfo(add_application_proxy), 'connect': gi.FunctionInfo(connect), 'connect_async': gi.FunctionInfo(connect_async), 'connect_finish': gi.FunctionInfo(connect_finish), 'connect_to_host': gi.FunctionInfo(connect_to_host), 'connect_to_host_async': gi.FunctionInfo(connect_to_host_async), 'connect_to_host_finish': gi.FunctionInfo(connect_to_host_finish), 'connect_to_service': gi.FunctionInfo(connect_to_service), 'connect_to_service_async': gi.FunctionInfo(connect_to_service_async), 'connect_to_service_finish': gi.FunctionInfo(connect_to_service_finish), 'connect_to_uri': gi.FunctionInfo(connect_to_uri), 'connect_to_uri_async': gi.FunctionInfo(connect_to_uri_async), 'connect_to_uri_finish': gi.FunctionInfo(connect_to_uri_finish), 'get_enable_proxy': gi.FunctionInfo(get_enable_proxy), 'get_family': gi.FunctionInfo(get_family), 'get_local_address': gi.FunctionInfo(get_local_address), 'get_protocol': gi.FunctionInfo(get_protocol), 'get_proxy_resolver': gi.FunctionInfo(get_proxy_resolver), 'get_socket_type': gi.FunctionInfo(get_socket_type), 'get_timeout': gi.FunctionInfo(get_timeout), 'get_tls': gi.FunctionInfo(get_tls), 'get_tls_validation_flags': gi.FunctionInfo(get_tls_validation_flags), 'set_enable_proxy': gi.FunctionInfo(set_enable_proxy), 'set_family': gi.FunctionInfo(set_family), 'set_local_address': gi.FunctionInfo(set_local_address), 'set_protocol': gi.FunctionInfo(set_protocol), 'set_proxy_resolver': gi.FunctionInfo(set_proxy_resolver), 'set_socket_type': gi.FunctionInfo(set_socket_type), 'set_timeout': gi.FunctionInfo(set_timeout), 'set_tls': gi.FunctionInfo(set_tls), 'set_tls_validation_flags': gi.FunctionInfo(set_tls_validation_flags), 'do_event': gi.VFuncInfo(event), 'parent_instance': <property object at 0x000001ea709c7330>, 'priv': <property object at 0x000001ea709c7420>})"
    __gdoc__ = 'Object GSocketClient\n\nSignals from GSocketClient:\n  event (GSocketClientEvent, GSocketConnectable, GIOStream)\n\nProperties from GSocketClient:\n  family -> GSocketFamily: family\n  type -> GSocketType: type\n  protocol -> GSocketProtocol: protocol\n  local-address -> GSocketAddress: local-address\n  timeout -> guint: timeout\n  enable-proxy -> gboolean: enable-proxy\n  tls -> gboolean: tls\n  tls-validation-flags -> GTlsCertificateFlags: tls-validation-flags\n  proxy-resolver -> GProxyResolver: proxy-resolver\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GSocketClient (1841600432)>'
    __info__ = ObjectInfo(SocketClient)


