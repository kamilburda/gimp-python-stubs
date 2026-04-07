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


from .FilterOutputStream import FilterOutputStream

from .Seekable import Seekable

class DataOutputStream(FilterOutputStream, Seekable):
    """
    :Constructors:
    
    ::
    
        DataOutputStream(**properties)
        new(base_stream:Gio.OutputStream) -> Gio.DataOutputStream
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_seek(self): # real signature unknown; restored from __doc__
        """ can_seek(self) -> bool """
        return False

    def can_truncate(self): # real signature unknown; restored from __doc__
        """ can_truncate(self) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_pending(self): # real signature unknown; restored from __doc__
        """ clear_pending(self) """
        pass

    def close(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def close_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, result): # real signature unknown; restored from __doc__
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
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

    def do_close_async(self, *args, **kwargs): # real signature unknown
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_close_finish(self, *args, **kwargs): # real signature unknown
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_close_fn(self, *args, **kwargs): # real signature unknown
        """ close_fn(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_flush(self, *args, **kwargs): # real signature unknown
        """ flush(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_flush_async(self, *args, **kwargs): # real signature unknown
        """ flush_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_flush_finish(self, *args, **kwargs): # real signature unknown
        """ flush_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_splice(self, *args, **kwargs): # real signature unknown
        """ splice(self, source:Gio.InputStream, flags:Gio.OutputStreamSpliceFlags, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_splice_async(self, *args, **kwargs): # real signature unknown
        """ splice_async(self, source:Gio.InputStream, flags:Gio.OutputStreamSpliceFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_splice_finish(self, *args, **kwargs): # real signature unknown
        """ splice_finish(self, result:Gio.AsyncResult) -> int """
        pass

    def do_writev_async(self, *args, **kwargs): # real signature unknown
        """ writev_async(self, vectors:list, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_writev_finish(self, *args, **kwargs): # real signature unknown
        """ writev_finish(self, result:Gio.AsyncResult) -> bool, bytes_written:int """
        pass

    def do_writev_fn(self, *args, **kwargs): # real signature unknown
        """ writev_fn(self, vectors:list, cancellable:Gio.Cancellable=None) -> bool, bytes_written:int """
        pass

    def do_write_async(self, *args, **kwargs): # real signature unknown
        """ write_async(self, buffer:list=None, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_write_finish(self, *args, **kwargs): # real signature unknown
        """ write_finish(self, result:Gio.AsyncResult) -> int """
        pass

    def do_write_fn(self, *args, **kwargs): # real signature unknown
        """ write_fn(self, buffer:list=None, cancellable:Gio.Cancellable=None) -> int """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self, cancellable=None): # real signature unknown; restored from __doc__
        """ flush(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def flush_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ flush_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def flush_finish(self, result): # real signature unknown; restored from __doc__
        """ flush_finish(self, result:Gio.AsyncResult) -> bool """
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

    def get_base_stream(self): # real signature unknown; restored from __doc__
        """ get_base_stream(self) -> Gio.OutputStream """
        pass

    def get_byte_order(self): # real signature unknown; restored from __doc__
        """ get_byte_order(self) -> Gio.DataStreamByteOrder """
        pass

    def get_close_base_stream(self): # real signature unknown; restored from __doc__
        """ get_close_base_stream(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def has_pending(self): # real signature unknown; restored from __doc__
        """ has_pending(self) -> bool """
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

    def is_closing(self): # real signature unknown; restored from __doc__
        """ is_closing(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls, base_stream): # real signature unknown; restored from __doc__
        """ new(base_stream:Gio.OutputStream) -> Gio.DataOutputStream """
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

    def put_byte(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_byte(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_int16(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_int16(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_int32(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_int32(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_int64(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_int64(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_string(self, p_str, cancellable=None): # real signature unknown; restored from __doc__
        """ put_string(self, str:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_uint16(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_uint16(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_uint32(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_uint32(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def put_uint64(self, data, cancellable=None): # real signature unknown; restored from __doc__
        """ put_uint64(self, data:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def seek(self, offset, type, cancellable=None): # real signature unknown; restored from __doc__
        """ seek(self, offset:int, type:GLib.SeekType, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_byte_order(self, order): # real signature unknown; restored from __doc__
        """ set_byte_order(self, order:Gio.DataStreamByteOrder) """
        pass

    def set_close_base_stream(self, close_base): # real signature unknown; restored from __doc__
        """ set_close_base_stream(self, close_base:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_pending(self): # real signature unknown; restored from __doc__
        """ set_pending(self) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def splice(self, source, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ splice(self, source:Gio.InputStream, flags:Gio.OutputStreamSpliceFlags, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def splice_async(self, source, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ splice_async(self, source:Gio.InputStream, flags:Gio.OutputStreamSpliceFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def splice_finish(self, result): # real signature unknown; restored from __doc__
        """ splice_finish(self, result:Gio.AsyncResult) -> int """
        return 0

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

    def tell(self): # real signature unknown; restored from __doc__
        """ tell(self) -> int """
        return 0

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def truncate(self, offset, cancellable=None): # real signature unknown; restored from __doc__
        """ truncate(self, offset:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ write(self, buffer:list, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def writev(self, vectors, cancellable=None): # real signature unknown; restored from __doc__
        """ writev(self, vectors:list, cancellable:Gio.Cancellable=None) -> bool, bytes_written:int """
        return False

    def writev_all(self, vectors, cancellable=None): # real signature unknown; restored from __doc__
        """ writev_all(self, vectors:list, cancellable:Gio.Cancellable=None) -> bool, bytes_written:int """
        return False

    def writev_all_async(self, vectors, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ writev_all_async(self, vectors:list, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def writev_all_finish(self, result): # real signature unknown; restored from __doc__
        """ writev_all_finish(self, result:Gio.AsyncResult) -> bool, bytes_written:int """
        return False

    def writev_async(self, vectors, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ writev_async(self, vectors:list, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def writev_finish(self, result): # real signature unknown; restored from __doc__
        """ writev_finish(self, result:Gio.AsyncResult) -> bool, bytes_written:int """
        return False

    def write_all(self, buffer, cancellable=None): # real signature unknown; restored from __doc__
        """ write_all(self, buffer:list, cancellable:Gio.Cancellable=None) -> bool, bytes_written:int """
        return False

    def write_all_async(self, buffer, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_all_async(self, buffer:list, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_all_finish(self, result): # real signature unknown; restored from __doc__
        """ write_all_finish(self, result:Gio.AsyncResult) -> bool, bytes_written:int """
        return False

    def write_async(self, buffer, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_async(self, buffer:list, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_bytes(self, bytes, cancellable=None): # real signature unknown; restored from __doc__
        """ write_bytes(self, bytes:GLib.Bytes, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def write_bytes_async(self, bytes, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ write_bytes_async(self, bytes:GLib.Bytes, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def write_bytes_finish(self, result): # real signature unknown; restored from __doc__
        """ write_bytes_finish(self, result:Gio.AsyncResult) -> int """
        return 0

    def write_finish(self, result): # real signature unknown; restored from __doc__
        """ write_finish(self, result:Gio.AsyncResult) -> int """
        return 0

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

    base_stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea7084bb20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DataOutputStream), '__module__': 'gi.repository.Gio', '__gtype__': <GType GDataOutputStream (1848612608)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'get_byte_order': gi.FunctionInfo(get_byte_order), 'put_byte': gi.FunctionInfo(put_byte), 'put_int16': gi.FunctionInfo(put_int16), 'put_int32': gi.FunctionInfo(put_int32), 'put_int64': gi.FunctionInfo(put_int64), 'put_string': gi.FunctionInfo(put_string), 'put_uint16': gi.FunctionInfo(put_uint16), 'put_uint32': gi.FunctionInfo(put_uint32), 'put_uint64': gi.FunctionInfo(put_uint64), 'set_byte_order': gi.FunctionInfo(set_byte_order), 'parent_instance': <property object at 0x000001ea7096be70>, 'priv': <property object at 0x000001ea7096bf60>})"
    __gdoc__ = 'Object GDataOutputStream\n\nProperties from GDataOutputStream:\n  byte-order -> GDataStreamByteOrder: byte-order\n\nProperties from GFilterOutputStream:\n  base-stream -> GOutputStream: base-stream\n  close-base-stream -> gboolean: close-base-stream\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GDataOutputStream (1848612608)>'
    __info__ = ObjectInfo(DataOutputStream)


