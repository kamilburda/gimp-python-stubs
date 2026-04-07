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


class Device(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Device(**properties)
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

    def get_associated_device(self): # real signature unknown; restored from __doc__
        """ get_associated_device(self) -> Gdk.Device or None """
        pass

    def get_axes(self): # real signature unknown; restored from __doc__
        """ get_axes(self) -> Gdk.AxisFlags """
        pass

    def get_axis_use(self, index_): # real signature unknown; restored from __doc__
        """ get_axis_use(self, index_:int) -> Gdk.AxisUse """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_device_type(self): # real signature unknown; restored from __doc__
        """ get_device_type(self) -> Gdk.DeviceType """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_has_cursor(self): # real signature unknown; restored from __doc__
        """ get_has_cursor(self) -> bool """
        return False

    def get_key(self, index_): # real signature unknown; restored from __doc__
        """ get_key(self, index_:int) -> bool, keyval:int, modifiers:Gdk.ModifierType """
        return False

    def get_last_event_window(self): # real signature unknown; restored from __doc__
        """ get_last_event_window(self) -> Gdk.Window or None """
        pass

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> Gdk.InputMode """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_axes(self): # real signature unknown; restored from __doc__
        """ get_n_axes(self) -> int """
        return 0

    def get_n_keys(self): # real signature unknown; restored from __doc__
        """ get_n_keys(self) -> int """
        return 0

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> screen:Gdk.Screen, x:int, y:int """
        pass

    def get_position_double(self): # real signature unknown; restored from __doc__
        """ get_position_double(self) -> screen:Gdk.Screen, x:float, y:float """
        pass

    def get_product_id(self): # real signature unknown; restored from __doc__
        """ get_product_id(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_seat(self): # real signature unknown; restored from __doc__
        """ get_seat(self) -> Gdk.Seat """
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> Gdk.InputSource """
        pass

    def get_vendor_id(self): # real signature unknown; restored from __doc__
        """ get_vendor_id(self) -> str or None """
        return ""

    def get_window_at_position(self): # real signature unknown; restored from __doc__
        """ get_window_at_position(self) -> Gdk.Window or None, win_x:int, win_y:int """
        pass

    def get_window_at_position_double(self): # real signature unknown; restored from __doc__
        """ get_window_at_position_double(self) -> Gdk.Window or None, win_x:float, win_y:float """
        pass

    def grab(self, window, grab_ownership, owner_events, event_mask, cursor=None, time_): # real signature unknown; restored from __doc__
        """ grab(self, window:Gdk.Window, grab_ownership:Gdk.GrabOwnership, owner_events:bool, event_mask:Gdk.EventMask, cursor:Gdk.Cursor=None, time_:int) -> Gdk.GrabStatus """
        pass

    def grab_info_libgtk_only(self, display, device): # real signature unknown; restored from __doc__
        """ grab_info_libgtk_only(display:Gdk.Display, device:Gdk.Device) -> bool, grab_window:Gdk.Window, owner_events:bool """
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

    def list_axes(self): # real signature unknown; restored from __doc__
        """ list_axes(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_slave_devices(self): # real signature unknown; restored from __doc__
        """ list_slave_devices(self) -> list or None """
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

    def set_axis_use(self, index_, use): # real signature unknown; restored from __doc__
        """ set_axis_use(self, index_:int, use:Gdk.AxisUse) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_key(self, index_, keyval, modifiers): # real signature unknown; restored from __doc__
        """ set_key(self, index_:int, keyval:int, modifiers:Gdk.ModifierType) """
        pass

    def set_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_mode(self, mode:Gdk.InputMode) -> bool """
        return False

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

    def ungrab(self, time_): # real signature unknown; restored from __doc__
        """ ungrab(self, time_:int) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def warp(self, screen, x, y): # real signature unknown; restored from __doc__
        """ warp(self, screen:Gdk.Screen, x:int, y:int) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001872539af80>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Device), '__module__': 'gi.repository.Gdk', '__gtype__': <GType GdkDevice (587202800)>, '__doc__': None, '__gsignals__': {}, 'grab_info_libgtk_only': <staticmethod(gi.FunctionInfo(grab_info_libgtk_only))>, 'get_associated_device': gi.FunctionInfo(get_associated_device), 'get_axes': gi.FunctionInfo(get_axes), 'get_axis_use': gi.FunctionInfo(get_axis_use), 'get_device_type': gi.FunctionInfo(get_device_type), 'get_display': gi.FunctionInfo(get_display), 'get_has_cursor': gi.FunctionInfo(get_has_cursor), 'get_key': gi.FunctionInfo(get_key), 'get_last_event_window': gi.FunctionInfo(get_last_event_window), 'get_mode': gi.FunctionInfo(get_mode), 'get_n_axes': gi.FunctionInfo(get_n_axes), 'get_n_keys': gi.FunctionInfo(get_n_keys), 'get_name': gi.FunctionInfo(get_name), 'get_position': gi.FunctionInfo(get_position), 'get_position_double': gi.FunctionInfo(get_position_double), 'get_product_id': gi.FunctionInfo(get_product_id), 'get_seat': gi.FunctionInfo(get_seat), 'get_source': gi.FunctionInfo(get_source), 'get_vendor_id': gi.FunctionInfo(get_vendor_id), 'get_window_at_position': gi.FunctionInfo(get_window_at_position), 'get_window_at_position_double': gi.FunctionInfo(get_window_at_position_double), 'grab': gi.FunctionInfo(grab), 'list_axes': gi.FunctionInfo(list_axes), 'list_slave_devices': gi.FunctionInfo(list_slave_devices), 'set_axis_use': gi.FunctionInfo(set_axis_use), 'set_key': gi.FunctionInfo(set_key), 'set_mode': gi.FunctionInfo(set_mode), 'ungrab': gi.FunctionInfo(ungrab), 'warp': gi.FunctionInfo(warp)})"
    __gdoc__ = 'Object GdkDevice\n\nSignals from GdkDevice:\n  changed ()\n  tool-changed (GdkDeviceTool)\n\nProperties from GdkDevice:\n  display -> GdkDisplay: Device Display\n    Display which the device belongs to\n  device-manager -> GdkDeviceManager: Device manager\n    Device manager which the device belongs to\n  name -> gchararray: Device name\n    Device name\n  associated-device -> GdkDevice: Associated device\n    Associated pointer or keyboard with this device\n  type -> GdkDeviceType: Device type\n    Device role in the device manager\n  input-source -> GdkInputSource: Input source\n    Source type for the device\n  input-mode -> GdkInputMode: Input mode for the device\n    Input mode for the device\n  has-cursor -> gboolean: Whether the device has a cursor\n    Whether there is a visible cursor following device motion\n  n-axes -> guint: Number of axes in the device\n    Number of axes in the device\n  vendor-id -> gchararray: Vendor ID\n    Vendor ID\n  product-id -> gchararray: Product ID\n    Product ID\n  seat -> GdkSeat: Seat\n    Seat\n  num-touches -> guint: Number of concurrent touches\n    Number of concurrent touches\n  axes -> GdkAxisFlags: Axes\n    Axes\n  tool -> GdkDeviceTool: Tool\n    The tool that is currently used with this device\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdkDevice (587202800)>'
    __info__ = ObjectInfo(Device)


