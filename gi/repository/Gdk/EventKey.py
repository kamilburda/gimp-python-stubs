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


from .EventKey import EventKey

class EventKey(EventKey):
    """
    :Constructors:
    
    ::
    
        EventKey()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gdk.Event """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Gdk.Event or None """
        pass

    def get_axis(*args, **kwargs): # reliably restored by inspect
        """ get_axis(self, axis_use:Gdk.AxisUse) -> bool, value:float """
        pass

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> bool, button:int """
        return False

    def get_click_count(self): # real signature unknown; restored from __doc__
        """ get_click_count(self) -> bool, click_count:int """
        return False

    def get_coords(*args, **kwargs): # reliably restored by inspect
        """ get_coords(self) -> bool, x_win:float, y_win:float """
        pass

    def get_device(self): # real signature unknown; restored from __doc__
        """ get_device(self) -> Gdk.Device or None """
        pass

    def get_device_tool(self): # real signature unknown; restored from __doc__
        """ get_device_tool(self) -> Gdk.DeviceTool """
        pass

    def get_event_sequence(self): # real signature unknown; restored from __doc__
        """ get_event_sequence(self) -> Gdk.EventSequence """
        pass

    def get_event_type(self): # real signature unknown; restored from __doc__
        """ get_event_type(self) -> Gdk.EventType """
        pass

    def get_keycode(self): # real signature unknown; restored from __doc__
        """ get_keycode(self) -> bool, keycode:int """
        return False

    def get_keyval(self): # real signature unknown; restored from __doc__
        """ get_keyval(self) -> bool, keyval:int """
        return False

    def get_pointer_emulated(self): # real signature unknown; restored from __doc__
        """ get_pointer_emulated(self) -> bool """
        return False

    def get_root_coords(*args, **kwargs): # reliably restored by inspect
        """ get_root_coords(self) -> bool, x_root:float, y_root:float """
        pass

    def get_scancode(self): # real signature unknown; restored from __doc__
        """ get_scancode(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_scroll_deltas(self): # real signature unknown; restored from __doc__
        """ get_scroll_deltas(self) -> bool, delta_x:float, delta_y:float """
        return False

    def get_scroll_direction(self): # real signature unknown; restored from __doc__
        """ get_scroll_direction(self) -> bool, direction:Gdk.ScrollDirection """
        return False

    def get_seat(self): # real signature unknown; restored from __doc__
        """ get_seat(self) -> Gdk.Seat """
        pass

    def get_source_device(self): # real signature unknown; restored from __doc__
        """ get_source_device(self) -> Gdk.Device or None """
        pass

    def get_state(*args, **kwargs): # reliably restored by inspect
        """ get_state(self) -> bool, state:Gdk.ModifierType """
        pass

    def get_time(self): # real signature unknown; restored from __doc__
        """ get_time(self) -> int """
        return 0

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window """
        pass

    def handler_set(self, func, data=None): # real signature unknown; restored from __doc__
        """ handler_set(func:Gdk.EventFunc, data=None) """
        pass

    def is_scroll_stop_event(self): # real signature unknown; restored from __doc__
        """ is_scroll_stop_event(self) -> bool """
        return False

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:Gdk.EventType) -> Gdk.Event """
        pass

    def peek(self): # real signature unknown; restored from __doc__
        """ peek() -> Gdk.Event or None """
        pass

    def put(self): # real signature unknown; restored from __doc__
        """ put(self) """
        pass

    def request_motions(self, event): # real signature unknown; restored from __doc__
        """ request_motions(event:Gdk.EventMotion) """
        pass

    def set_device(self, device): # real signature unknown; restored from __doc__
        """ set_device(self, device:Gdk.Device) """
        pass

    def set_device_tool(self, tool=None): # real signature unknown; restored from __doc__
        """ set_device_tool(self, tool:Gdk.DeviceTool=None) """
        pass

    def set_screen(self, screen): # real signature unknown; restored from __doc__
        """ set_screen(self, screen:Gdk.Screen) """
        pass

    def set_source_device(self, device): # real signature unknown; restored from __doc__
        """ set_source_device(self, device:Gdk.Device) """
        pass

    def triggers_context_menu(self): # real signature unknown; restored from __doc__
        """ triggers_context_menu(self) -> bool """
        return False

    def _get_angle(self, event2): # real signature unknown; restored from __doc__
        """ _get_angle(self, event2:Gdk.Event) -> bool, angle:float """
        return False

    def _get_center(self, event2): # real signature unknown; restored from __doc__
        """ _get_center(self, event2:Gdk.Event) -> bool, x:float, y:float """
        return False

    def _get_distance(self, event2): # real signature unknown; restored from __doc__
        """ _get_distance(self, event2:Gdk.Event) -> bool, distance:float """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hardware_keycode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_modifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', '__doc__': None, 'type': <property object at 0x00000187252a9c60>, 'window': <property object at 0x00000187252a9d50>, 'send_event': <property object at 0x00000187252a9e40>, 'time': <property object at 0x00000187252a9f30>, 'state': <property object at 0x00000187252aa020>, 'keyval': <property object at 0x00000187252aa110>, 'length': <property object at 0x00000187252aa200>, 'string': <property object at 0x00000187252aa2f0>, 'hardware_keycode': <property object at 0x00000187252aa3e0>, 'group': <property object at 0x00000187252aa4d0>, 'is_modifier': <property object at 0x00000187252aa5c0>, 'new': <bound method new of <class 'gi.repository.Gdk.Event'>>, '_get_angle': gi.FunctionInfo(_get_angle), '_get_center': gi.FunctionInfo(_get_center), '_get_distance': gi.FunctionInfo(_get_distance), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_axis': <function strip_boolean_result.<locals>.wrapped at 0x00000187252ac720>, 'get_button': gi.FunctionInfo(get_button), 'get_click_count': gi.FunctionInfo(get_click_count), 'get_coords': <function strip_boolean_result.<locals>.wrapped at 0x00000187252ac7c0>, 'get_device': gi.FunctionInfo(get_device), 'get_device_tool': gi.FunctionInfo(get_device_tool), 'get_event_sequence': gi.FunctionInfo(get_event_sequence), 'get_event_type': gi.FunctionInfo(get_event_type), 'get_keycode': gi.FunctionInfo(get_keycode), 'get_keyval': gi.FunctionInfo(get_keyval), 'get_pointer_emulated': gi.FunctionInfo(get_pointer_emulated), 'get_root_coords': <function strip_boolean_result.<locals>.wrapped at 0x00000187252ac860>, 'get_scancode': gi.FunctionInfo(get_scancode), 'get_screen': gi.FunctionInfo(get_screen), 'get_scroll_deltas': gi.FunctionInfo(get_scroll_deltas), 'get_scroll_direction': gi.FunctionInfo(get_scroll_direction), 'get_seat': gi.FunctionInfo(get_seat), 'get_source_device': gi.FunctionInfo(get_source_device), 'get_state': <function strip_boolean_result.<locals>.wrapped at 0x00000187252ac900>, 'get_time': gi.FunctionInfo(get_time), 'get_window': gi.FunctionInfo(get_window), 'is_scroll_stop_event': gi.FunctionInfo(is_scroll_stop_event), 'put': gi.FunctionInfo(put), 'set_device': gi.FunctionInfo(set_device), 'set_device_tool': gi.FunctionInfo(set_device_tool), 'set_screen': gi.FunctionInfo(set_screen), 'set_source_device': gi.FunctionInfo(set_source_device), 'triggers_context_menu': gi.FunctionInfo(triggers_context_menu), 'get': gi.FunctionInfo(get), 'handler_set': gi.FunctionInfo(handler_set), 'peek': gi.FunctionInfo(peek), 'request_motions': gi.FunctionInfo(request_motions)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(EventKey)


