# encoding: utf-8
# module gi.repository.GimpUi
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gimp as __gi_repository_Gimp
import gi.repository.Gtk as __gi_repository_Gtk
import gi._gi as __gi__gi


from .IntComboBox import IntComboBox

class ChannelComboBox(IntComboBox):
    """
    :Constructors:
    
    ::
    
        ChannelComboBox(**properties)
        new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) -> bool """
        return False

    def add(self, widget): # real signature unknown; restored from __doc__
        """ add(self, widget:Gtk.Widget) """
        pass

    def add_accelerator(self, accel_signal, accel_group, accel_key, accel_mods, accel_flags): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accel_signal:str, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType, accel_flags:Gtk.AccelFlags) """
        pass

    def add_attribute(self, cell, attribute, column): # real signature unknown; restored from __doc__
        """ add_attribute(self, cell:Gtk.CellRenderer, attribute:str, column:int) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ add_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def add_events(self, events): # real signature unknown; restored from __doc__
        """ add_events(self, events:int) """
        pass

    def add_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ add_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def add_tick_callback(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ add_tick_callback(self, callback:Gtk.TickCallback, user_data=None) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_template_callback_full(self, callback_name, callback_symbol): # real signature unknown; restored from __doc__
        """ bind_template_callback_full(self, callback_name:str, callback_symbol:GObject.Callback) """
        pass

    def bind_template_child_full(self, name, internal_child, struct_offset): # real signature unknown; restored from __doc__
        """ bind_template_child_full(self, name:str, internal_child:bool, struct_offset:int) """
        pass

    def can_activate_accel(self, signal_id): # real signature unknown; restored from __doc__
        """ can_activate_accel(self, signal_id:int) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_resize(self): # real signature unknown; restored from __doc__
        """ check_resize(self) """
        pass

    def child_focus(self, direction): # real signature unknown; restored from __doc__
        """ child_focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def child_get(self, child, *prop_names): # reliably restored by inspect
        """ Returns a list of child property values for the given names. """
        pass

    def child_get_property(self, child, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def child_notify(self, child, child_property): # real signature unknown; restored from __doc__
        """ child_notify(self, child:Gtk.Widget, child_property:str) """
        pass

    def child_notify_by_pspec(self, child, pspec): # real signature unknown; restored from __doc__
        """ child_notify_by_pspec(self, child:Gtk.Widget, pspec:GObject.ParamSpec) """
        pass

    def child_set(self, child, **kwargs): # reliably restored by inspect
        """ Set a child properties on the given child to key/value pairs. """
        pass

    def child_set_property(self, child, property_name, value): # real signature unknown; restored from __doc__
        """ child_set_property(self, child:Gtk.Widget, property_name:str, value:GObject.Value) """
        pass

    def child_type(self): # real signature unknown; restored from __doc__
        """ child_type(self) -> GType """
        pass

    def class_path(self): # real signature unknown; restored from __doc__
        """ class_path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_attributes(self, cell): # real signature unknown; restored from __doc__
        """ clear_attributes(self, cell:Gtk.CellRenderer) """
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def compute_expand(self, orientation): # real signature unknown; restored from __doc__
        """ compute_expand(self, orientation:Gtk.Orientation) -> bool """
        return False

    def connect(self, value, callback, data=None): # real signature unknown; restored from __doc__
        """ connect(self, value:int, callback:GObject.Callback, data=None) -> int """
        return 0

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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_pango_context(self): # real signature unknown; restored from __doc__
        """ create_pango_context(self) -> Pango.Context """
        pass

    def create_pango_layout(self, text=None): # real signature unknown; restored from __doc__
        """ create_pango_layout(self, text:str=None) -> Pango.Layout """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
        pass

    def destroyed(self, widget_pointer): # real signature unknown; restored from __doc__
        """ destroyed(self, widget_pointer:Gtk.Widget) -> widget_pointer:Gtk.Widget """
        pass

    def device_is_shadowed(self, device): # real signature unknown; restored from __doc__
        """ device_is_shadowed(self, device:Gdk.Device) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_add(self, *args, **kwargs): # real signature unknown
        """ add(self, widget:Gtk.Widget) """
        pass

    def do_adjust_baseline_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_allocation(self, baseline:int) """
        pass

    def do_adjust_baseline_request(self, *args, **kwargs): # real signature unknown
        """ adjust_baseline_request(self, minimum_baseline:int, natural_baseline:int) """
        pass

    def do_adjust_size_allocation(self, *args, **kwargs): # real signature unknown
        """ adjust_size_allocation(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int, allocated_pos:int, allocated_size:int) """
        pass

    def do_adjust_size_request(self, *args, **kwargs): # real signature unknown
        """ adjust_size_request(self, orientation:Gtk.Orientation, minimum_size:int, natural_size:int) """
        pass

    def do_button_press_event(self, *args, **kwargs): # real signature unknown
        """ button_press_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_button_release_event(self, *args, **kwargs): # real signature unknown
        """ button_release_event(self, event:Gdk.EventButton) -> bool """
        pass

    def do_can_activate_accel(self, *args, **kwargs): # real signature unknown
        """ can_activate_accel(self, signal_id:int) -> bool """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def do_check_resize(self, *args, **kwargs): # real signature unknown
        """ check_resize(self) """
        pass

    def do_child_notify(self, *args, **kwargs): # real signature unknown
        """ child_notify(self, child_property:GObject.ParamSpec) """
        pass

    def do_child_type(self, *args, **kwargs): # real signature unknown
        """ child_type(self) -> GType """
        pass

    def do_composited_changed(self, *args, **kwargs): # real signature unknown
        """ composited_changed(self) """
        pass

    def do_composite_name(self, *args, **kwargs): # real signature unknown
        """ composite_name(self, child:Gtk.Widget) -> str """
        pass

    def do_compute_expand(self, *args, **kwargs): # real signature unknown
        """ compute_expand(self, hexpand_p:bool, vexpand_p:bool) """
        pass

    def do_configure_event(self, *args, **kwargs): # real signature unknown
        """ configure_event(self, event:Gdk.EventConfigure) -> bool """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_damage_event(self, *args, **kwargs): # real signature unknown
        """ damage_event(self, event:Gdk.EventExpose) -> bool """
        pass

    def do_delete_event(self, *args, **kwargs): # real signature unknown
        """ delete_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_destroy(self, *args, **kwargs): # real signature unknown
        """ destroy(self) """
        pass

    def do_destroy_event(self, *args, **kwargs): # real signature unknown
        """ destroy_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_direction_changed(self, *args, **kwargs): # real signature unknown
        """ direction_changed(self, previous_direction:Gtk.TextDirection) """
        pass

    def do_dispatch_child_properties_changed(self, *args, **kwargs): # real signature unknown
        """ dispatch_child_properties_changed(self, n_pspecs:int, pspecs:GObject.ParamSpec) """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_drag_begin(self, *args, **kwargs): # real signature unknown
        """ drag_begin(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_delete(self, *args, **kwargs): # real signature unknown
        """ drag_data_delete(self, context:Gdk.DragContext) """
        pass

    def do_drag_data_get(self, *args, **kwargs): # real signature unknown
        """ drag_data_get(self, context:Gdk.DragContext, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_data_received(self, *args, **kwargs): # real signature unknown
        """ drag_data_received(self, context:Gdk.DragContext, x:int, y:int, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_drag_drop(self, *args, **kwargs): # real signature unknown
        """ drag_drop(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_drag_end(self, *args, **kwargs): # real signature unknown
        """ drag_end(self, context:Gdk.DragContext) """
        pass

    def do_drag_failed(self, *args, **kwargs): # real signature unknown
        """ drag_failed(self, context:Gdk.DragContext, result:Gtk.DragResult) -> bool """
        pass

    def do_drag_leave(self, *args, **kwargs): # real signature unknown
        """ drag_leave(self, context:Gdk.DragContext, time_:int) """
        pass

    def do_drag_motion(self, *args, **kwargs): # real signature unknown
        """ drag_motion(self, context:Gdk.DragContext, x:int, y:int, time_:int) -> bool """
        pass

    def do_draw(self, *args, **kwargs): # real signature unknown
        """ draw(self, cr:cairo.Context) -> bool """
        pass

    def do_enter_notify_event(self, *args, **kwargs): # real signature unknown
        """ enter_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event:Gdk.Event) -> bool """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_focus_in_event(self, *args, **kwargs): # real signature unknown
        """ focus_in_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_focus_out_event(self, *args, **kwargs): # real signature unknown
        """ focus_out_event(self, event:Gdk.EventFocus) -> bool """
        pass

    def do_forall(self, *args, **kwargs): # real signature unknown
        """ forall(self, include_internals:bool, callback:Gtk.Callback, callback_data=None) """
        pass

    def do_format_entry_text(self, *args, **kwargs): # real signature unknown
        """ format_entry_text(self, path:str) -> str """
        pass

    def do_get_accessible(self, *args, **kwargs): # real signature unknown
        """ get_accessible(self) -> Atk.Object """
        pass

    def do_get_child_property(self, *args, **kwargs): # real signature unknown
        """ get_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_get_path_for_child(self, *args, **kwargs): # real signature unknown
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_and_baseline_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_grab_broken_event(self, *args, **kwargs): # real signature unknown
        """ grab_broken_event(self, event:Gdk.EventGrabBroken) -> bool """
        pass

    def do_grab_focus(self, *args, **kwargs): # real signature unknown
        """ grab_focus(self) """
        pass

    def do_grab_notify(self, *args, **kwargs): # real signature unknown
        """ grab_notify(self, was_grabbed:bool) """
        pass

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_hierarchy_changed(self, *args, **kwargs): # real signature unknown
        """ hierarchy_changed(self, previous_toplevel:Gtk.Widget) """
        pass

    def do_keynav_failed(self, *args, **kwargs): # real signature unknown
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_key_press_event(self, *args, **kwargs): # real signature unknown
        """ key_press_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_key_release_event(self, *args, **kwargs): # real signature unknown
        """ key_release_event(self, event:Gdk.EventKey) -> bool """
        pass

    def do_leave_notify_event(self, *args, **kwargs): # real signature unknown
        """ leave_notify_event(self, event:Gdk.EventCrossing) -> bool """
        pass

    def do_map(self, *args, **kwargs): # real signature unknown
        """ map(self) """
        pass

    def do_map_event(self, *args, **kwargs): # real signature unknown
        """ map_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_mnemonic_activate(self, *args, **kwargs): # real signature unknown
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        pass

    def do_motion_notify_event(self, *args, **kwargs): # real signature unknown
        """ motion_notify_event(self, event:Gdk.EventMotion) -> bool """
        pass

    def do_move_focus(self, *args, **kwargs): # real signature unknown
        """ move_focus(self, direction:Gtk.DirectionType) """
        pass

    def do_parent_set(self, *args, **kwargs): # real signature unknown
        """ parent_set(self, previous_parent:Gtk.Widget) """
        pass

    def do_popup_menu(self, *args, **kwargs): # real signature unknown
        """ popup_menu(self) -> bool """
        pass

    def do_property_notify_event(self, *args, **kwargs): # real signature unknown
        """ property_notify_event(self, event:Gdk.EventProperty) -> bool """
        pass

    def do_proximity_in_event(self, *args, **kwargs): # real signature unknown
        """ proximity_in_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_proximity_out_event(self, *args, **kwargs): # real signature unknown
        """ proximity_out_event(self, event:Gdk.EventProximity) -> bool """
        pass

    def do_query_tooltip(self, *args, **kwargs): # real signature unknown
        """ query_tooltip(self, x:int, y:int, keyboard_tooltip:bool, tooltip:Gtk.Tooltip) -> bool """
        pass

    def do_queue_draw_region(self, *args, **kwargs): # real signature unknown
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, widget:Gtk.Widget) """
        pass

    def do_screen_changed(self, *args, **kwargs): # real signature unknown
        """ screen_changed(self, previous_screen:Gdk.Screen) """
        pass

    def do_scroll_event(self, *args, **kwargs): # real signature unknown
        """ scroll_event(self, event:Gdk.EventScroll) -> bool """
        pass

    def do_selection_clear_event(self, *args, **kwargs): # real signature unknown
        """ selection_clear_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_get(self, *args, **kwargs): # real signature unknown
        """ selection_get(self, selection_data:Gtk.SelectionData, info:int, time_:int) """
        pass

    def do_selection_notify_event(self, *args, **kwargs): # real signature unknown
        """ selection_notify_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_selection_received(self, *args, **kwargs): # real signature unknown
        """ selection_received(self, selection_data:Gtk.SelectionData, time_:int) """
        pass

    def do_selection_request_event(self, *args, **kwargs): # real signature unknown
        """ selection_request_event(self, event:Gdk.EventSelection) -> bool """
        pass

    def do_set_child_property(self, *args, **kwargs): # real signature unknown
        """ set_child_property(self, child:Gtk.Widget, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_set_focus_child(self, *args, **kwargs): # real signature unknown
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
        pass

    def do_show_all(self, *args, **kwargs): # real signature unknown
        """ show_all(self) """
        pass

    def do_show_help(self, *args, **kwargs): # real signature unknown
        """ show_help(self, help_type:Gtk.WidgetHelpType) -> bool """
        pass

    def do_size_allocate(self, *args, **kwargs): # real signature unknown
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def do_state_changed(self, *args, **kwargs): # real signature unknown
        """ state_changed(self, previous_state:Gtk.StateType) """
        pass

    def do_state_flags_changed(self, *args, **kwargs): # real signature unknown
        """ state_flags_changed(self, previous_state_flags:Gtk.StateFlags) """
        pass

    def do_style_set(self, *args, **kwargs): # real signature unknown
        """ style_set(self, previous_style:Gtk.Style) """
        pass

    def do_style_updated(self, *args, **kwargs): # real signature unknown
        """ style_updated(self) """
        pass

    def do_touch_event(self, *args, **kwargs): # real signature unknown
        """ touch_event(self, event:Gdk.EventTouch) -> bool """
        pass

    def do_unmap(self, *args, **kwargs): # real signature unknown
        """ unmap(self) """
        pass

    def do_unmap_event(self, *args, **kwargs): # real signature unknown
        """ unmap_event(self, event:Gdk.EventAny) -> bool """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
        pass

    def do_visibility_notify_event(self, *args, **kwargs): # real signature unknown
        """ visibility_notify_event(self, event:Gdk.EventVisibility) -> bool """
        pass

    def do_window_state_event(self, *args, **kwargs): # real signature unknown
        """ window_state_event(self, event:Gdk.EventWindowState) -> bool """
        pass

    def drag_begin(self, targets, actions, button, event=None): # real signature unknown; restored from __doc__
        """ drag_begin(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None) -> Gdk.DragContext """
        pass

    def drag_begin_with_coordinates(self, targets, actions, button, event=None, x, y): # real signature unknown; restored from __doc__
        """ drag_begin_with_coordinates(self, targets:Gtk.TargetList, actions:Gdk.DragAction, button:int, event:Gdk.Event=None, x:int, y:int) -> Gdk.DragContext """
        pass

    def drag_check_threshold(self, start_x, start_y, current_x, current_y): # real signature unknown; restored from __doc__
        """ drag_check_threshold(self, start_x:int, start_y:int, current_x:int, current_y:int) -> bool """
        return False

    def drag_dest_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_image_targets(self) """
        pass

    def drag_dest_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_text_targets(self) """
        pass

    def drag_dest_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_dest_add_uri_targets(self) """
        pass

    def drag_dest_find_target(self, context, target_list=None): # real signature unknown; restored from __doc__
        """ drag_dest_find_target(self, context:Gdk.DragContext, target_list:Gtk.TargetList=None) -> Gdk.Atom """
        pass

    def drag_dest_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_dest_get_track_motion(self): # real signature unknown; restored from __doc__
        """ drag_dest_get_track_motion(self) -> bool """
        return False

    def drag_dest_set(self, flags, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_dest_set(self, flags:Gtk.DestDefaults, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_dest_set_proxy(self, proxy_window, protocol, use_coordinates): # real signature unknown; restored from __doc__
        """ drag_dest_set_proxy(self, proxy_window:Gdk.Window, protocol:Gdk.DragProtocol, use_coordinates:bool) """
        pass

    def drag_dest_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_dest_set_track_motion(self, track_motion): # real signature unknown; restored from __doc__
        """ drag_dest_set_track_motion(self, track_motion:bool) """
        pass

    def drag_dest_unset(self): # real signature unknown; restored from __doc__
        """ drag_dest_unset(self) """
        pass

    def drag_get_data(self, context, target, time_): # real signature unknown; restored from __doc__
        """ drag_get_data(self, context:Gdk.DragContext, target:Gdk.Atom, time_:int) """
        pass

    def drag_highlight(self): # real signature unknown; restored from __doc__
        """ drag_highlight(self) """
        pass

    def drag_source_add_image_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_image_targets(self) """
        pass

    def drag_source_add_text_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_text_targets(self) """
        pass

    def drag_source_add_uri_targets(self): # real signature unknown; restored from __doc__
        """ drag_source_add_uri_targets(self) """
        pass

    def drag_source_get_target_list(self): # real signature unknown; restored from __doc__
        """ drag_source_get_target_list(self) -> Gtk.TargetList or None """
        pass

    def drag_source_set(self, start_button_mask, targets=None, actions): # real signature unknown; restored from __doc__
        """ drag_source_set(self, start_button_mask:Gdk.ModifierType, targets:list=None, actions:Gdk.DragAction) """
        pass

    def drag_source_set_icon_gicon(self, icon): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_gicon(self, icon:Gio.Icon) """
        pass

    def drag_source_set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_name(self, icon_name:str) """
        pass

    def drag_source_set_icon_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def drag_source_set_icon_stock(self, stock_id): # real signature unknown; restored from __doc__
        """ drag_source_set_icon_stock(self, stock_id:str) """
        pass

    def drag_source_set_target_list(self, target_list): # reliably restored by inspect
        # no doc
        pass

    def drag_source_unset(self): # real signature unknown; restored from __doc__
        """ drag_source_unset(self) """
        pass

    def drag_unhighlight(self): # real signature unknown; restored from __doc__
        """ drag_unhighlight(self) """
        pass

    def draw(self, cr): # real signature unknown; restored from __doc__
        """ draw(self, cr:cairo.Context) """
        pass

    def editing_done(self): # real signature unknown; restored from __doc__
        """ editing_done(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_style(self): # real signature unknown; restored from __doc__
        """ ensure_style(self) """
        pass

    def error_bell(self): # real signature unknown; restored from __doc__
        """ error_bell(self) """
        pass

    def event(self, event): # real signature unknown; restored from __doc__
        """ event(self, event:Gdk.Event) -> bool """
        return False

    def find_child_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_child_property(self, property_name:str) -> GObject.ParamSpec or None """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_style_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def forall(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ forall(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Gtk.Callback, callback_data=None) """
        pass

    def freeze_child_notify(self): # reliably restored by inspect
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

    def get_accessible(self): # real signature unknown; restored from __doc__
        """ get_accessible(self) -> Atk.Object """
        pass

    def get_action_group(self, prefix): # real signature unknown; restored from __doc__
        """ get_action_group(self, prefix:str) -> Gio.ActionGroup or None """
        pass

    def get_active(self): # real signature unknown; restored from __doc__
        """ get_active(self) -> bool, value:int """
        return False

    def get_active_id(self): # real signature unknown; restored from __doc__
        """ get_active_id(self) -> str or None """
        return ""

    def get_active_iter(*args, **kwargs): # reliably restored by inspect
        """ get_active_iter(self) -> bool, iter:Gtk.TreeIter """
        pass

    def get_active_user_data(self): # real signature unknown; restored from __doc__
        """ get_active_user_data(self) -> bool, user_data """
        return False

    def get_add_tearoffs(self): # real signature unknown; restored from __doc__
        """ get_add_tearoffs(self) -> bool """
        return False

    def get_allocated_baseline(self): # real signature unknown; restored from __doc__
        """ get_allocated_baseline(self) -> int """
        return 0

    def get_allocated_height(self): # real signature unknown; restored from __doc__
        """ get_allocated_height(self) -> int """
        return 0

    def get_allocated_size(self): # real signature unknown; restored from __doc__
        """ get_allocated_size(self) -> allocation:Gdk.Rectangle, baseline:int """
        pass

    def get_allocated_width(self): # real signature unknown; restored from __doc__
        """ get_allocated_width(self) -> int """
        return 0

    def get_allocation(self): # real signature unknown; restored from __doc__
        """ get_allocation(self) -> allocation:Gdk.Rectangle """
        pass

    def get_ancestor(self, widget_type): # real signature unknown; restored from __doc__
        """ get_ancestor(self, widget_type:GType) -> Gtk.Widget or None """
        pass

    def get_app_paintable(self): # real signature unknown; restored from __doc__
        """ get_app_paintable(self) -> bool """
        return False

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> Gtk.CellArea or None """
        pass

    def get_border_width(self): # real signature unknown; restored from __doc__
        """ get_border_width(self) -> int """
        return 0

    def get_button_sensitivity(self): # real signature unknown; restored from __doc__
        """ get_button_sensitivity(self) -> Gtk.SensitivityType """
        pass

    def get_can_default(self): # real signature unknown; restored from __doc__
        """ get_can_default(self) -> bool """
        return False

    def get_can_focus(self): # real signature unknown; restored from __doc__
        """ get_can_focus(self) -> bool """
        return False

    def get_cells(self): # real signature unknown; restored from __doc__
        """ get_cells(self) -> list """
        return []

    def get_child(self): # real signature unknown; restored from __doc__
        """ get_child(self) -> Gtk.Widget or None """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_child_requisition(self): # real signature unknown; restored from __doc__
        """ get_child_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_child_visible(self): # real signature unknown; restored from __doc__
        """ get_child_visible(self) -> bool """
        return False

    def get_clip(self): # real signature unknown; restored from __doc__
        """ get_clip(self) -> clip:Gdk.Rectangle """
        pass

    def get_clipboard(self, selection): # real signature unknown; restored from __doc__
        """ get_clipboard(self, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_column_span_column(self): # real signature unknown; restored from __doc__
        """ get_column_span_column(self) -> int """
        return 0

    def get_composite_name(self): # real signature unknown; restored from __doc__
        """ get_composite_name(self) -> str """
        return ""

    def get_css_name(self): # real signature unknown; restored from __doc__
        """ get_css_name(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_direction(self): # real signature unknown; restored from __doc__
        """ get_default_direction() -> Gtk.TextDirection """
        pass

    def get_default_style(self): # real signature unknown; restored from __doc__
        """ get_default_style() -> Gtk.Style """
        pass

    def get_device_enabled(self, device): # real signature unknown; restored from __doc__
        """ get_device_enabled(self, device:Gdk.Device) -> bool """
        return False

    def get_device_events(self, device): # real signature unknown; restored from __doc__
        """ get_device_events(self, device:Gdk.Device) -> Gdk.EventMask """
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_double_buffered(self): # real signature unknown; restored from __doc__
        """ get_double_buffered(self) -> bool """
        return False

    def get_entry_text_column(self): # real signature unknown; restored from __doc__
        """ get_entry_text_column(self) -> int """
        return 0

    def get_events(self): # real signature unknown; restored from __doc__
        """ get_events(self) -> int """
        return 0

    def get_focus_chain(*args, **kwargs): # reliably restored by inspect
        """ get_focus_chain(self) -> bool, focusable_widgets:list """
        pass

    def get_focus_child(self): # real signature unknown; restored from __doc__
        """ get_focus_child(self) -> Gtk.Widget or None """
        pass

    def get_focus_hadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_hadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_focus_on_click(self): # real signature unknown; restored from __doc__
        """ get_focus_on_click(self) -> bool """
        return False

    def get_focus_vadjustment(self): # real signature unknown; restored from __doc__
        """ get_focus_vadjustment(self) -> Gtk.Adjustment or None """
        pass

    def get_font_map(self): # real signature unknown; restored from __doc__
        """ get_font_map(self) -> Pango.FontMap or None """
        pass

    def get_font_options(self): # real signature unknown; restored from __doc__
        """ get_font_options(self) -> cairo.FontOptions or None """
        pass

    def get_frame_clock(self): # real signature unknown; restored from __doc__
        """ get_frame_clock(self) -> Gdk.FrameClock or None """
        pass

    def get_halign(self): # real signature unknown; restored from __doc__
        """ get_halign(self) -> Gtk.Align """
        pass

    def get_has_entry(self): # real signature unknown; restored from __doc__
        """ get_has_entry(self) -> bool """
        return False

    def get_has_tooltip(self): # real signature unknown; restored from __doc__
        """ get_has_tooltip(self) -> bool """
        return False

    def get_has_window(self): # real signature unknown; restored from __doc__
        """ get_has_window(self) -> bool """
        return False

    def get_hexpand(self): # real signature unknown; restored from __doc__
        """ get_hexpand(self) -> bool """
        return False

    def get_hexpand_set(self): # real signature unknown; restored from __doc__
        """ get_hexpand_set(self) -> bool """
        return False

    def get_id_column(self): # real signature unknown; restored from __doc__
        """ get_id_column(self) -> int """
        return 0

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_layout(self): # real signature unknown; restored from __doc__
        """ get_layout(self) -> GimpUi.IntComboBoxLayout """
        pass

    def get_mapped(self): # real signature unknown; restored from __doc__
        """ get_mapped(self) -> bool """
        return False

    def get_margin_bottom(self): # real signature unknown; restored from __doc__
        """ get_margin_bottom(self) -> int """
        return 0

    def get_margin_end(self): # real signature unknown; restored from __doc__
        """ get_margin_end(self) -> int """
        return 0

    def get_margin_left(self): # real signature unknown; restored from __doc__
        """ get_margin_left(self) -> int """
        return 0

    def get_margin_right(self): # real signature unknown; restored from __doc__
        """ get_margin_right(self) -> int """
        return 0

    def get_margin_start(self): # real signature unknown; restored from __doc__
        """ get_margin_start(self) -> int """
        return 0

    def get_margin_top(self): # real signature unknown; restored from __doc__
        """ get_margin_top(self) -> int """
        return 0

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> Gtk.TreeModel """
        pass

    def get_modifier_mask(self, intent): # real signature unknown; restored from __doc__
        """ get_modifier_mask(self, intent:Gdk.ModifierIntent) -> Gdk.ModifierType """
        pass

    def get_modifier_style(self): # real signature unknown; restored from __doc__
        """ get_modifier_style(self) -> Gtk.RcStyle """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_no_show_all(self): # real signature unknown; restored from __doc__
        """ get_no_show_all(self) -> bool """
        return False

    def get_opacity(self): # real signature unknown; restored from __doc__
        """ get_opacity(self) -> float """
        return 0.0

    def get_pango_context(self): # real signature unknown; restored from __doc__
        """ get_pango_context(self) -> Pango.Context """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.Widget or None """
        pass

    def get_parent_window(self): # real signature unknown; restored from __doc__
        """ get_parent_window(self) -> Gdk.Window or None """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_path_for_child(self, child): # real signature unknown; restored from __doc__
        """ get_path_for_child(self, child:Gtk.Widget) -> Gtk.WidgetPath """
        pass

    def get_pointer(self): # real signature unknown; restored from __doc__
        """ get_pointer(self) -> x:int, y:int """
        pass

    def get_popup_accessible(self): # real signature unknown; restored from __doc__
        """ get_popup_accessible(self) -> Atk.Object """
        pass

    def get_popup_fixed_width(self): # real signature unknown; restored from __doc__
        """ get_popup_fixed_width(self) -> bool """
        return False

    def get_preferred_height(self): # real signature unknown; restored from __doc__
        """ get_preferred_height(self) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_and_baseline_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_and_baseline_for_width(self, width:int) -> minimum_height:int, natural_height:int, minimum_baseline:int, natural_baseline:int """
        pass

    def get_preferred_height_for_width(self, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self): # real signature unknown; restored from __doc__
        """ get_preferred_size(self) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self): # real signature unknown; restored from __doc__
        """ get_preferred_width(self) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_realized(self): # real signature unknown; restored from __doc__
        """ get_realized(self) -> bool """
        return False

    def get_receives_default(self): # real signature unknown; restored from __doc__
        """ get_receives_default(self) -> bool """
        return False

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_requisition(self): # real signature unknown; restored from __doc__
        """ get_requisition(self) -> requisition:Gtk.Requisition """
        pass

    def get_resize_mode(self): # real signature unknown; restored from __doc__
        """ get_resize_mode(self) -> Gtk.ResizeMode """
        pass

    def get_root_window(self): # real signature unknown; restored from __doc__
        """ get_root_window(self) -> Gdk.Window """
        pass

    def get_row_span_column(self): # real signature unknown; restored from __doc__
        """ get_row_span_column(self) -> int """
        return 0

    def get_scale_factor(self): # real signature unknown; restored from __doc__
        """ get_scale_factor(self) -> int """
        return 0

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen """
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_settings(self): # real signature unknown; restored from __doc__
        """ get_settings(self) -> Gtk.Settings """
        pass

    def get_size_request(self): # real signature unknown; restored from __doc__
        """ get_size_request(self) -> width:int, height:int """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateType """
        pass

    def get_state_flags(self): # real signature unknown; restored from __doc__
        """ get_state_flags(self) -> Gtk.StateFlags """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.Style """
        pass

    def get_style_context(self): # real signature unknown; restored from __doc__
        """ get_style_context(self) -> Gtk.StyleContext """
        pass

    def get_support_multidevice(self): # real signature unknown; restored from __doc__
        """ get_support_multidevice(self) -> bool """
        return False

    def get_template_child(self, widget_type, name): # real signature unknown; restored from __doc__
        """ get_template_child(self, widget_type:GType, name:str) -> GObject.Object """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_tooltip_markup(self): # real signature unknown; restored from __doc__
        """ get_tooltip_markup(self) -> str or None """
        return ""

    def get_tooltip_text(self): # real signature unknown; restored from __doc__
        """ get_tooltip_text(self) -> str or None """
        return ""

    def get_tooltip_window(self): # real signature unknown; restored from __doc__
        """ get_tooltip_window(self) -> Gtk.Window """
        pass

    def get_toplevel(self): # real signature unknown; restored from __doc__
        """ get_toplevel(self) -> Gtk.Widget """
        pass

    def get_valign(self): # real signature unknown; restored from __doc__
        """ get_valign(self) -> Gtk.Align """
        pass

    def get_valign_with_baseline(self): # real signature unknown; restored from __doc__
        """ get_valign_with_baseline(self) -> Gtk.Align """
        pass

    def get_vexpand(self): # real signature unknown; restored from __doc__
        """ get_vexpand(self) -> bool """
        return False

    def get_vexpand_set(self): # real signature unknown; restored from __doc__
        """ get_vexpand_set(self) -> bool """
        return False

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visual(self): # real signature unknown; restored from __doc__
        """ get_visual(self) -> Gdk.Visual """
        pass

    def get_window(self): # real signature unknown; restored from __doc__
        """ get_window(self) -> Gdk.Window or None """
        pass

    def get_wrap_width(self): # real signature unknown; restored from __doc__
        """ get_wrap_width(self) -> int """
        return 0

    def grab_add(self): # real signature unknown; restored from __doc__
        """ grab_add(self) """
        pass

    def grab_default(self): # real signature unknown; restored from __doc__
        """ grab_default(self) """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) """
        pass

    def grab_remove(self): # real signature unknown; restored from __doc__
        """ grab_remove(self) """
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

    def handle_border_width(self): # real signature unknown; restored from __doc__
        """ handle_border_width(self) """
        pass

    def has_default(self): # real signature unknown; restored from __doc__
        """ has_default(self) -> bool """
        return False

    def has_focus(self): # real signature unknown; restored from __doc__
        """ has_focus(self) -> bool """
        return False

    def has_grab(self): # real signature unknown; restored from __doc__
        """ has_grab(self) -> bool """
        return False

    def has_rc_style(self): # real signature unknown; restored from __doc__
        """ has_rc_style(self) -> bool """
        return False

    def has_screen(self): # real signature unknown; restored from __doc__
        """ has_screen(self) -> bool """
        return False

    def has_visible_focus(self): # real signature unknown; restored from __doc__
        """ has_visible_focus(self) -> bool """
        return False

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
        pass

    def hide_on_delete(self): # real signature unknown; restored from __doc__
        """ hide_on_delete(self) -> bool """
        return False

    def init_template(self): # real signature unknown; restored from __doc__
        """ init_template(self) """
        pass

    def input_shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ input_shape_combine_region(self, region:cairo.Region=None) """
        pass

    def insert_action_group(self, name, group=None): # real signature unknown; restored from __doc__
        """ insert_action_group(self, name:str, group:Gio.ActionGroup=None) """
        pass

    def install_child_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_child_properties(self, pspecs:list) """
        pass

    def install_child_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_child_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def install_style_property(self, pspec): # real signature unknown; restored from __doc__
        """ install_style_property(self, pspec:GObject.ParamSpec) """
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

    def intersect(self, area): # real signature unknown; restored from __doc__
        """ intersect(self, area:Gdk.Rectangle) -> bool, intersection:Gdk.Rectangle """
        return False

    def in_destruction(self): # real signature unknown; restored from __doc__
        """ in_destruction(self) -> bool """
        return False

    def is_ancestor(self, ancestor): # real signature unknown; restored from __doc__
        """ is_ancestor(self, ancestor:Gtk.Widget) -> bool """
        return False

    def is_composited(self): # real signature unknown; restored from __doc__
        """ is_composited(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus(self): # real signature unknown; restored from __doc__
        """ is_focus(self) -> bool """
        return False

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_toplevel(self): # real signature unknown; restored from __doc__
        """ is_toplevel(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def keynav_failed(self, direction): # real signature unknown; restored from __doc__
        """ keynav_failed(self, direction:Gtk.DirectionType) -> bool """
        return False

    def list_accel_closures(self): # real signature unknown; restored from __doc__
        """ list_accel_closures(self) -> list """
        return []

    def list_action_prefixes(self): # real signature unknown; restored from __doc__
        """ list_action_prefixes(self) -> list """
        return []

    def list_child_properties(self): # real signature unknown; restored from __doc__
        """ list_child_properties(self) -> list """
        return []

    def list_mnemonic_labels(self): # real signature unknown; restored from __doc__
        """ list_mnemonic_labels(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_style_properties(self): # real signature unknown; restored from __doc__
        """ list_style_properties(self) -> list """
        return []

    def map(self): # real signature unknown; restored from __doc__
        """ map(self) """
        pass

    def mnemonic_activate(self, group_cycling): # real signature unknown; restored from __doc__
        """ mnemonic_activate(self, group_cycling:bool) -> bool """
        return False

    def modify_base(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_base(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_bg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_bg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_cursor(self, primary=None, secondary=None): # real signature unknown; restored from __doc__
        """ modify_cursor(self, primary:Gdk.Color=None, secondary:Gdk.Color=None) """
        pass

    def modify_fg(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_fg(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    def modify_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ modify_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def modify_style(self, style): # real signature unknown; restored from __doc__
        """ modify_style(self, style:Gtk.RcStyle) """
        pass

    def modify_text(self, state, color=None): # real signature unknown; restored from __doc__
        """ modify_text(self, state:Gtk.StateType, color:Gdk.Color=None) """
        pass

    @classmethod
    def new(cls, constraint=None): # real signature unknown; restored from __doc__
        """ new(constraint:GimpUi.ItemConstraintFunc=None) -> Gtk.Widget """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_area(self, area): # real signature unknown; restored from __doc__
        """ new_with_area(area:Gtk.CellArea) -> Gtk.Widget """
        pass

    def new_with_area_and_entry(self, area): # real signature unknown; restored from __doc__
        """ new_with_area_and_entry(area:Gtk.CellArea) -> Gtk.Widget """
        pass

    def new_with_entry(self): # real signature unknown; restored from __doc__
        """ new_with_entry() -> Gtk.Widget """
        pass

    def new_with_model(self, model): # real signature unknown; restored from __doc__
        """ new_with_model(model:Gtk.TreeModel) -> Gtk.Widget """
        pass

    def new_with_model_and_entry(self, model): # real signature unknown; restored from __doc__
        """ new_with_model_and_entry(model:Gtk.TreeModel) -> Gtk.Widget """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_background_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_background_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_color(self, state, color=None): # real signature unknown; restored from __doc__
        """ override_color(self, state:Gtk.StateFlags, color:Gdk.RGBA=None) """
        pass

    def override_cursor(self, cursor=None, secondary_cursor=None): # real signature unknown; restored from __doc__
        """ override_cursor(self, cursor:Gdk.RGBA=None, secondary_cursor:Gdk.RGBA=None) """
        pass

    def override_font(self, font_desc=None): # real signature unknown; restored from __doc__
        """ override_font(self, font_desc:Pango.FontDescription=None) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def override_symbolic_color(self, name, color=None): # real signature unknown; restored from __doc__
        """ override_symbolic_color(self, name:str, color:Gdk.RGBA=None) """
        pass

    def pack_end(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_end(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def pack_start(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_start(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def path(self): # real signature unknown; restored from __doc__
        """ path(self) -> path_length:int, path:str, path_reversed:str """
        pass

    def popdown(self): # real signature unknown; restored from __doc__
        """ popdown(self) """
        pass

    def popup(self): # real signature unknown; restored from __doc__
        """ popup(self) """
        pass

    def popup_for_device(self, device): # real signature unknown; restored from __doc__
        """ popup_for_device(self, device:Gdk.Device) """
        pass

    def pop_composite_child(self): # real signature unknown; restored from __doc__
        """ pop_composite_child() """
        pass

    def propagate_draw(self, child, cr): # real signature unknown; restored from __doc__
        """ propagate_draw(self, child:Gtk.Widget, cr:cairo.Context) """
        pass

    def push_composite_child(self): # real signature unknown; restored from __doc__
        """ push_composite_child() """
        pass

    def queue_allocate(self): # real signature unknown; restored from __doc__
        """ queue_allocate(self) """
        pass

    def queue_compute_expand(self): # real signature unknown; restored from __doc__
        """ queue_compute_expand(self) """
        pass

    def queue_draw(self): # real signature unknown; restored from __doc__
        """ queue_draw(self) """
        pass

    def queue_draw_area(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ queue_draw_area(self, x:int, y:int, width:int, height:int) """
        pass

    def queue_draw_region(self, region): # real signature unknown; restored from __doc__
        """ queue_draw_region(self, region:cairo.Region) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def queue_resize_no_redraw(self): # real signature unknown; restored from __doc__
        """ queue_resize_no_redraw(self) """
        pass

    def realize(self): # real signature unknown; restored from __doc__
        """ realize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def region_intersect(self, region): # real signature unknown; restored from __doc__
        """ region_intersect(self, region:cairo.Region) -> cairo.Region """
        pass

    def register_window(self, window): # real signature unknown; restored from __doc__
        """ register_window(self, window:Gdk.Window) """
        pass

    def remove(self, widget): # real signature unknown; restored from __doc__
        """ remove(self, widget:Gtk.Widget) """
        pass

    def remove_accelerator(self, accel_group, accel_key, accel_mods): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, accel_group:Gtk.AccelGroup, accel_key:int, accel_mods:Gdk.ModifierType) -> bool """
        return False

    def remove_mnemonic_label(self, label): # real signature unknown; restored from __doc__
        """ remove_mnemonic_label(self, label:Gtk.Widget) """
        pass

    def remove_tick_callback(self, id): # real signature unknown; restored from __doc__
        """ remove_tick_callback(self, id:int) """
        pass

    def remove_widget(self): # real signature unknown; restored from __doc__
        """ remove_widget(self) """
        pass

    def render_icon(self, stock_id, size, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, stock_id:str, size:int, detail:str=None) -> GdkPixbuf.Pixbuf or None """
        pass

    def render_icon_pixbuf(self, stock_id, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, stock_id:str, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def reorder(self, cell, position): # real signature unknown; restored from __doc__
        """ reorder(self, cell:Gtk.CellRenderer, position:int) """
        pass

    def reparent(self, new_parent): # real signature unknown; restored from __doc__
        """ reparent(self, new_parent:Gtk.Widget) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reset_rc_styles(self): # real signature unknown; restored from __doc__
        """ reset_rc_styles(self) """
        pass

    def reset_style(self): # real signature unknown; restored from __doc__
        """ reset_style(self) """
        pass

    def resize_children(self): # real signature unknown; restored from __doc__
        """ resize_children(self) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def send_expose(self, event): # real signature unknown; restored from __doc__
        """ send_expose(self, event:Gdk.Event) -> int """
        return 0

    def send_focus_change(self, event): # real signature unknown; restored from __doc__
        """ send_focus_change(self, event:Gdk.Event) -> bool """
        return False

    def set_accel_path(self, accel_path=None, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str=None, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accessible_role(self, role): # real signature unknown; restored from __doc__
        """ set_accessible_role(self, role:Atk.Role) """
        pass

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_active(self, value): # real signature unknown; restored from __doc__
        """ set_active(self, value:int) -> bool """
        return False

    def set_active_by_user_data(self, user_data=None): # real signature unknown; restored from __doc__
        """ set_active_by_user_data(self, user_data=None) -> bool """
        return False

    def set_active_id(self, active_id=None): # real signature unknown; restored from __doc__
        """ set_active_id(self, active_id:str=None) -> bool """
        return False

    def set_active_iter(self, iter=None): # real signature unknown; restored from __doc__
        """ set_active_iter(self, iter:Gtk.TreeIter=None) """
        pass

    def set_add_tearoffs(self, add_tearoffs): # real signature unknown; restored from __doc__
        """ set_add_tearoffs(self, add_tearoffs:bool) """
        pass

    def set_allocation(self, allocation): # real signature unknown; restored from __doc__
        """ set_allocation(self, allocation:Gdk.Rectangle) """
        pass

    def set_app_paintable(self, app_paintable): # real signature unknown; restored from __doc__
        """ set_app_paintable(self, app_paintable:bool) """
        pass

    def set_border_width(self, border_width): # real signature unknown; restored from __doc__
        """ set_border_width(self, border_width:int) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_button_sensitivity(self, sensitivity): # real signature unknown; restored from __doc__
        """ set_button_sensitivity(self, sensitivity:Gtk.SensitivityType) """
        pass

    def set_can_default(self, can_default): # real signature unknown; restored from __doc__
        """ set_can_default(self, can_default:bool) """
        pass

    def set_can_focus(self, can_focus): # real signature unknown; restored from __doc__
        """ set_can_focus(self, can_focus:bool) """
        pass

    def set_cell_data_func(self, cell, func=None, func_data=None): # real signature unknown; restored from __doc__
        """ set_cell_data_func(self, cell:Gtk.CellRenderer, func:Gtk.CellLayoutDataFunc=None, func_data=None) """
        pass

    def set_child_visible(self, is_visible): # real signature unknown; restored from __doc__
        """ set_child_visible(self, is_visible:bool) """
        pass

    def set_clip(self, clip): # real signature unknown; restored from __doc__
        """ set_clip(self, clip:Gdk.Rectangle) """
        pass

    def set_column_span_column(self, column_span): # real signature unknown; restored from __doc__
        """ set_column_span_column(self, column_span:int) """
        pass

    def set_composite_name(self, name): # real signature unknown; restored from __doc__
        """ set_composite_name(self, name:str) """
        pass

    def set_connect_func(self, connect_func, connect_data=None): # real signature unknown; restored from __doc__
        """ set_connect_func(self, connect_func:Gtk.BuilderConnectFunc, connect_data=None) """
        pass

    def set_css_name(self, name): # real signature unknown; restored from __doc__
        """ set_css_name(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_default_direction(dir:Gtk.TextDirection) """
        pass

    def set_device_enabled(self, device, enabled): # real signature unknown; restored from __doc__
        """ set_device_enabled(self, device:Gdk.Device, enabled:bool) """
        pass

    def set_device_events(self, device, events): # real signature unknown; restored from __doc__
        """ set_device_events(self, device:Gdk.Device, events:Gdk.EventMask) """
        pass

    def set_direction(self, dir): # real signature unknown; restored from __doc__
        """ set_direction(self, dir:Gtk.TextDirection) """
        pass

    def set_double_buffered(self, double_buffered): # real signature unknown; restored from __doc__
        """ set_double_buffered(self, double_buffered:bool) """
        pass

    def set_entry_text_column(self, text_column): # real signature unknown; restored from __doc__
        """ set_entry_text_column(self, text_column:int) """
        pass

    def set_events(self, events): # real signature unknown; restored from __doc__
        """ set_events(self, events:int) """
        pass

    def set_focus_chain(self, focusable_widgets): # real signature unknown; restored from __doc__
        """ set_focus_chain(self, focusable_widgets:list) """
        pass

    def set_focus_child(self, child=None): # real signature unknown; restored from __doc__
        """ set_focus_child(self, child:Gtk.Widget=None) """
        pass

    def set_focus_hadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_hadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_focus_on_click(self, focus_on_click): # real signature unknown; restored from __doc__
        """ set_focus_on_click(self, focus_on_click:bool) """
        pass

    def set_focus_vadjustment(self, adjustment): # real signature unknown; restored from __doc__
        """ set_focus_vadjustment(self, adjustment:Gtk.Adjustment) """
        pass

    def set_font_map(self, font_map=None): # real signature unknown; restored from __doc__
        """ set_font_map(self, font_map:Pango.FontMap=None) """
        pass

    def set_font_options(self, options=None): # real signature unknown; restored from __doc__
        """ set_font_options(self, options:cairo.FontOptions=None) """
        pass

    def set_halign(self, align): # real signature unknown; restored from __doc__
        """ set_halign(self, align:Gtk.Align) """
        pass

    def set_has_tooltip(self, has_tooltip): # real signature unknown; restored from __doc__
        """ set_has_tooltip(self, has_tooltip:bool) """
        pass

    def set_has_window(self, has_window): # real signature unknown; restored from __doc__
        """ set_has_window(self, has_window:bool) """
        pass

    def set_hexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_hexpand(self, expand:bool) """
        pass

    def set_hexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_hexpand_set(self, set:bool) """
        pass

    def set_id_column(self, id_column): # real signature unknown; restored from __doc__
        """ set_id_column(self, id_column:int) """
        pass

    def set_label(self, label): # real signature unknown; restored from __doc__
        """ set_label(self, label:str) """
        pass

    def set_layout(self, layout): # real signature unknown; restored from __doc__
        """ set_layout(self, layout:GimpUi.IntComboBoxLayout) """
        pass

    def set_mapped(self, mapped): # real signature unknown; restored from __doc__
        """ set_mapped(self, mapped:bool) """
        pass

    def set_margin_bottom(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_bottom(self, margin:int) """
        pass

    def set_margin_end(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_end(self, margin:int) """
        pass

    def set_margin_left(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_left(self, margin:int) """
        pass

    def set_margin_right(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_right(self, margin:int) """
        pass

    def set_margin_start(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_start(self, margin:int) """
        pass

    def set_margin_top(self, margin): # real signature unknown; restored from __doc__
        """ set_margin_top(self, margin:int) """
        pass

    def set_model(self, model=None): # real signature unknown; restored from __doc__
        """ set_model(self, model:Gtk.TreeModel=None) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_no_show_all(self, no_show_all): # real signature unknown; restored from __doc__
        """ set_no_show_all(self, no_show_all:bool) """
        pass

    def set_opacity(self, opacity): # real signature unknown; restored from __doc__
        """ set_opacity(self, opacity:float) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Gtk.Widget) """
        pass

    def set_parent_window(self, parent_window): # real signature unknown; restored from __doc__
        """ set_parent_window(self, parent_window:Gdk.Window) """
        pass

    def set_popup_fixed_width(self, fixed): # real signature unknown; restored from __doc__
        """ set_popup_fixed_width(self, fixed:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_realized(self, realized): # real signature unknown; restored from __doc__
        """ set_realized(self, realized:bool) """
        pass

    def set_reallocate_redraws(self, needs_redraws): # real signature unknown; restored from __doc__
        """ set_reallocate_redraws(self, needs_redraws:bool) """
        pass

    def set_receives_default(self, receives_default): # real signature unknown; restored from __doc__
        """ set_receives_default(self, receives_default:bool) """
        pass

    def set_redraw_on_allocate(self, redraw_on_allocate): # real signature unknown; restored from __doc__
        """ set_redraw_on_allocate(self, redraw_on_allocate:bool) """
        pass

    def set_resize_mode(self, resize_mode): # real signature unknown; restored from __doc__
        """ set_resize_mode(self, resize_mode:Gtk.ResizeMode) """
        pass

    def set_row_separator_func(self, func, data=None): # real signature unknown; restored from __doc__
        """ set_row_separator_func(self, func:Gtk.TreeViewRowSeparatorFunc, data=None) """
        pass

    def set_row_span_column(self, row_span): # real signature unknown; restored from __doc__
        """ set_row_span_column(self, row_span:int) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_sensitivity(self, func, data=None): # real signature unknown; restored from __doc__
        """ set_sensitivity(self, func:GimpUi.IntSensitivityFunc, data=None) """
        pass

    def set_size_request(self, width, height): # real signature unknown; restored from __doc__
        """ set_size_request(self, width:int, height:int) """
        pass

    def set_state(self, state): # real signature unknown; restored from __doc__
        """ set_state(self, state:Gtk.StateType) """
        pass

    def set_state_flags(self, flags, clear): # real signature unknown; restored from __doc__
        """ set_state_flags(self, flags:Gtk.StateFlags, clear:bool) """
        pass

    def set_style(self, style=None): # real signature unknown; restored from __doc__
        """ set_style(self, style:Gtk.Style=None) """
        pass

    def set_support_multidevice(self, support_multidevice): # real signature unknown; restored from __doc__
        """ set_support_multidevice(self, support_multidevice:bool) """
        pass

    def set_template(self, template_bytes): # real signature unknown; restored from __doc__
        """ set_template(self, template_bytes:GLib.Bytes) """
        pass

    def set_template_from_resource(self, resource_name): # real signature unknown; restored from __doc__
        """ set_template_from_resource(self, resource_name:str) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_tooltip_markup(self, markup=None): # real signature unknown; restored from __doc__
        """ set_tooltip_markup(self, markup:str=None) """
        pass

    def set_tooltip_text(self, text=None): # real signature unknown; restored from __doc__
        """ set_tooltip_text(self, text:str=None) """
        pass

    def set_tooltip_window(self, custom_window=None): # real signature unknown; restored from __doc__
        """ set_tooltip_window(self, custom_window:Gtk.Window=None) """
        pass

    def set_valign(self, align): # real signature unknown; restored from __doc__
        """ set_valign(self, align:Gtk.Align) """
        pass

    def set_vexpand(self, expand): # real signature unknown; restored from __doc__
        """ set_vexpand(self, expand:bool) """
        pass

    def set_vexpand_set(self, set): # real signature unknown; restored from __doc__
        """ set_vexpand_set(self, set:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visual(self, visual=None): # real signature unknown; restored from __doc__
        """ set_visual(self, visual:Gdk.Visual=None) """
        pass

    def set_window(self, window): # real signature unknown; restored from __doc__
        """ set_window(self, window:Gdk.Window) """
        pass

    def set_wrap_width(self, width): # real signature unknown; restored from __doc__
        """ set_wrap_width(self, width:int) """
        pass

    def shape_combine_region(self, region=None): # real signature unknown; restored from __doc__
        """ shape_combine_region(self, region:cairo.Region=None) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
        pass

    def show_all(self): # real signature unknown; restored from __doc__
        """ show_all(self) """
        pass

    def show_now(self): # real signature unknown; restored from __doc__
        """ show_now(self) """
        pass

    def size_allocate(self, allocation): # real signature unknown; restored from __doc__
        """ size_allocate(self, allocation:Gdk.Rectangle) """
        pass

    def size_allocate_with_baseline(self, allocation, baseline): # real signature unknown; restored from __doc__
        """ size_allocate_with_baseline(self, allocation:Gdk.Rectangle, baseline:int) """
        pass

    def size_request(self): # real signature unknown; restored from __doc__
        """ size_request(self) -> requisition:Gtk.Requisition """
        pass

    def start_editing(self, event=None): # real signature unknown; restored from __doc__
        """ start_editing(self, event:Gdk.Event=None) """
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

    def style_attach(self): # real signature unknown; restored from __doc__
        """ style_attach(self) """
        pass

    def style_get_property(self, property_name, value=None): # reliably restored by inspect
        # no doc
        pass

    def thaw_child_notify(self): # real signature unknown; restored from __doc__
        """ thaw_child_notify(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def translate_coordinates(*args, **kwargs): # reliably restored by inspect
        """ translate_coordinates(self, dest_widget:Gtk.Widget, src_x:int, src_y:int) -> bool, dest_x:int, dest_y:int """
        pass

    def trigger_tooltip_query(self): # real signature unknown; restored from __doc__
        """ trigger_tooltip_query(self) """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap(self) """
        pass

    def unparent(self): # real signature unknown; restored from __doc__
        """ unparent(self) """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_window(self, window): # real signature unknown; restored from __doc__
        """ unregister_window(self, window:Gdk.Window) """
        pass

    def unset_focus_chain(self): # real signature unknown; restored from __doc__
        """ unset_focus_chain(self) """
        pass

    def unset_state_flags(self, flags): # real signature unknown; restored from __doc__
        """ unset_state_flags(self, flags:Gtk.StateFlags) """
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

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __contains__(self, child): # reliably restored by inspect
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

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
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

    container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000020ee0174580>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ChannelComboBox), '__module__': 'gi.repository.GimpUi', '__gtype__': <GType GimpChannelComboBox (3717481264)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>})"
    __firstlineno__ = 451
    __gdoc__ = "Object GimpChannelComboBox\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nProperties from GimpIntComboBox:\n  ellipsize -> PangoEllipsizeMode: Ellipsize\n    Ellipsize mode for the used text cell renderer\n  label -> gchararray: Label\n    An optional label to be displayed\n  layout -> GimpIntComboBoxLayout: Layout\n    Combo box layout\n  value -> gint: Value\n    Value of active item\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkComboBox:\n  changed ()\n  move-active (GtkScrollType)\n  popup ()\n  popdown () -> gboolean\n  format-entry-text (gchararray) -> gchararray\n\nProperties from GtkComboBox:\n  model -> GtkTreeModel: ComboBox model\n    The model for the combo box\n  wrap-width -> gint: Wrap width\n    Wrap width for laying out the items in a grid\n  row-span-column -> gint: Row span column\n    TreeModel column containing the row span values\n  column-span-column -> gint: Column span column\n    TreeModel column containing the column span values\n  active -> gint: Active item\n    The item which is currently active\n  add-tearoffs -> gboolean: Add tearoffs to menus\n    Whether dropdowns should have a tearoff menu item\n  tearoff-title -> gchararray: Tearoff Title\n    A title that may be displayed by the window manager when the popup is torn-off\n  has-frame -> gboolean: Has Frame\n    Whether the combo box draws a frame around the child\n  popup-shown -> gboolean: Popup shown\n    Whether the combo's dropdown is shown\n  button-sensitivity -> GtkSensitivityType: Button Sensitivity\n    Whether the dropdown button is sensitive when the model is empty\n  has-entry -> gboolean: Has Entry\n    Whether combo box has an entry\n  entry-text-column -> gint: Entry Text Column\n    The column in the combo box's model to associate with strings from the entry if the combo was created with #GtkComboBox:has-entry = %TRUE\n  popup-fixed-width -> gboolean: Popup Fixed Width\n    Whether the popup's width should be a fixed width matching the allocated width of the combo box\n  id-column -> gint: ID Column\n    The column in the combo box's model that provides string IDs for the values in the model\n  active-id -> gchararray: Active id\n    The value of the id column for the active row\n  cell-area -> GtkCellArea: Cell Area\n    The GtkCellArea used to layout cells\n\nSignals from GtkCellEditable:\n  editing-done ()\n  remove-widget ()\n\nSignals from GtkContainer:\n  add (GtkWidget)\n  remove (GtkWidget)\n  check-resize ()\n  set-focus-child (GtkWidget)\n\nProperties from GtkContainer:\n  border-width -> guint: Border width\n    The width of the empty border outside the containers children\n  resize-mode -> GtkResizeMode: Resize mode\n    Specify how resize events are handled\n  child -> GtkWidget: Child\n    Can be used to add a new child to the container\n\nSignals from GtkWidget:\n  direction-changed (GtkTextDirection)\n  state-changed (GtkStateType)\n  composited-changed ()\n  destroy ()\n  show ()\n  hide ()\n  map ()\n  unmap ()\n  realize ()\n  unrealize ()\n  size-allocate (GdkRectangle)\n  state-flags-changed (GtkStateFlags)\n  parent-set (GtkWidget)\n  hierarchy-changed (GtkWidget)\n  style-set (GtkStyle)\n  style-updated ()\n  grab-notify (gboolean)\n  child-notify (GParam)\n  draw (CairoContext) -> gboolean\n  mnemonic-activate (gboolean) -> gboolean\n  grab-focus ()\n  focus (GtkDirectionType) -> gboolean\n  move-focus (GtkDirectionType)\n  keynav-failed (GtkDirectionType) -> gboolean\n  event (GdkEvent) -> gboolean\n  event-after (GdkEvent)\n  button-press-event (GdkEvent) -> gboolean\n  button-release-event (GdkEvent) -> gboolean\n  touch-event (GdkEvent) -> gboolean\n  scroll-event (GdkEvent) -> gboolean\n  motion-notify-event (GdkEvent) -> gboolean\n  delete-event (GdkEvent) -> gboolean\n  destroy-event (GdkEvent) -> gboolean\n  key-press-event (GdkEvent) -> gboolean\n  key-release-event (GdkEvent) -> gboolean\n  enter-notify-event (GdkEvent) -> gboolean\n  leave-notify-event (GdkEvent) -> gboolean\n  configure-event (GdkEvent) -> gboolean\n  focus-in-event (GdkEvent) -> gboolean\n  focus-out-event (GdkEvent) -> gboolean\n  map-event (GdkEvent) -> gboolean\n  unmap-event (GdkEvent) -> gboolean\n  property-notify-event (GdkEvent) -> gboolean\n  selection-clear-event (GdkEvent) -> gboolean\n  selection-request-event (GdkEvent) -> gboolean\n  selection-notify-event (GdkEvent) -> gboolean\n  selection-received (GtkSelectionData, guint)\n  selection-get (GtkSelectionData, guint, guint)\n  proximity-in-event (GdkEvent) -> gboolean\n  proximity-out-event (GdkEvent) -> gboolean\n  drag-leave (GdkDragContext, guint)\n  drag-begin (GdkDragContext)\n  drag-end (GdkDragContext)\n  drag-data-delete (GdkDragContext)\n  drag-failed (GdkDragContext, GtkDragResult) -> gboolean\n  drag-motion (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-drop (GdkDragContext, gint, gint, guint) -> gboolean\n  drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)\n  drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)\n  visibility-notify-event (GdkEvent) -> gboolean\n  window-state-event (GdkEvent) -> gboolean\n  damage-event (GdkEvent) -> gboolean\n  grab-broken-event (GdkEvent) -> gboolean\n  query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean\n  popup-menu () -> gboolean\n  show-help (GtkWidgetHelpType) -> gboolean\n  accel-closures-changed ()\n  screen-changed (GdkScreen)\n  can-activate-accel (guint) -> gboolean\n\nProperties from GtkWidget:\n  name -> gchararray: Widget name\n    The name of the widget\n  parent -> GtkContainer: Parent widget\n    The parent widget of this widget. Must be a Container widget\n  width-request -> gint: Width request\n    Override for width request of the widget, or -1 if natural request should be used\n  height-request -> gint: Height request\n    Override for height request of the widget, or -1 if natural request should be used\n  visible -> gboolean: Visible\n    Whether the widget is visible\n  sensitive -> gboolean: Sensitive\n    Whether the widget responds to input\n  app-paintable -> gboolean: Application paintable\n    Whether the application will paint directly on the widget\n  can-focus -> gboolean: Can focus\n    Whether the widget can accept the input focus\n  has-focus -> gboolean: Has focus\n    Whether the widget has the input focus\n  is-focus -> gboolean: Is focus\n    Whether the widget is the focus widget within the toplevel\n  focus-on-click -> gboolean: Focus on click\n    Whether the widget should grab focus when it is clicked with the mouse\n  can-default -> gboolean: Can default\n    Whether the widget can be the default widget\n  has-default -> gboolean: Has default\n    Whether the widget is the default widget\n  receives-default -> gboolean: Receives default\n    If TRUE, the widget will receive the default action when it is focused\n  composite-child -> gboolean: Composite child\n    Whether the widget is part of a composite widget\n  style -> GtkStyle: Style\n    The style of the widget, which contains information about how it will look (colors etc)\n  events -> GdkEventMask: Events\n    The event mask that decides what kind of GdkEvents this widget gets\n  no-show-all -> gboolean: No show all\n    Whether gtk_widget_show_all() should not affect this widget\n  has-tooltip -> gboolean: Has tooltip\n    Whether this widget has a tooltip\n  tooltip-markup -> gchararray: Tooltip markup\n    The contents of the tooltip for this widget\n  tooltip-text -> gchararray: Tooltip Text\n    The contents of the tooltip for this widget\n  window -> GdkWindow: Window\n    The widget's window if it is realized\n  opacity -> gdouble: Opacity for Widget\n    The opacity of the widget, from 0 to 1\n  double-buffered -> gboolean: Double Buffered\n    Whether the widget is double buffered\n  halign -> GtkAlign: Horizontal Alignment\n    How to position in extra horizontal space\n  valign -> GtkAlign: Vertical Alignment\n    How to position in extra vertical space\n  margin-left -> gint: Margin on Left\n    Pixels of extra space on the left side\n  margin-right -> gint: Margin on Right\n    Pixels of extra space on the right side\n  margin-start -> gint: Margin on Start\n    Pixels of extra space on the start\n  margin-end -> gint: Margin on End\n    Pixels of extra space on the end\n  margin-top -> gint: Margin on Top\n    Pixels of extra space on the top side\n  margin-bottom -> gint: Margin on Bottom\n    Pixels of extra space on the bottom side\n  margin -> gint: All Margins\n    Pixels of extra space on all four sides\n  hexpand -> gboolean: Horizontal Expand\n    Whether widget wants more horizontal space\n  vexpand -> gboolean: Vertical Expand\n    Whether widget wants more vertical space\n  hexpand-set -> gboolean: Horizontal Expand Set\n    Whether to use the hexpand property\n  vexpand-set -> gboolean: Vertical Expand Set\n    Whether to use the vexpand property\n  expand -> gboolean: Expand Both\n    Whether widget wants to expand in both directions\n  scale-factor -> gint: Scale factor\n    The scaling factor of the window\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpChannelComboBox (3717481264)>'
    __info__ = ObjectInfo(ChannelComboBox)
    __static_attributes__ = ()


