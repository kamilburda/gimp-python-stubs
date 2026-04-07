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


from .Event import Event

class Event(Event):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gdk.Event """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get(self): # real signature unknown; restored from __doc__
        """ get() -> Gdk.Event or None """
        pass

    def get_axis(self, axis_use): # real signature unknown; restored from __doc__
        """ get_axis(self, axis_use:Gdk.AxisUse) -> bool, value:float """
        return False

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> bool, button:int """
        return False

    def get_click_count(self): # real signature unknown; restored from __doc__
        """ get_click_count(self) -> bool, click_count:int """
        return False

    def get_coords(self): # real signature unknown; restored from __doc__
        """ get_coords(self) -> bool, x_win:float, y_win:float """
        return False

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

    def get_root_coords(self): # real signature unknown; restored from __doc__
        """ get_root_coords(self) -> bool, x_root:float, y_root:float """
        return False

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

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> bool, state:Gdk.ModifierType """
        return False

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

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

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

    def __getattr__(self, name): # reliably restored by inspect
        # no doc
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

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, name, value): # reliably restored by inspect
        # no doc
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

    any = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    crossing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    expose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    focus_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    grab_broken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    motion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner_change = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad_group_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    proximity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scroll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    setting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_pinch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    touchpad_swipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _UNION_MEMBERS = {
        <EventType.DELETE: 0>: 'any',
        <EventType.DESTROY: 1>: 'any',
        <EventType.EXPOSE: 2>: 'expose',
        <EventType.MOTION_NOTIFY: 3>: 'motion',
        <EventType.BUTTON_PRESS: 4>: 'button',
        <EventType.2BUTTON_PRESS: 5>: 'button',
        <EventType.3BUTTON_PRESS: 6>: 'button',
        <EventType.BUTTON_RELEASE: 7>: 'button',
        <EventType.KEY_PRESS: 8>: 'key',
        <EventType.KEY_RELEASE: 9>: 'key',
        <EventType.ENTER_NOTIFY: 10>: 'crossing',
        <EventType.LEAVE_NOTIFY: 11>: 'crossing',
        <EventType.FOCUS_CHANGE: 12>: 'focus_change',
        <EventType.CONFIGURE: 13>: 'configure',
        <EventType.MAP: 14>: 'any',
        <EventType.UNMAP: 15>: 'any',
        <EventType.PROPERTY_NOTIFY: 16>: 'property',
        <EventType.SELECTION_CLEAR: 17>: 'selection',
        <EventType.SELECTION_REQUEST: 18>: 'selection',
        <EventType.SELECTION_NOTIFY: 19>: 'selection',
        <EventType.PROXIMITY_IN: 20>: 'proximity',
        <EventType.PROXIMITY_OUT: 21>: 'proximity',
        <EventType.DRAG_ENTER: 22>: 'dnd',
        <EventType.DRAG_LEAVE: 23>: 'dnd',
        <EventType.DRAG_MOTION: 24>: 'dnd',
        <EventType.DRAG_STATUS: 25>: 'dnd',
        <EventType.DROP_START: 26>: 'dnd',
        <EventType.DROP_FINISHED: 27>: 'dnd',
        <EventType.CLIENT_EVENT: 28>: 'client',
        <EventType.VISIBILITY_NOTIFY: 29>: 'visibility',
        <EventType.SCROLL: 31>: 'scroll',
        <EventType.TOUCH_BEGIN: 37>: 'touch',
        <EventType.TOUCH_UPDATE: 38>: 'touch',
        <EventType.TOUCH_END: 39>: 'touch',
        <EventType.TOUCH_CANCEL: 40>: 'touch',
    }
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', '_UNION_MEMBERS': {<EventType.DELETE: 0>: 'any', <EventType.DESTROY: 1>: 'any', <EventType.MOTION_NOTIFY: 3>: 'motion', <EventType.BUTTON_PRESS: 4>: 'button', <EventType.BUTTON_RELEASE: 7>: 'button', <EventType.KEY_PRESS: 8>: 'key', <EventType.KEY_RELEASE: 9>: 'key', <EventType.ENTER_NOTIFY: 10>: 'crossing', <EventType.LEAVE_NOTIFY: 11>: 'crossing', <EventType.FOCUS_CHANGE: 12>: 'focus_change', <EventType.CONFIGURE: 13>: 'configure', <EventType.PROXIMITY_IN: 20>: 'proximity', <EventType.PROXIMITY_OUT: 21>: 'proximity', <EventType.DRAG_ENTER: 22>: 'dnd', <EventType.DRAG_LEAVE: 23>: 'dnd', <EventType.DRAG_MOTION: 24>: 'dnd', <EventType.DROP_START: 26>: 'dnd', <EventType.2BUTTON_PRESS: 5>: 'button', <EventType.3BUTTON_PRESS: 6>: 'button', <EventType.PROPERTY_NOTIFY: 16>: 'property', <EventType.SELECTION_CLEAR: 17>: 'selection', <EventType.SELECTION_REQUEST: 18>: 'selection', <EventType.SELECTION_NOTIFY: 19>: 'selection', <EventType.DRAG_STATUS: 25>: 'dnd', <EventType.DROP_FINISHED: 27>: 'dnd', <EventType.CLIENT_EVENT: 28>: 'client', <EventType.VISIBILITY_NOTIFY: 29>: 'visibility', <EventType.SCROLL: 31>: 'scroll', <EventType.EXPOSE: 2>: 'expose', <EventType.MAP: 14>: 'any', <EventType.UNMAP: 15>: 'any', <EventType.TOUCH_BEGIN: 37>: 'touch', <EventType.TOUCH_UPDATE: 38>: 'touch', <EventType.TOUCH_END: 39>: 'touch', <EventType.TOUCH_CANCEL: 40>: 'touch'}, '__getattr__': <function Event.__getattr__ at 0x000001872518b420>, '__setattr__': <function Event.__setattr__ at 0x000001872518b4c0>, '__repr__': <function Event.__repr__ at 0x000001872518b560>, '__doc__': None})"
    __gtype__ = None # (!) real value is '<GType GdkEvent (585160224)>'
    __info__ = gi.UnionInfo(Event)


