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


class DBusMessage(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        DBusMessage(**properties)
        new() -> Gio.DBusMessage
        new_from_blob(blob:list, capabilities:Gio.DBusCapabilityFlags) -> Gio.DBusMessage
        new_method_call(name:str=None, path:str, interface_:str=None, method:str) -> Gio.DBusMessage
        new_signal(path:str, interface_:str, signal:str) -> Gio.DBusMessage
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bytes_needed(self, blob): # real signature unknown; restored from __doc__
        """ bytes_needed(blob:list) -> int """
        return 0

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gio.DBusMessage """
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

    def get_arg0(self): # real signature unknown; restored from __doc__
        """ get_arg0(self) -> str or None """
        return ""

    def get_arg0_path(self): # real signature unknown; restored from __doc__
        """ get_arg0_path(self) -> str or None """
        return ""

    def get_body(self): # real signature unknown; restored from __doc__
        """ get_body(self) -> GLib.Variant or None """
        pass

    def get_byte_order(self): # real signature unknown; restored from __doc__
        """ get_byte_order(self) -> Gio.DBusMessageByteOrder """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_destination(self): # real signature unknown; restored from __doc__
        """ get_destination(self) -> str or None """
        return ""

    def get_error_name(self): # real signature unknown; restored from __doc__
        """ get_error_name(self) -> str or None """
        return ""

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.DBusMessageFlags """
        pass

    def get_header(self, header_field): # real signature unknown; restored from __doc__
        """ get_header(self, header_field:Gio.DBusMessageHeaderField) -> GLib.Variant or None """
        pass

    def get_header_fields(self): # real signature unknown; restored from __doc__
        """ get_header_fields(self) -> list """
        return []

    def get_interface(self): # real signature unknown; restored from __doc__
        """ get_interface(self) -> str or None """
        return ""

    def get_locked(self): # real signature unknown; restored from __doc__
        """ get_locked(self) -> bool """
        return False

    def get_member(self): # real signature unknown; restored from __doc__
        """ get_member(self) -> str or None """
        return ""

    def get_message_type(self): # real signature unknown; restored from __doc__
        """ get_message_type(self) -> Gio.DBusMessageType """
        pass

    def get_num_unix_fds(self): # real signature unknown; restored from __doc__
        """ get_num_unix_fds(self) -> int """
        return 0

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reply_serial(self): # real signature unknown; restored from __doc__
        """ get_reply_serial(self) -> int """
        return 0

    def get_sender(self): # real signature unknown; restored from __doc__
        """ get_sender(self) -> str or None """
        return ""

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> int """
        return 0

    def get_signature(self): # real signature unknown; restored from __doc__
        """ get_signature(self) -> str """
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

    def lock(self): # real signature unknown; restored from __doc__
        """ lock(self) """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gio.DBusMessage """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_from_blob(cls, blob, capabilities): # real signature unknown; restored from __doc__
        """ new_from_blob(blob:list, capabilities:Gio.DBusCapabilityFlags) -> Gio.DBusMessage """
        pass

    @classmethod
    def new_method_call(cls, name=None, path, interface_=None, method): # real signature unknown; restored from __doc__
        """ new_method_call(name:str=None, path:str, interface_:str=None, method:str) -> Gio.DBusMessage """
        pass

    def new_method_error_literal(self, error_name, error_message): # real signature unknown; restored from __doc__
        """ new_method_error_literal(self, error_name:str, error_message:str) -> Gio.DBusMessage """
        pass

    def new_method_reply(self): # real signature unknown; restored from __doc__
        """ new_method_reply(self) -> Gio.DBusMessage """
        pass

    @classmethod
    def new_signal(cls, path, interface_, signal): # real signature unknown; restored from __doc__
        """ new_signal(path:str, interface_:str, signal:str) -> Gio.DBusMessage """
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

    def print_(self, indent): # real signature unknown; restored from __doc__
        """ print_(self, indent:int) -> str """
        return ""

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

    def set_body(self, body): # real signature unknown; restored from __doc__
        """ set_body(self, body:GLib.Variant) """
        pass

    def set_byte_order(self, byte_order): # real signature unknown; restored from __doc__
        """ set_byte_order(self, byte_order:Gio.DBusMessageByteOrder) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_destination(self, value=None): # real signature unknown; restored from __doc__
        """ set_destination(self, value:str=None) """
        pass

    def set_error_name(self, value): # real signature unknown; restored from __doc__
        """ set_error_name(self, value:str) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Gio.DBusMessageFlags) """
        pass

    def set_header(self, header_field, value=None): # real signature unknown; restored from __doc__
        """ set_header(self, header_field:Gio.DBusMessageHeaderField, value:GLib.Variant=None) """
        pass

    def set_interface(self, value=None): # real signature unknown; restored from __doc__
        """ set_interface(self, value:str=None) """
        pass

    def set_member(self, value=None): # real signature unknown; restored from __doc__
        """ set_member(self, value:str=None) """
        pass

    def set_message_type(self, type): # real signature unknown; restored from __doc__
        """ set_message_type(self, type:Gio.DBusMessageType) """
        pass

    def set_num_unix_fds(self, value): # real signature unknown; restored from __doc__
        """ set_num_unix_fds(self, value:int) """
        pass

    def set_path(self, value=None): # real signature unknown; restored from __doc__
        """ set_path(self, value:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reply_serial(self, value): # real signature unknown; restored from __doc__
        """ set_reply_serial(self, value:int) """
        pass

    def set_sender(self, value=None): # real signature unknown; restored from __doc__
        """ set_sender(self, value:str=None) """
        pass

    def set_serial(self, serial): # real signature unknown; restored from __doc__
        """ set_serial(self, serial:int) """
        pass

    def set_signature(self, value=None): # real signature unknown; restored from __doc__
        """ set_signature(self, value:str=None) """
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

    def to_blob(self, capabilities): # real signature unknown; restored from __doc__
        """ to_blob(self, capabilities:Gio.DBusCapabilityFlags) -> list """
        return []

    def to_gerror(self): # real signature unknown; restored from __doc__
        """ to_gerror(self) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea708486d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DBusMessage), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDBusMessage (1841874720)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_blob': <classmethod(gi.FunctionInfo(new_from_blob))>, 'new_method_call': <classmethod(gi.FunctionInfo(new_method_call))>, 'new_signal': <classmethod(gi.FunctionInfo(new_signal))>, 'bytes_needed': <staticmethod(gi.FunctionInfo(bytes_needed))>, 'copy': gi.FunctionInfo(copy), 'get_arg0': gi.FunctionInfo(get_arg0), 'get_arg0_path': gi.FunctionInfo(get_arg0_path), 'get_body': gi.FunctionInfo(get_body), 'get_byte_order': gi.FunctionInfo(get_byte_order), 'get_destination': gi.FunctionInfo(get_destination), 'get_error_name': gi.FunctionInfo(get_error_name), 'get_flags': gi.FunctionInfo(get_flags), 'get_header': gi.FunctionInfo(get_header), 'get_header_fields': gi.FunctionInfo(get_header_fields), 'get_interface': gi.FunctionInfo(get_interface), 'get_locked': gi.FunctionInfo(get_locked), 'get_member': gi.FunctionInfo(get_member), 'get_message_type': gi.FunctionInfo(get_message_type), 'get_num_unix_fds': gi.FunctionInfo(get_num_unix_fds), 'get_path': gi.FunctionInfo(get_path), 'get_reply_serial': gi.FunctionInfo(get_reply_serial), 'get_sender': gi.FunctionInfo(get_sender), 'get_serial': gi.FunctionInfo(get_serial), 'get_signature': gi.FunctionInfo(get_signature), 'lock': gi.FunctionInfo(lock), 'new_method_error_literal': gi.FunctionInfo(new_method_error_literal), 'new_method_reply': gi.FunctionInfo(new_method_reply), 'print_': gi.FunctionInfo(print), 'set_body': gi.FunctionInfo(set_body), 'set_byte_order': gi.FunctionInfo(set_byte_order), 'set_destination': gi.FunctionInfo(set_destination), 'set_error_name': gi.FunctionInfo(set_error_name), 'set_flags': gi.FunctionInfo(set_flags), 'set_header': gi.FunctionInfo(set_header), 'set_interface': gi.FunctionInfo(set_interface), 'set_member': gi.FunctionInfo(set_member), 'set_message_type': gi.FunctionInfo(set_message_type), 'set_num_unix_fds': gi.FunctionInfo(set_num_unix_fds), 'set_path': gi.FunctionInfo(set_path), 'set_reply_serial': gi.FunctionInfo(set_reply_serial), 'set_sender': gi.FunctionInfo(set_sender), 'set_serial': gi.FunctionInfo(set_serial), 'set_signature': gi.FunctionInfo(set_signature), 'to_blob': gi.FunctionInfo(to_blob), 'to_gerror': gi.FunctionInfo(to_gerror)})"
    __gdoc__ = 'Object GDBusMessage\n\nProperties from GDBusMessage:\n  locked -> gboolean: locked\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDBusMessage (1841874720)>'
    __info__ = ObjectInfo(DBusMessage)


