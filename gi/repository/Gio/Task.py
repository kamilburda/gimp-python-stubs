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


from .AsyncResult import AsyncResult

class Task(__gi_overrides_GObject.Object, AsyncResult):
    """
    :Constructors:
    
    ::
    
        Task(**properties)
        new(source_object:GObject.Object=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, callback_data=None) -> Gio.Task
    """
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

    def get_cancellable(self): # real signature unknown; restored from __doc__
        """ get_cancellable(self) -> Gio.Cancellable or None """
        pass

    def get_check_cancellable(self): # real signature unknown; restored from __doc__
        """ get_check_cancellable(self) -> bool """
        return False

    def get_completed(self): # real signature unknown; restored from __doc__
        """ get_completed(self) -> bool """
        return False

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> GLib.MainContext """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str or None """
        return ""

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_return_on_cancel(self): # real signature unknown; restored from __doc__
        """ get_return_on_cancel(self) -> bool """
        return False

    def get_source_object(self): # real signature unknown; restored from __doc__
        """ get_source_object(self) -> GObject.Object or None """
        pass

    def get_source_tag(self): # real signature unknown; restored from __doc__
        """ get_source_tag(self) """
        pass

    def get_task_data(self): # real signature unknown; restored from __doc__
        """ get_task_data(self) """
        pass

    def get_user_data(self): # real signature unknown; restored from __doc__
        """ get_user_data(self) """
        pass

    def had_error(self): # real signature unknown; restored from __doc__
        """ had_error(self) -> bool """
        return False

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

    def is_tagged(self, source_tag=None): # real signature unknown; restored from __doc__
        """ is_tagged(self, source_tag=None) -> bool """
        return False

    def is_valid(self, result, source_object=None): # real signature unknown; restored from __doc__
        """ is_valid(result:Gio.AsyncResult, source_object:GObject.Object=None) -> bool """
        return False

    def legacy_propagate_error(self): # real signature unknown; restored from __doc__
        """ legacy_propagate_error(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls, source_object=None, cancellable=None, callback=None, callback_data=None): # real signature unknown; restored from __doc__
        """ new(source_object:GObject.Object=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, callback_data=None) -> Gio.Task """
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

    def propagate_boolean(self): # real signature unknown; restored from __doc__
        """ propagate_boolean(self) -> bool """
        return False

    def propagate_int(self): # real signature unknown; restored from __doc__
        """ propagate_int(self) -> int """
        return 0

    def propagate_pointer(self): # real signature unknown; restored from __doc__
        """ propagate_pointer(self) """
        pass

    def propagate_value(self): # real signature unknown; restored from __doc__
        """ propagate_value(self) -> bool, value:GObject.Value """
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

    def report_error(self, source_object=None, callback=None, callback_data=None, source_tag=None, error): # real signature unknown; restored from __doc__
        """ report_error(source_object:GObject.Object=None, callback:Gio.AsyncReadyCallback=None, callback_data=None, source_tag=None, error:error) """
        pass

    def return_boolean(self, result): # real signature unknown; restored from __doc__
        """ return_boolean(self, result:bool) """
        pass

    def return_error(self, error): # real signature unknown; restored from __doc__
        """ return_error(self, error:error) """
        pass

    def return_error_if_cancelled(self): # real signature unknown; restored from __doc__
        """ return_error_if_cancelled(self) -> bool """
        return False

    def return_int(self, result): # real signature unknown; restored from __doc__
        """ return_int(self, result:int) """
        pass

    def return_new_error_literal(self, domain, code, message): # real signature unknown; restored from __doc__
        """ return_new_error_literal(self, domain:int, code:int, message:str) """
        pass

    def return_pointer(self, result=None, result_destroy=None): # real signature unknown; restored from __doc__
        """ return_pointer(self, result=None, result_destroy:GLib.DestroyNotify=None) """
        pass

    def return_value(self, result=None): # real signature unknown; restored from __doc__
        """ return_value(self, result:GObject.Value=None) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def run_in_thread(self, task_func): # real signature unknown; restored from __doc__
        """ run_in_thread(self, task_func:Gio.TaskThreadFunc) """
        pass

    def run_in_thread_sync(self, task_func): # real signature unknown; restored from __doc__
        """ run_in_thread_sync(self, task_func:Gio.TaskThreadFunc) """
        pass

    def set_check_cancellable(self, check_cancellable): # real signature unknown; restored from __doc__
        """ set_check_cancellable(self, check_cancellable:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) """
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_return_on_cancel(self, return_on_cancel): # real signature unknown; restored from __doc__
        """ set_return_on_cancel(self, return_on_cancel:bool) -> bool """
        return False

    def set_source_tag(self, source_tag=None): # real signature unknown; restored from __doc__
        """ set_source_tag(self, source_tag=None) """
        pass

    def set_static_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_static_name(self, name:str=None) """
        pass

    def set_task_data(self, task_data=None, task_data_destroy=None): # real signature unknown; restored from __doc__
        """ set_task_data(self, task_data=None, task_data_destroy:GLib.DestroyNotify=None) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea7086cac0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Task), '__module__': 'gi.repository.Gio', '__gtype__': <GType GTask (1841606384)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'is_valid': <staticmethod(gi.FunctionInfo(is_valid))>, 'report_error': <staticmethod(gi.FunctionInfo(report_error))>, 'get_cancellable': gi.FunctionInfo(get_cancellable), 'get_check_cancellable': gi.FunctionInfo(get_check_cancellable), 'get_completed': gi.FunctionInfo(get_completed), 'get_context': gi.FunctionInfo(get_context), 'get_name': gi.FunctionInfo(get_name), 'get_priority': gi.FunctionInfo(get_priority), 'get_return_on_cancel': gi.FunctionInfo(get_return_on_cancel), 'get_source_object': gi.FunctionInfo(get_source_object), 'get_source_tag': gi.FunctionInfo(get_source_tag), 'get_task_data': gi.FunctionInfo(get_task_data), 'had_error': gi.FunctionInfo(had_error), 'propagate_boolean': gi.FunctionInfo(propagate_boolean), 'propagate_int': gi.FunctionInfo(propagate_int), 'propagate_pointer': gi.FunctionInfo(propagate_pointer), 'propagate_value': gi.FunctionInfo(propagate_value), 'return_boolean': gi.FunctionInfo(return_boolean), 'return_error': gi.FunctionInfo(return_error), 'return_error_if_cancelled': gi.FunctionInfo(return_error_if_cancelled), 'return_int': gi.FunctionInfo(return_int), 'return_new_error_literal': gi.FunctionInfo(return_new_error_literal), 'return_pointer': gi.FunctionInfo(return_pointer), 'return_value': gi.FunctionInfo(return_value), 'run_in_thread': gi.FunctionInfo(run_in_thread), 'run_in_thread_sync': gi.FunctionInfo(run_in_thread_sync), 'set_check_cancellable': gi.FunctionInfo(set_check_cancellable), 'set_name': gi.FunctionInfo(set_name), 'set_priority': gi.FunctionInfo(set_priority), 'set_return_on_cancel': gi.FunctionInfo(set_return_on_cancel), 'set_source_tag': gi.FunctionInfo(set_source_tag), 'set_static_name': gi.FunctionInfo(set_static_name), 'set_task_data': gi.FunctionInfo(set_task_data)})"
    __gdoc__ = 'Object GTask\n\nProperties from GTask:\n  completed -> gboolean: completed\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GTask (1841606384)>'
    __info__ = ObjectInfo(Task)


