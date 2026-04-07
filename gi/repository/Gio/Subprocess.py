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


from .Initable import Initable

class Subprocess(__gi_overrides_GObject.Object, Initable):
    """
    :Constructors:
    
    ::
    
        Subprocess(**properties)
        new(argv:list, flags:Gio.SubprocessFlags) -> Gio.Subprocess
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def communicate(self, stdin_buf=None, cancellable=None): # real signature unknown; restored from __doc__
        """ communicate(self, stdin_buf:GLib.Bytes=None, cancellable:Gio.Cancellable=None) -> bool, stdout_buf:GLib.Bytes, stderr_buf:GLib.Bytes """
        return False

    def communicate_async(self, stdin_buf=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ communicate_async(self, stdin_buf:GLib.Bytes=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def communicate_finish(self, result): # real signature unknown; restored from __doc__
        """ communicate_finish(self, result:Gio.AsyncResult) -> bool, stdout_buf:GLib.Bytes, stderr_buf:GLib.Bytes """
        return False

    def communicate_utf8(self, stdin_buf=None, cancellable=None): # real signature unknown; restored from __doc__
        """ communicate_utf8(self, stdin_buf:str=None, cancellable:Gio.Cancellable=None) -> bool, stdout_buf:str, stderr_buf:str """
        return False

    def communicate_utf8_async(self, stdin_buf=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ communicate_utf8_async(self, stdin_buf:str=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def communicate_utf8_finish(self, result): # real signature unknown; restored from __doc__
        """ communicate_utf8_finish(self, result:Gio.AsyncResult) -> bool, stdout_buf:str, stderr_buf:str """
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

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_exit(self): # real signature unknown; restored from __doc__
        """ force_exit(self) """
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

    def get_exit_status(self): # real signature unknown; restored from __doc__
        """ get_exit_status(self) -> int """
        return 0

    def get_identifier(self): # real signature unknown; restored from __doc__
        """ get_identifier(self) -> str or None """
        return ""

    def get_if_exited(self): # real signature unknown; restored from __doc__
        """ get_if_exited(self) -> bool """
        return False

    def get_if_signaled(self): # real signature unknown; restored from __doc__
        """ get_if_signaled(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_status(self): # real signature unknown; restored from __doc__
        """ get_status(self) -> int """
        return 0

    def get_stderr_pipe(self): # real signature unknown; restored from __doc__
        """ get_stderr_pipe(self) -> Gio.InputStream or None """
        pass

    def get_stdin_pipe(self): # real signature unknown; restored from __doc__
        """ get_stdin_pipe(self) -> Gio.OutputStream or None """
        pass

    def get_stdout_pipe(self): # real signature unknown; restored from __doc__
        """ get_stdout_pipe(self) -> Gio.InputStream or None """
        pass

    def get_successful(self): # real signature unknown; restored from __doc__
        """ get_successful(self) -> bool """
        return False

    def get_term_sig(self): # real signature unknown; restored from __doc__
        """ get_term_sig(self) -> int """
        return 0

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
    def new(cls, argv, flags): # real signature unknown; restored from __doc__
        """ new(argv:list, flags:Gio.SubprocessFlags) -> Gio.Subprocess """
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

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def wait(self, cancellable=None): # real signature unknown; restored from __doc__
        """ wait(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def wait_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wait_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wait_check(self, cancellable=None): # real signature unknown; restored from __doc__
        """ wait_check(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def wait_check_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ wait_check_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def wait_check_finish(self, result): # real signature unknown; restored from __doc__
        """ wait_check_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def wait_finish(self, result): # real signature unknown; restored from __doc__
        """ wait_finish(self, result:Gio.AsyncResult) -> bool """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea7086b640>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Subprocess), '__module__': 'gi.repository.Gio', '__gtype__': <GType GSubprocess (1841605712)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'communicate': gi.FunctionInfo(communicate), 'communicate_async': gi.FunctionInfo(communicate_async), 'communicate_finish': gi.FunctionInfo(communicate_finish), 'communicate_utf8': gi.FunctionInfo(communicate_utf8), 'communicate_utf8_async': gi.FunctionInfo(communicate_utf8_async), 'communicate_utf8_finish': gi.FunctionInfo(communicate_utf8_finish), 'force_exit': gi.FunctionInfo(force_exit), 'get_exit_status': gi.FunctionInfo(get_exit_status), 'get_identifier': gi.FunctionInfo(get_identifier), 'get_if_exited': gi.FunctionInfo(get_if_exited), 'get_if_signaled': gi.FunctionInfo(get_if_signaled), 'get_status': gi.FunctionInfo(get_status), 'get_stderr_pipe': gi.FunctionInfo(get_stderr_pipe), 'get_stdin_pipe': gi.FunctionInfo(get_stdin_pipe), 'get_stdout_pipe': gi.FunctionInfo(get_stdout_pipe), 'get_successful': gi.FunctionInfo(get_successful), 'get_term_sig': gi.FunctionInfo(get_term_sig), 'wait': gi.FunctionInfo(wait), 'wait_async': gi.FunctionInfo(wait_async), 'wait_check': gi.FunctionInfo(wait_check), 'wait_check_async': gi.FunctionInfo(wait_check_async), 'wait_check_finish': gi.FunctionInfo(wait_check_finish), 'wait_finish': gi.FunctionInfo(wait_finish)})"
    __gdoc__ = 'Object GSubprocess\n\nProperties from GSubprocess:\n  flags -> GSubprocessFlags: flags\n  argv -> GStrv: argv\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GSubprocess (1841605712)>'
    __info__ = ObjectInfo(Subprocess)


