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


from .Window import Window

class Window(Window):
    """
    :Constructors:
    
    ::
    
        Window(**properties)
        new(parent:Gdk.Window=None, attributes:Gdk.WindowAttr, attributes_mask:Gdk.WindowAttributesType) -> Gdk.Window
    """
    def at_pointer(self): # real signature unknown; restored from __doc__
        """ at_pointer() -> Gdk.Window, win_x:int, win_y:int """
        pass

    def beep(self): # real signature unknown; restored from __doc__
        """ beep(self) """
        pass

    def begin_draw_frame(self, region): # real signature unknown; restored from __doc__
        """ begin_draw_frame(self, region:cairo.Region) -> Gdk.DrawingContext """
        pass

    def begin_move_drag(self, button, root_x, root_y, timestamp): # real signature unknown; restored from __doc__
        """ begin_move_drag(self, button:int, root_x:int, root_y:int, timestamp:int) """
        pass

    def begin_move_drag_for_device(self, device, button, root_x, root_y, timestamp): # real signature unknown; restored from __doc__
        """ begin_move_drag_for_device(self, device:Gdk.Device, button:int, root_x:int, root_y:int, timestamp:int) """
        pass

    def begin_paint_rect(self, rectangle): # real signature unknown; restored from __doc__
        """ begin_paint_rect(self, rectangle:Gdk.Rectangle) """
        pass

    def begin_paint_region(self, region): # real signature unknown; restored from __doc__
        """ begin_paint_region(self, region:cairo.Region) """
        pass

    def begin_resize_drag(self, edge, button, root_x, root_y, timestamp): # real signature unknown; restored from __doc__
        """ begin_resize_drag(self, edge:Gdk.WindowEdge, button:int, root_x:int, root_y:int, timestamp:int) """
        pass

    def begin_resize_drag_for_device(self, edge, device, button, root_x, root_y, timestamp): # real signature unknown; restored from __doc__
        """ begin_resize_drag_for_device(self, edge:Gdk.WindowEdge, device:Gdk.Device, button:int, root_x:int, root_y:int, timestamp:int) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cairo_create(self): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def configure_finished(self): # real signature unknown; restored from __doc__
        """ configure_finished(self) """
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

    def constrain_size(self, geometry, flags, width, height): # real signature unknown; restored from __doc__
        """ constrain_size(geometry:Gdk.Geometry, flags:Gdk.WindowHints, width:int, height:int) -> new_width:int, new_height:int """
        pass

    def coords_from_parent(self, parent_x, parent_y): # real signature unknown; restored from __doc__
        """ coords_from_parent(self, parent_x:float, parent_y:float) -> x:float, y:float """
        pass

    def coords_to_parent(self, x, y): # real signature unknown; restored from __doc__
        """ coords_to_parent(self, x:float, y:float) -> parent_x:float, parent_y:float """
        pass

    def create_gl_context(self): # real signature unknown; restored from __doc__
        """ create_gl_context(self) -> Gdk.GLContext """
        pass

    def create_similar_image_surface(self, format, width, height, scale): # real signature unknown; restored from __doc__
        """ create_similar_image_surface(self, format:cairo.Format, width:int, height:int, scale:int) -> cairo.Surface """
        pass

    def create_similar_surface(self, content, width, height): # real signature unknown; restored from __doc__
        """ create_similar_surface(self, content:cairo.Content, width:int, height:int) -> cairo.Surface """
        pass

    def deiconify(self): # real signature unknown; restored from __doc__
        """ deiconify(self) """
        pass

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroy_notify(self): # real signature unknown; restored from __doc__
        """ destroy_notify(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_create_surface(self, *args, **kwargs): # real signature unknown
        """ create_surface(self, width:int, height:int) -> cairo.Surface """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_from_embedder(self, *args, **kwargs): # real signature unknown
        """ from_embedder(self, embedder_x:float, embedder_y:float, offscreen_x:float, offscreen_y:float) """
        pass

    def do_to_embedder(self, *args, **kwargs): # real signature unknown
        """ to_embedder(self, offscreen_x:float, offscreen_y:float, embedder_x:float, embedder_y:float) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def enable_synchronized_configure(self): # real signature unknown; restored from __doc__
        """ enable_synchronized_configure(self) """
        pass

    def end_draw_frame(self, context): # real signature unknown; restored from __doc__
        """ end_draw_frame(self, context:Gdk.DrawingContext) """
        pass

    def end_paint(self): # real signature unknown; restored from __doc__
        """ end_paint(self) """
        pass

    def ensure_native(self): # real signature unknown; restored from __doc__
        """ ensure_native(self) -> bool """
        return False

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush(self) """
        pass

    def focus(self, timestamp): # real signature unknown; restored from __doc__
        """ focus(self, timestamp:int) """
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

    def freeze_toplevel_updates_libgtk_only(self): # real signature unknown; restored from __doc__
        """ freeze_toplevel_updates_libgtk_only(self) """
        pass

    def freeze_updates(self): # real signature unknown; restored from __doc__
        """ freeze_updates(self) """
        pass

    def fullscreen(self): # real signature unknown; restored from __doc__
        """ fullscreen(self) """
        pass

    def fullscreen_on_monitor(self, monitor): # real signature unknown; restored from __doc__
        """ fullscreen_on_monitor(self, monitor:int) """
        pass

    def geometry_changed(self): # real signature unknown; restored from __doc__
        """ geometry_changed(self) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_accept_focus(self): # real signature unknown; restored from __doc__
        """ get_accept_focus(self) -> bool """
        return False

    def get_background_pattern(self): # real signature unknown; restored from __doc__
        """ get_background_pattern(self) -> cairo.Pattern or None """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_children_with_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ get_children_with_user_data(self, user_data=None) -> list """
        return []

    def get_clip_region(self): # real signature unknown; restored from __doc__
        """ get_clip_region(self) -> cairo.Region """
        pass

    def get_composited(self): # real signature unknown; restored from __doc__
        """ get_composited(self) -> bool """
        return False

    def get_cursor(self): # real signature unknown; restored from __doc__
        """ get_cursor(self) -> Gdk.Cursor or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_decorations(self): # real signature unknown; restored from __doc__
        """ get_decorations(self) -> bool, decorations:Gdk.WMDecoration """
        return False

    def get_device_cursor(self, device): # real signature unknown; restored from __doc__
        """ get_device_cursor(self, device:Gdk.Device) -> Gdk.Cursor or None """
        pass

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_device_position(self, device): # real signature unknown; restored from __doc__
        """ get_device_position(self, device:Gdk.Device) -> Gdk.Window or None, x:int, y:int, mask:Gdk.ModifierType """
        pass

    def get_device_position_double(self, device): # real signature unknown; restored from __doc__
        """ get_device_position_double(self, device:Gdk.Device) -> Gdk.Window or None, x:float, y:float, mask:Gdk.ModifierType """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_drag_protocol(self): # real signature unknown; restored from __doc__
        """ get_drag_protocol(self) -> Gdk.DragProtocol, target:Gdk.Window """
        pass

    def get_effective_parent(self): # real signature unknown; restored from __doc__
        """ get_effective_parent(self) -> Gdk.Window """
        pass

    def get_effective_toplevel(self): # real signature unknown; restored from __doc__
        """ get_effective_toplevel(self) -> Gdk.Window """
        pass

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> Gdk.EventMask """
        pass

    def get_event_compression(self): # real signature unknown; restored from __doc__
        """ get_event_compression(self) -> bool """
        return False

    def get_focus_on_map(self): # real signature unknown; restored from __doc__
        """ get_focus_on_map(self) -> bool """
        return False

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock """
        pass

    def get_frame_extents(self): # real signature unknown; restored from __doc__
        """ get_frame_extents(self) -> rect:Gdk.Rectangle """
        pass

    def get_fullscreen_mode(self): # real signature unknown; restored from __doc__
        """ get_fullscreen_mode(self) -> Gdk.FullscreenMode """
        pass

    def get_geometry(self): # real signature unknown; restored from __doc__
        """ get_geometry(self) -> x:int, y:int, width:int, height:int """
        pass

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> Gdk.Window """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_modal_hint(self): # real signature unknown; restored from __doc__
        """ get_modal_hint(self) -> bool """
        return False

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> int, x:int, y:int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gdk.Window """
        pass

    def get_pass_through(self): # real signature unknown; restored from __doc__
        """ get_pass_through(self) -> bool """
        return False

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> Gdk.Window or None, x:int, y:int, mask:Gdk.ModifierType """
        pass

    def get_position(self): # real signature unknown; restored from __doc__
        """ get_position(self) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_root_coords(self, x, y): # real signature unknown; restored from __doc__
        """ get_root_coords(self, x:int, y:int) -> root_x:int, root_y:int """
        pass

    def get_root_origin(self): # real signature unknown; restored from __doc__
        """ get_root_origin(self) -> x:int, y:int """
        pass

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_source_events(self, source): # real signature unknown; restored from __doc__
        """ get_source_events(self, source:Gdk.InputSource) -> Gdk.EventMask """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gdk.WindowState """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gdk.Window """
        pass

    def get_type_hint(self): # real signature unknown; restored from __doc__
        """ get_type_hint(self) -> Gdk.WindowTypeHint """
        pass

    def get_update_area(self): # real signature unknown; restored from __doc__
        """ get_update_area(self) -> cairo.Region """
        pass

    def get_user_data(self): # real signature unknown; restored from __doc__
        """ get_user_data(self) -> data """
        pass

    def get_visible_region(self): # real signature unknown; restored from __doc__
        """ get_visible_region(self) -> cairo.Region """
        pass

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_window_type(self): # real signature unknown; restored from __doc__
        """ get_window_type(self) -> Gdk.WindowType """
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

    def has_native(self): # real signature unknown; restored from __doc__
        """ has_native(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def iconify(self): # real signature unknown; restored from __doc__
        """ iconify(self) """
        pass

    def input_shape_combine_region(self, shape_region, offset_x, offset_y): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, shape_region:cairo.Region, offset_x:int, offset_y:int) """
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

    def invalidate_maybe_recurse(self, region, child_func=None, user_data=None): # real signature unknown; restored from __doc__
        """ invalidate_maybe_recurse(self, region:cairo.Region, child_func:Gdk.WindowChildFunc=None, user_data=None) """
        pass

    def invalidate_rect(self, rect=None, invalidate_children): # real signature unknown; restored from __doc__
        """ invalidate_rect(self, rect:Gdk.Rectangle=None, invalidate_children:bool) """
        pass

    def invalidate_region(self, region, invalidate_children): # real signature unknown; restored from __doc__
        """ invalidate_region(self, region:cairo.Region, invalidate_children:bool) """
        pass

    def is_destroyed(self): # real signature unknown; restored from __doc__
        """ is_destroyed(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_input_only(self): # real signature unknown; restored from __doc__
        """ is_input_only(self) -> bool """
        return False

    def is_shaped(self): # real signature unknown; restored from __doc__
        """ is_shaped(self) -> bool """
        return False

    def is_viewable(self): # real signature unknown; restored from __doc__
        """ is_viewable(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def lower(self): # real signature unknown; restored from __doc__
        """ lower(self) """
        pass

    def mark_paint_from_clip(self, cr): # real signature unknown; restored from __doc__
        """ mark_paint_from_clip(self, cr:cairo.Context) """
        pass

    def maximize(self): # real signature unknown; restored from __doc__
        """ maximize(self) """
        pass

    def merge_child_input_shapes(self): # real signature unknown; restored from __doc__
        """ merge_child_input_shapes(self) """
        pass

    def merge_child_shapes(self): # real signature unknown; restored from __doc__
        """ merge_child_shapes(self) """
        pass

    def move(self, x, y): # real signature unknown; restored from __doc__
        """ move(self, x:int, y:int) """
        pass

    def move_region(self, region, dx, dy): # real signature unknown; restored from __doc__
        """ move_region(self, region:cairo.Region, dx:int, dy:int) """
        pass

    def move_resize(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ move_resize(self, x:int, y:int, width:int, height:int) """
        pass

    def move_to_rect(self, rect, rect_anchor, window_anchor, anchor_hints, rect_anchor_dx, rect_anchor_dy): # real signature unknown; restored from __doc__
        """ move_to_rect(self, rect:Gdk.Rectangle, rect_anchor:Gdk.Gravity, window_anchor:Gdk.Gravity, anchor_hints:Gdk.AnchorHints, rect_anchor_dx:int, rect_anchor_dy:int) """
        pass

    def new(self, parent=None, attributes, attributes_mask): # real signature unknown; restored from __doc__
        """ new(parent:Gdk.Window=None, attributes:Gdk.WindowAttr, attributes_mask:Gdk.WindowAttributesType) -> Gdk.Window """
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

    def peek_children(self): # real signature unknown; restored from __doc__
        """ peek_children(self) -> list """
        return []

    def process_all_updates(self): # real signature unknown; restored from __doc__
        """ process_all_updates() """
        pass

    def process_updates(self, update_children): # real signature unknown; restored from __doc__
        """ process_updates(self, update_children:bool) """
        pass

    def raise_(self): # real signature unknown; restored from __doc__
        """ raise_(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register_dnd(self): # real signature unknown; restored from __doc__
        """ register_dnd(self) """
        pass

    def reparent(self, new_parent, x, y): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gdk.Window, x:int, y:int) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resize(self, width, height): # real signature unknown; restored from __doc__
        """ resize(self, width:int, height:int) """
        pass

    def restack(self, sibling=None, above): # real signature unknown; restored from __doc__
        """ restack(self, sibling:Gdk.Window=None, above:bool) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def scroll(self, dx, dy): # real signature unknown; restored from __doc__
        """ scroll(self, dx:int, dy:int) """
        pass

    def set_accept_focus(self, accept_focus): # real signature unknown; restored from __doc__
        """ set_accept_focus(self, accept_focus:bool) """
        pass

    def set_background(self, color): # real signature unknown; restored from __doc__
        """ set_background(self, color:Gdk.Color) """
        pass

    def set_background_pattern(self, pattern=None): # real signature unknown; restored from __doc__
        """ set_background_pattern(self, pattern:cairo.Pattern=None) """
        pass

    def set_background_rgba(self, rgba): # real signature unknown; restored from __doc__
        """ set_background_rgba(self, rgba:Gdk.RGBA) """
        pass

    def set_child_input_shapes(self): # real signature unknown; restored from __doc__
        """ set_child_input_shapes(self) """
        pass

    def set_child_shapes(self): # real signature unknown; restored from __doc__
        """ set_child_shapes(self) """
        pass

    def set_composited(self, composited): # real signature unknown; restored from __doc__
        """ set_composited(self, composited:bool) """
        pass

    def set_cursor(self, cursor=None): # real signature unknown; restored from __doc__
        """ set_cursor(self, cursor:Gdk.Cursor=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_debug_updates(self, setting): # real signature unknown; restored from __doc__
        """ set_debug_updates(setting:bool) """
        pass

    def set_decorations(self, decorations): # real signature unknown; restored from __doc__
        """ set_decorations(self, decorations:Gdk.WMDecoration) """
        pass

    def set_device_cursor(self, device, cursor): # real signature unknown; restored from __doc__
        """ set_device_cursor(self, device:Gdk.Device, cursor:Gdk.Cursor) """
        pass

    def set_device_events(self, device, event_mask): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, event_mask:Gdk.EventMask) """
        pass

    def set_events(self, event_mask): # real signature unknown; restored from __doc__
        """ set_events(self, event_mask:Gdk.EventMask) """
        pass

    def set_event_compression(self, event_compression): # real signature unknown; restored from __doc__
        """ set_event_compression(self, event_compression:bool) """
        pass

    def set_focus_on_map(self, focus_on_map): # real signature unknown; restored from __doc__
        """ set_focus_on_map(self, focus_on_map:bool) """
        pass

    def set_fullscreen_mode(self, mode): # real signature unknown; restored from __doc__
        """ set_fullscreen_mode(self, mode:Gdk.FullscreenMode) """
        pass

    def set_functions(self, functions): # real signature unknown; restored from __doc__
        """ set_functions(self, functions:Gdk.WMFunction) """
        pass

    def set_geometry_hints(self, geometry, geom_mask): # real signature unknown; restored from __doc__
        """ set_geometry_hints(self, geometry:Gdk.Geometry, geom_mask:Gdk.WindowHints) """
        pass

    def set_group(self, leader=None): # real signature unknown; restored from __doc__
        """ set_group(self, leader:Gdk.Window=None) """
        pass

    def set_icon_list(self, pixbufs): # real signature unknown; restored from __doc__
        """ set_icon_list(self, pixbufs:list) """
        pass

    def set_icon_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_icon_name(self, name:str=None) """
        pass

    def set_keep_above(self, setting): # real signature unknown; restored from __doc__
        """ set_keep_above(self, setting:bool) """
        pass

    def set_keep_below(self, setting): # real signature unknown; restored from __doc__
        """ set_keep_below(self, setting:bool) """
        pass

    def set_modal_hint(self, modal): # real signature unknown; restored from __doc__
        """ set_modal_hint(self, modal:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_opaque_region(self, region=None): # real signature unknown; restored from __doc__
        """ set_opaque_region(self, region:cairo.Region=None) """
        pass

    def set_override_redirect(self, override_redirect): # real signature unknown; restored from __doc__
        """ set_override_redirect(self, override_redirect:bool) """
        pass

    def set_pass_through(self, pass_through): # real signature unknown; restored from __doc__
        """ set_pass_through(self, pass_through:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:str) """
        pass

    def set_shadow_width(self, left, right, top, bottom): # real signature unknown; restored from __doc__
        """ set_shadow_width(self, left:int, right:int, top:int, bottom:int) """
        pass

    def set_skip_pager_hint(self, skips_pager): # real signature unknown; restored from __doc__
        """ set_skip_pager_hint(self, skips_pager:bool) """
        pass

    def set_skip_taskbar_hint(self, skips_taskbar): # real signature unknown; restored from __doc__
        """ set_skip_taskbar_hint(self, skips_taskbar:bool) """
        pass

    def set_source_events(self, source, event_mask): # real signature unknown; restored from __doc__
        """ set_source_events(self, source:Gdk.InputSource, event_mask:Gdk.EventMask) """
        pass

    def set_startup_id(self, startup_id): # real signature unknown; restored from __doc__
        """ set_startup_id(self, startup_id:str) """
        pass

    def set_static_gravities(self, use_static): # real signature unknown; restored from __doc__
        """ set_static_gravities(self, use_static:bool) -> bool """
        return False

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_transient_for(self, parent): # real signature unknown; restored from __doc__
        """ set_transient_for(self, parent:Gdk.Window) """
        pass

    def set_type_hint(self, hint): # real signature unknown; restored from __doc__
        """ set_type_hint(self, hint:Gdk.WindowTypeHint) """
        pass

    def set_urgency_hint(self, urgent): # real signature unknown; restored from __doc__
        """ set_urgency_hint(self, urgent:bool) """
        pass

    def set_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ set_user_data(self, user_data:GObject.Object=None) """
        pass

    def shape_combine_region(self, shape_region=None, offset_x, offset_y): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, shape_region:cairo.Region=None, offset_x:int, offset_y:int) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_unraised(self): # real signature unknown; restored from __doc__
        """ show_unraised(self) """
        pass

    def show_window_menu(self, event): # real signature unknown; restored from __doc__
        """ show_window_menu(self, event:Gdk.Event) -> bool """
        return False

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stick(self): # real signature unknown; restored from __doc__
        """ stick(self) """
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

    def thaw_toplevel_updates_libgtk_only(self): # real signature unknown; restored from __doc__
        """ thaw_toplevel_updates_libgtk_only(self) """
        pass

    def thaw_updates(self): # real signature unknown; restored from __doc__
        """ thaw_updates(self) """
        pass

    def unfullscreen(self): # real signature unknown; restored from __doc__
        """ unfullscreen(self) """
        pass

    def unmaximize(self): # real signature unknown; restored from __doc__
        """ unmaximize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unstick(self): # real signature unknown; restored from __doc__
        """ unstick(self) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def withdraw(self): # real signature unknown; restored from __doc__
        """ withdraw(self) """
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

    def __init__(self, parent, attributes, attributes_mask): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, parent, attributes, attributes_mask): # reliably restored by inspect
        # no doc
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000018725090d00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', '__new__': <staticmethod(<function Window.__new__ at 0x000001872518b100>)>, '__init__': <function Window.__init__ at 0x000001872518b1a0>, 'cairo_create': <function Window.cairo_create at 0x000001872518b240>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Object GdkWindow\n\nSignals from GdkWindow:\n  pick-embedded-child (gdouble, gdouble) -> GdkWindow\n  to-embedder (gdouble, gdouble, gpointer, gpointer)\n  from-embedder (gdouble, gdouble, gpointer, gpointer)\n  create-surface (gint, gint) -> CairoSurface\n  moved-to-rect (gpointer, gpointer, gboolean, gboolean)\n\nProperties from GdkWindow:\n  cursor -> GdkCursor: Cursor\n    Cursor\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GdkWindow (585157056)>'
    __info__ = ObjectInfo(Window)


