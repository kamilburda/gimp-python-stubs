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


from .AsyncInitable import AsyncInitable

from .Initable import Initable

class DBusConnection(__gi_overrides_GObject.Object, AsyncInitable, Initable):
    """
    :Constructors:
    
    ::
    
        DBusConnection(**properties)
        new_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_finish(res:Gio.AsyncResult) -> Gio.DBusConnection
        new_for_address_sync(address:str, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection
        new_sync(stream:Gio.IOStream, guid:str=None, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection
    """
    def add_filter(self, filter_function, user_data=None): # real signature unknown; restored from __doc__
        """ add_filter(self, filter_function:Gio.DBusMessageFilterFunction, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def call(self, bus_name=None, object_path, interface_name, method_name, parameters=None, reply_type=None, flags, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ call(self, bus_name:str=None, object_path:str, interface_name:str, method_name:str, parameters:GLib.Variant=None, reply_type:GLib.VariantType=None, flags:Gio.DBusCallFlags, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def call_finish(self, res): # real signature unknown; restored from __doc__
        """ call_finish(self, res:Gio.AsyncResult) -> GLib.Variant """
        pass

    def call_sync(self, bus_name=None, object_path, interface_name, method_name, parameters=None, reply_type=None, flags, timeout_msec, cancellable=None): # real signature unknown; restored from __doc__
        """ call_sync(self, bus_name:str=None, object_path:str, interface_name:str, method_name:str, parameters:GLib.Variant=None, reply_type:GLib.VariantType=None, flags:Gio.DBusCallFlags, timeout_msec:int, cancellable:Gio.Cancellable=None) -> GLib.Variant """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, res): # real signature unknown; restored from __doc__
        """ close_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def close_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
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

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_signal(self, destination_bus_name=None, object_path, interface_name, signal_name, parameters=None): # real signature unknown; restored from __doc__
        """ emit_signal(self, destination_bus_name:str=None, object_path:str, interface_name:str, signal_name:str, parameters:GLib.Variant=None) -> bool """
        return False

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def export_action_group(self, object_path, action_group): # real signature unknown; restored from __doc__
        """ export_action_group(self, object_path:str, action_group:Gio.ActionGroup) -> int """
        return 0

    def export_menu_model(self, object_path, menu): # real signature unknown; restored from __doc__
        """ export_menu_model(self, object_path:str, menu:Gio.MenuModel) -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ flush(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def flush_finish(self, res): # real signature unknown; restored from __doc__
        """ flush_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def flush_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ flush_sync(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def get_capabilities(self): # real signature unknown; restored from __doc__
        """ get_capabilities(self) -> Gio.DBusCapabilityFlags """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_exit_on_close(self): # real signature unknown; restored from __doc__
        """ get_exit_on_close(self) -> bool """
        return False

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusConnectionFlags """
        pass

    def get_guid(self): # real signature unknown; restored from __doc__
        """ get_guid(self) -> str """
        return ""

    def get_last_serial(self): # real signature unknown; restored from __doc__
        """ get_last_serial(self) -> int """
        return 0

    def get_peer_credentials(self): # real signature unknown; restored from __doc__
        """ get_peer_credentials(self) -> Gio.Credentials or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_stream(self): # real signature unknown; restored from __doc__
        """ get_stream(self) -> Gio.IOStream """
        pass

    def get_unique_name(self): # real signature unknown; restored from __doc__
        """ get_unique_name(self) -> str or None """
        return ""

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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
        return False

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

    def is_closed(self): # real signature unknown; restored from __doc__
        """ is_closed(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def new(self, stream, guid=None, flags, observer=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(stream:Gio.IOStream, guid:str=None, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    @classmethod
    def new_finish(cls, res): # real signature unknown; restored from __doc__
        """ new_finish(res:Gio.AsyncResult) -> Gio.DBusConnection """
        pass

    def new_for_address(self, address, flags, observer=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_for_address(address:str, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    @classmethod
    def new_for_address_finish(cls, res): # real signature unknown; restored from __doc__
        """ new_for_address_finish(res:Gio.AsyncResult) -> Gio.DBusConnection """
        pass

    @classmethod
    def new_for_address_sync(cls, address, flags, observer=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_for_address_sync(address:str, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection """
        pass

    @classmethod
    def new_sync(cls, stream, guid=None, flags, observer=None, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(stream:Gio.IOStream, guid:str=None, flags:Gio.DBusConnectionFlags, observer:Gio.DBusAuthObserver=None, cancellable:Gio.Cancellable=None) -> Gio.DBusConnection """
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

    def register_object(self, object_path, interface_info, method_call_closure=None, get_property_closure=None, set_property_closure=None): # real signature unknown; restored from __doc__
        """ register_object(self, object_path:str, interface_info:Gio.DBusInterfaceInfo, method_call_closure:GObject.Closure=None, get_property_closure:GObject.Closure=None, set_property_closure:GObject.Closure=None) -> int """
        return 0

    def register_object_with_closures2(self, object_path, interface_info, method_call_closure=None, get_property_closure=None, set_property_closure=None): # real signature unknown; restored from __doc__
        """ register_object_with_closures2(self, object_path:str, interface_info:Gio.DBusInterfaceInfo, method_call_closure:GObject.Closure=None, get_property_closure:GObject.Closure=None, set_property_closure:GObject.Closure=None) -> int """
        return 0

    def register_subtree(self, object_path, vtable, flags, user_data=None, user_data_free_func): # real signature unknown; restored from __doc__
        """ register_subtree(self, object_path:str, vtable:Gio.DBusSubtreeVTable, flags:Gio.DBusSubtreeFlags, user_data=None, user_data_free_func:GLib.DestroyNotify) -> int """
        return 0

    def remove_filter(self, filter_id): # real signature unknown; restored from __doc__
        """ remove_filter(self, filter_id:int) """
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

    def send_message(self, message, flags): # real signature unknown; restored from __doc__
        """ send_message(self, message:Gio.DBusMessage, flags:Gio.DBusSendMessageFlags) -> bool, out_serial:int """
        return False

    def send_message_with_reply(self, message, flags, timeout_msec, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ send_message_with_reply(self, message:Gio.DBusMessage, flags:Gio.DBusSendMessageFlags, timeout_msec:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) -> out_serial:int """
        pass

    def send_message_with_reply_finish(self, res): # real signature unknown; restored from __doc__
        """ send_message_with_reply_finish(self, res:Gio.AsyncResult) -> Gio.DBusMessage """
        pass

    def send_message_with_reply_sync(self, message, flags, timeout_msec, cancellable=None): # real signature unknown; restored from __doc__
        """ send_message_with_reply_sync(self, message:Gio.DBusMessage, flags:Gio.DBusSendMessageFlags, timeout_msec:int, cancellable:Gio.Cancellable=None) -> Gio.DBusMessage, out_serial:int """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_exit_on_close(self, exit_on_close): # real signature unknown; restored from __doc__
        """ set_exit_on_close(self, exit_on_close:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def signal_subscribe(self, sender=None, interface_name=None, member=None, object_path=None, arg0=None, flags, callback, user_data=None): # real signature unknown; restored from __doc__
        """ signal_subscribe(self, sender:str=None, interface_name:str=None, member:str=None, object_path:str=None, arg0:str=None, flags:Gio.DBusSignalFlags, callback:Gio.DBusSignalCallback, user_data=None) -> int """
        return 0

    def signal_unsubscribe(self, subscription_id): # real signature unknown; restored from __doc__
        """ signal_unsubscribe(self, subscription_id:int) """
        pass

    def start_message_processing(self): # real signature unknown; restored from __doc__
        """ start_message_processing(self) """
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

    def unexport_action_group(self, export_id): # real signature unknown; restored from __doc__
        """ unexport_action_group(self, export_id:int) """
        pass

    def unexport_menu_model(self, export_id): # real signature unknown; restored from __doc__
        """ unexport_menu_model(self, export_id:int) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_object(self, registration_id): # real signature unknown; restored from __doc__
        """ unregister_object(self, registration_id:int) -> bool """
        return False

    def unregister_subtree(self, registration_id): # real signature unknown; restored from __doc__
        """ unregister_subtree(self, registration_id:int) -> bool """
        return False

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea7084a770>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DBusConnection), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDBusConnection (1841878560)>, '__doc__': None, '__gsignals__': {}, 'new_finish': <classmethod(gi.FunctionInfo(new_finish))>, 'new_for_address_finish': <classmethod(gi.FunctionInfo(new_for_address_finish))>, 'new_for_address_sync': <classmethod(gi.FunctionInfo(new_for_address_sync))>, 'new_sync': <classmethod(gi.FunctionInfo(new_sync))>, 'new': <staticmethod(gi.FunctionInfo(new))>, 'new_for_address': <staticmethod(gi.FunctionInfo(new_for_address))>, 'add_filter': gi.FunctionInfo(add_filter), 'call': gi.FunctionInfo(call), 'call_finish': gi.FunctionInfo(call_finish), 'call_sync': gi.FunctionInfo(call_sync), 'close': gi.FunctionInfo(close), 'close_finish': gi.FunctionInfo(close_finish), 'close_sync': gi.FunctionInfo(close_sync), 'emit_signal': gi.FunctionInfo(emit_signal), 'export_action_group': gi.FunctionInfo(export_action_group), 'export_menu_model': gi.FunctionInfo(export_menu_model), 'flush': gi.FunctionInfo(flush), 'flush_finish': gi.FunctionInfo(flush_finish), 'flush_sync': gi.FunctionInfo(flush_sync), 'get_capabilities': gi.FunctionInfo(get_capabilities), 'get_exit_on_close': gi.FunctionInfo(get_exit_on_close), 'get_flags': gi.FunctionInfo(get_flags), 'get_guid': gi.FunctionInfo(get_guid), 'get_last_serial': gi.FunctionInfo(get_last_serial), 'get_peer_credentials': gi.FunctionInfo(get_peer_credentials), 'get_stream': gi.FunctionInfo(get_stream), 'get_unique_name': gi.FunctionInfo(get_unique_name), 'is_closed': gi.FunctionInfo(is_closed), 'register_object': gi.FunctionInfo(register_object), 'register_object_with_closures2': gi.FunctionInfo(register_object_with_closures2), 'register_subtree': gi.FunctionInfo(register_subtree), 'remove_filter': gi.FunctionInfo(remove_filter), 'send_message': gi.FunctionInfo(send_message), 'send_message_with_reply': gi.FunctionInfo(send_message_with_reply), 'send_message_with_reply_finish': gi.FunctionInfo(send_message_with_reply_finish), 'send_message_with_reply_sync': gi.FunctionInfo(send_message_with_reply_sync), 'set_exit_on_close': gi.FunctionInfo(set_exit_on_close), 'signal_subscribe': gi.FunctionInfo(signal_subscribe), 'signal_unsubscribe': gi.FunctionInfo(signal_unsubscribe), 'start_message_processing': gi.FunctionInfo(start_message_processing), 'unexport_action_group': gi.FunctionInfo(unexport_action_group), 'unexport_menu_model': gi.FunctionInfo(unexport_menu_model), 'unregister_object': gi.FunctionInfo(unregister_object), 'unregister_subtree': gi.FunctionInfo(unregister_subtree)})"
    __gdoc__ = 'Object GDBusConnection\n\nSignals from GDBusConnection:\n  closed (gboolean, GError)\n\nProperties from GDBusConnection:\n  stream -> GIOStream: stream\n  address -> gchararray: address\n  flags -> GDBusConnectionFlags: flags\n  guid -> gchararray: guid\n  unique-name -> gchararray: unique-name\n  closed -> gboolean: closed\n  exit-on-close -> gboolean: exit-on-close\n  capabilities -> GDBusCapabilityFlags: capabilities\n  authentication-observer -> GDBusAuthObserver: authentication-observer\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDBusConnection (1841878560)>'
    __info__ = ObjectInfo(DBusConnection)


