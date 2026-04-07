# encoding: utf-8
# module gi.repository.Gdk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gi._gi as __gi__gi
import gobject as __gobject


class Display(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Display(**properties)
    """
    def beep(self): # real signature unknown; restored from __doc__
        """ beep(self) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
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

    def device_is_grabbed(self, device): # real signature unknown; restored from __doc__
        """ device_is_grabbed(self, device:Gdk.Device) -> bool """
        return False

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

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
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

    def get_app_launch_context(self): # real signature unknown; restored from __doc__
        """ get_app_launch_context(self) -> Gdk.AppLaunchContext """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gdk.Display or None """
        pass

    def get_default_cursor_size(self): # real signature unknown; restored from __doc__
        """ get_default_cursor_size(self) -> int """
        return 0

    def get_default_group(self): # real signature unknown; restored from __doc__
        """ get_default_group(self) -> Gdk.Window """
        pass

    def get_default_screen(self): # real signature unknown; restored from __doc__
        """ get_default_screen(self) -> Gdk.Screen """
        pass

    def get_default_seat(self): # real signature unknown; restored from __doc__
        """ get_default_seat(self) -> Gdk.Seat """
        pass

    def get_device_manager(self): # real signature unknown; restored from __doc__
        """ get_device_manager(self) -> Gdk.DeviceManager or None """
        pass

    def get_event(self): # real signature unknown; restored from __doc__
        """ get_event(self) -> Gdk.Event or None """
        pass

    def get_maximal_cursor_size(self): # real signature unknown; restored from __doc__
        """ get_maximal_cursor_size(self) -> width:int, height:int """
        pass

    def get_monitor(self, monitor_num): # real signature unknown; restored from __doc__
        """ get_monitor(self, monitor_num:int) -> Gdk.Monitor or None """
        pass

    def get_monitor_at_point(self, x, y): # real signature unknown; restored from __doc__
        """ get_monitor_at_point(self, x:int, y:int) -> Gdk.Monitor """
        pass

    def get_monitor_at_window(self, window): # real signature unknown; restored from __doc__
        """ get_monitor_at_window(self, window:Gdk.Window) -> Gdk.Monitor """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_monitors(self): # real signature unknown; restored from __doc__
        """ get_n_monitors(self) -> int """
        return 0

    def get_n_screens(self): # real signature unknown; restored from __doc__
        """ get_n_screens(self) -> int """
        return 0

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> screen:Gdk.Screen, x:int, y:int, mask:Gdk.ModifierType """
        pass

    def get_primary_monitor(self): # real signature unknown; restored from __doc__
        """ get_primary_monitor(self) -> Gdk.Monitor or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_screen(self, screen_num): # real signature unknown; restored from __doc__
        """ get_screen(self, screen_num:int) -> Gdk.Screen """
        pass

    def get_window_at_pointer(self): # real signature unknown; restored from __doc__
        """ get_window_at_pointer(self) -> Gdk.Window or None, win_x:int, win_y:int """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def keyboard_ungrab(self, time_): # real signature unknown; restored from __doc__
        """ keyboard_ungrab(self, time_:int) """
        pass

    def list_devices(self): # real signature unknown; restored from __doc__
        """ list_devices(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_seats(self): # real signature unknown; restored from __doc__
        """ list_seats(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def notify_startup_complete(self, startup_id): # real signature unknown; restored from __doc__
        """ notify_startup_complete(self, startup_id:str) """
        pass

    def open(self, display_name): # real signature unknown; restored from __doc__
        """ open(display_name:str) -> Gdk.Display or None """
        pass

    def open_default_libgtk_only(self): # real signature unknown; restored from __doc__
        """ open_default_libgtk_only() -> Gdk.Display or None """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_event(self): # real signature unknown; restored from __doc__
        """ peek_event(self) -> Gdk.Event or None """
        pass

    def pointer_is_grabbed(self): # real signature unknown; restored from __doc__
        """ pointer_is_grabbed(self) -> bool """
        return False

    def pointer_ungrab(self, time_): # real signature unknown; restored from __doc__
        """ pointer_ungrab(self, time_:int) """
        pass

    def put_event(self, event): # real signature unknown; restored from __doc__
        """ put_event(self, event:Gdk.Event) """
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

    def request_selection_notification(self, selection): # real signature unknown; restored from __doc__
        """ request_selection_notification(self, selection:Gdk.Atom) -> bool """
        return False

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_double_click_distance(self, distance): # real signature unknown; restored from __doc__
        """ set_double_click_distance(self, distance:int) """
        pass

    def set_double_click_time(self, msec): # real signature unknown; restored from __doc__
        """ set_double_click_time(self, msec:int) """
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

    def store_clipboard(self, clipboard_window, time_, targets=None): # real signature unknown; restored from __doc__
        """ store_clipboard(self, clipboard_window:Gdk.Window, time_:int, targets:list=None) """
        pass

    def supports_clipboard_persistence(self): # real signature unknown; restored from __doc__
        """ supports_clipboard_persistence(self) -> bool """
        return False

    def supports_composite(self): # real signature unknown; restored from __doc__
        """ supports_composite(self) -> bool """
        return False

    def supports_cursor_alpha(self): # real signature unknown; restored from __doc__
        """ supports_cursor_alpha(self) -> bool """
        return False

    def supports_cursor_color(self): # real signature unknown; restored from __doc__
        """ supports_cursor_color(self) -> bool """
        return False

    def supports_input_shapes(self): # real signature unknown; restored from __doc__
        """ supports_input_shapes(self) -> bool """
        return False

    def supports_selection_notification(self): # real signature unknown; restored from __doc__
        """ supports_selection_notification(self) -> bool """
        return False

    def supports_shapes(self): # real signature unknown; restored from __doc__
        """ supports_shapes(self) -> bool """
        return False

    def sync(self): # real signature unknown; restored from __doc__
        """ sync(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def warp_pointer(self, screen, x, y): # real signature unknown; restored from __doc__
        """ warp_pointer(self, screen:Gdk.Screen, x:int, y:int) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001872539b670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Display), '__module__': 'gi.repository.Gdk', '__gtype__': <GType GdkDisplay (585158304)>, '__doc__': None, '__gsignals__': {}, 'get_default': <staticmethod(gi.FunctionInfo(get_default))>, 'open': <staticmethod(gi.FunctionInfo(open))>, 'open_default_libgtk_only': <staticmethod(gi.FunctionInfo(open_default_libgtk_only))>, 'beep': gi.FunctionInfo(beep), 'close': gi.FunctionInfo(close), 'device_is_grabbed': gi.FunctionInfo(device_is_grabbed), 'flush': gi.FunctionInfo(flush), 'get_app_launch_context': gi.FunctionInfo(get_app_launch_context), 'get_default_cursor_size': gi.FunctionInfo(get_default_cursor_size), 'get_default_group': gi.FunctionInfo(get_default_group), 'get_default_screen': gi.FunctionInfo(get_default_screen), 'get_default_seat': gi.FunctionInfo(get_default_seat), 'get_device_manager': gi.FunctionInfo(get_device_manager), 'get_event': gi.FunctionInfo(get_event), 'get_maximal_cursor_size': gi.FunctionInfo(get_maximal_cursor_size), 'get_monitor': gi.FunctionInfo(get_monitor), 'get_monitor_at_point': gi.FunctionInfo(get_monitor_at_point), 'get_monitor_at_window': gi.FunctionInfo(get_monitor_at_window), 'get_n_monitors': gi.FunctionInfo(get_n_monitors), 'get_n_screens': gi.FunctionInfo(get_n_screens), 'get_name': gi.FunctionInfo(get_name), 'get_pointer': gi.FunctionInfo(get_pointer), 'get_primary_monitor': gi.FunctionInfo(get_primary_monitor), 'get_screen': gi.FunctionInfo(get_screen), 'get_window_at_pointer': gi.FunctionInfo(get_window_at_pointer), 'has_pending': gi.FunctionInfo(has_pending), 'is_closed': gi.FunctionInfo(is_closed), 'keyboard_ungrab': gi.FunctionInfo(keyboard_ungrab), 'list_devices': gi.FunctionInfo(list_devices), 'list_seats': gi.FunctionInfo(list_seats), 'notify_startup_complete': gi.FunctionInfo(notify_startup_complete), 'peek_event': gi.FunctionInfo(peek_event), 'pointer_is_grabbed': gi.FunctionInfo(pointer_is_grabbed), 'pointer_ungrab': gi.FunctionInfo(pointer_ungrab), 'put_event': gi.FunctionInfo(put_event), 'request_selection_notification': gi.FunctionInfo(request_selection_notification), 'set_double_click_distance': gi.FunctionInfo(set_double_click_distance), 'set_double_click_time': gi.FunctionInfo(set_double_click_time), 'store_clipboard': gi.FunctionInfo(store_clipboard), 'supports_clipboard_persistence': gi.FunctionInfo(supports_clipboard_persistence), 'supports_composite': gi.FunctionInfo(supports_composite), 'supports_cursor_alpha': gi.FunctionInfo(supports_cursor_alpha), 'supports_cursor_color': gi.FunctionInfo(supports_cursor_color), 'supports_input_shapes': gi.FunctionInfo(supports_input_shapes), 'supports_selection_notification': gi.FunctionInfo(supports_selection_notification), 'supports_shapes': gi.FunctionInfo(supports_shapes), 'sync': gi.FunctionInfo(sync), 'warp_pointer': gi.FunctionInfo(warp_pointer)})"
    __gdoc__ = 'Object GdkDisplay\n\nSignals from GdkDisplay:\n  opened ()\n  closed (gboolean)\n  seat-added (GdkSeat)\n  seat-removed (GdkSeat)\n  monitor-added (GdkMonitor)\n  monitor-removed (GdkMonitor)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdkDisplay (585158304)>'
    __info__ = ObjectInfo(Display)


