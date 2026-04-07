# encoding: utf-8
# module gi.repository.Gimp
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GExiv2 as __gi_overrides_GExiv2
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class Image(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Image(**properties)
        new(width:int, height:int, type:Gimp.ImageBaseType) -> Gimp.Image
        new_with_precision(width:int, height:int, type:Gimp.ImageBaseType, precision:Gimp.Precision) -> Gimp.Image
    """
    def add_hguide(self, yposition): # real signature unknown; restored from __doc__
        """ add_hguide(self, yposition:int) -> int """
        return 0

    def add_sample_point(self, position_x, position_y): # real signature unknown; restored from __doc__
        """ add_sample_point(self, position_x:int, position_y:int) -> int """
        return 0

    def add_vguide(self, xposition): # real signature unknown; restored from __doc__
        """ add_vguide(self, xposition:int) -> int """
        return 0

    def attach_parasite(self, parasite): # real signature unknown; restored from __doc__
        """ attach_parasite(self, parasite:Gimp.Parasite) -> bool """
        return False

    def autocrop(self, drawable=None): # real signature unknown; restored from __doc__
        """ autocrop(self, drawable:Gimp.Drawable=None) -> bool """
        return False

    def autocrop_selected_layers(self, drawable=None): # real signature unknown; restored from __doc__
        """ autocrop_selected_layers(self, drawable:Gimp.Drawable=None) -> bool """
        return False

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clean_all(self): # real signature unknown; restored from __doc__
        """ clean_all(self) -> bool """
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

    def convert_color_profile(self, profile, intent, bpc): # real signature unknown; restored from __doc__
        """ convert_color_profile(self, profile:Gimp.ColorProfile, intent:Gimp.ColorRenderingIntent, bpc:bool) -> bool """
        return False

    def convert_color_profile_from_file(self, file, intent, bpc): # real signature unknown; restored from __doc__
        """ convert_color_profile_from_file(self, file:Gio.File, intent:Gimp.ColorRenderingIntent, bpc:bool) -> bool """
        return False

    def convert_grayscale(self): # real signature unknown; restored from __doc__
        """ convert_grayscale(self) -> bool """
        return False

    def convert_indexed(self, dither_type, palette_type, num_cols, alpha_dither, remove_unused, palette): # real signature unknown; restored from __doc__
        """ convert_indexed(self, dither_type:Gimp.ConvertDitherType, palette_type:Gimp.ConvertPaletteType, num_cols:int, alpha_dither:bool, remove_unused:bool, palette:str) -> bool """
        return False

    def convert_precision(self, precision): # real signature unknown; restored from __doc__
        """ convert_precision(self, precision:Gimp.Precision) -> bool """
        return False

    def convert_rgb(self): # real signature unknown; restored from __doc__
        """ convert_rgb(self) -> bool """
        return False

    def convert_set_dither_matrix(self, width, height, matrix): # real signature unknown; restored from __doc__
        """ convert_set_dither_matrix(width:int, height:int, matrix:GLib.Bytes) -> bool """
        return False

    def crop(self, new_width, new_height, offx, offy): # real signature unknown; restored from __doc__
        """ crop(self, new_width:int, new_height:int, offx:int, offy:int) -> bool """
        return False

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
        return False

    def delete_guide(self, guide): # real signature unknown; restored from __doc__
        """ delete_guide(self, guide:int) -> bool """
        return False

    def delete_sample_point(self, sample_point): # real signature unknown; restored from __doc__
        """ delete_sample_point(self, sample_point:int) -> bool """
        return False

    def detach_parasite(self, name): # real signature unknown; restored from __doc__
        """ detach_parasite(self, name:str) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> Gimp.Image """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def export_path_to_file(self, file, path=None): # real signature unknown; restored from __doc__
        """ export_path_to_file(self, file:Gio.File, path:Gimp.Path=None) -> bool """
        return False

    def export_path_to_string(self, path=None): # real signature unknown; restored from __doc__
        """ export_path_to_string(self, path:Gimp.Path=None) -> str """
        return ""

    def find_next_guide(self, guide): # real signature unknown; restored from __doc__
        """ find_next_guide(self, guide:int) -> int """
        return 0

    def find_next_sample_point(self, sample_point): # real signature unknown; restored from __doc__
        """ find_next_sample_point(self, sample_point:int) -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def flatten(self): # real signature unknown; restored from __doc__
        """ flatten(self) -> Gimp.Layer """
        pass

    def flip(self, flip_type): # real signature unknown; restored from __doc__
        """ flip(self, flip_type:Gimp.OrientationType) -> bool """
        return False

    def floating_sel_attached_to(self): # real signature unknown; restored from __doc__
        """ floating_sel_attached_to(self) -> Gimp.Drawable """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def freeze_channels(self): # real signature unknown; restored from __doc__
        """ freeze_channels(self) -> bool """
        return False

    def freeze_layers(self): # real signature unknown; restored from __doc__
        """ freeze_layers(self) -> bool """
        return False

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

    def freeze_paths(self): # real signature unknown; restored from __doc__
        """ freeze_paths(self) -> bool """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_base_type(self): # real signature unknown; restored from __doc__
        """ get_base_type(self) -> Gimp.ImageBaseType """
        pass

    def get_by_id(self, image_id): # real signature unknown; restored from __doc__
        """ get_by_id(image_id:int) -> Gimp.Image or None """
        pass

    def get_channels(self): # real signature unknown; restored from __doc__
        """ get_channels(self) -> list """
        return []

    def get_channel_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_channel_by_name(self, name:str) -> Gimp.Channel """
        pass

    def get_channel_by_tattoo(self, tattoo): # real signature unknown; restored from __doc__
        """ get_channel_by_tattoo(self, tattoo:int) -> Gimp.Channel """
        pass

    def get_color_profile(self): # real signature unknown; restored from __doc__
        """ get_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_component_active(self, component): # real signature unknown; restored from __doc__
        """ get_component_active(self, component:Gimp.ChannelType) -> bool """
        return False

    def get_component_visible(self, component): # real signature unknown; restored from __doc__
        """ get_component_visible(self, component:Gimp.ChannelType) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_new_layer_mode(self): # real signature unknown; restored from __doc__
        """ get_default_new_layer_mode(self) -> Gimp.LayerMode """
        pass

    def get_effective_color_profile(self): # real signature unknown; restored from __doc__
        """ get_effective_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_exported_file(self): # real signature unknown; restored from __doc__
        """ get_exported_file(self) -> Gio.File """
        pass

    def get_file(self): # real signature unknown; restored from __doc__
        """ get_file(self) -> Gio.File """
        pass

    def get_floating_sel(self): # real signature unknown; restored from __doc__
        """ get_floating_sel(self) -> Gimp.Layer """
        pass

    def get_guide_orientation(self, guide): # real signature unknown; restored from __doc__
        """ get_guide_orientation(self, guide:int) -> Gimp.OrientationType """
        pass

    def get_guide_position(self, guide): # real signature unknown; restored from __doc__
        """ get_guide_position(self, guide:int) -> int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_imported_file(self): # real signature unknown; restored from __doc__
        """ get_imported_file(self) -> Gio.File """
        pass

    def get_item_position(self, item): # real signature unknown; restored from __doc__
        """ get_item_position(self, item:Gimp.Item) -> int """
        return 0

    def get_layers(self): # real signature unknown; restored from __doc__
        """ get_layers(self) -> list """
        return []

    def get_layer_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_layer_by_name(self, name:str) -> Gimp.Layer """
        pass

    def get_layer_by_tattoo(self, tattoo): # real signature unknown; restored from __doc__
        """ get_layer_by_tattoo(self, tattoo:int) -> Gimp.Layer """
        pass

    def get_metadata(self): # real signature unknown; restored from __doc__
        """ get_metadata(self) -> Gimp.Metadata or None """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_palette(self): # real signature unknown; restored from __doc__
        """ get_palette(self) -> Gimp.Palette """
        pass

    def get_parasite(self, name): # real signature unknown; restored from __doc__
        """ get_parasite(self, name:str) -> Gimp.Parasite """
        pass

    def get_parasite_list(self): # real signature unknown; restored from __doc__
        """ get_parasite_list(self) -> list """
        return []

    def get_paths(self): # real signature unknown; restored from __doc__
        """ get_paths(self) -> list """
        return []

    def get_path_by_name(self, name): # real signature unknown; restored from __doc__
        """ get_path_by_name(self, name:str) -> Gimp.Path """
        pass

    def get_path_by_tattoo(self, tattoo): # real signature unknown; restored from __doc__
        """ get_path_by_tattoo(self, tattoo:int) -> Gimp.Path """
        pass

    def get_precision(self): # real signature unknown; restored from __doc__
        """ get_precision(self) -> Gimp.Precision """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> bool, xresolution:float, yresolution:float """
        return False

    def get_sample_point_position(self, sample_point): # real signature unknown; restored from __doc__
        """ get_sample_point_position(self, sample_point:int) -> int, position_y:int """
        return 0

    def get_selected_channels(self): # real signature unknown; restored from __doc__
        """ get_selected_channels(self) -> list """
        return []

    def get_selected_drawables(self): # real signature unknown; restored from __doc__
        """ get_selected_drawables(self) -> list """
        return []

    def get_selected_layers(self): # real signature unknown; restored from __doc__
        """ get_selected_layers(self) -> list """
        return []

    def get_selected_paths(self): # real signature unknown; restored from __doc__
        """ get_selected_paths(self) -> list """
        return []

    def get_selection(self): # real signature unknown; restored from __doc__
        """ get_selection(self) -> Gimp.Selection """
        pass

    def get_simulation_bpc(self): # real signature unknown; restored from __doc__
        """ get_simulation_bpc(self) -> bool """
        return False

    def get_simulation_intent(self): # real signature unknown; restored from __doc__
        """ get_simulation_intent(self) -> Gimp.ColorRenderingIntent """
        pass

    def get_simulation_profile(self): # real signature unknown; restored from __doc__
        """ get_simulation_profile(self) -> Gimp.ColorProfile """
        pass

    def get_tattoo_state(self): # real signature unknown; restored from __doc__
        """ get_tattoo_state(self) -> int """
        return 0

    def get_thumbnail(self, width, height, alpha): # real signature unknown; restored from __doc__
        """ get_thumbnail(self, width:int, height:int, alpha:Gimp.PixbufTransparency) -> GdkPixbuf.Pixbuf """
        pass

    def get_thumbnail_data(self, width, height): # real signature unknown; restored from __doc__
        """ get_thumbnail_data(self, width:int, height:int) -> GLib.Bytes, width:int, height:int, bpp:int """
        pass

    def get_unit(self): # real signature unknown; restored from __doc__
        """ get_unit(self) -> Gimp.Unit """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_xcf_file(self): # real signature unknown; restored from __doc__
        """ get_xcf_file(self) -> Gio.File """
        pass

    def grid_get_background_color(self): # real signature unknown; restored from __doc__
        """ grid_get_background_color(self) -> Gegl.Color """
        pass

    def grid_get_foreground_color(self): # real signature unknown; restored from __doc__
        """ grid_get_foreground_color(self) -> Gegl.Color """
        pass

    def grid_get_offset(self): # real signature unknown; restored from __doc__
        """ grid_get_offset(self) -> bool, xoffset:float, yoffset:float """
        return False

    def grid_get_spacing(self): # real signature unknown; restored from __doc__
        """ grid_get_spacing(self) -> bool, xspacing:float, yspacing:float """
        return False

    def grid_get_style(self): # real signature unknown; restored from __doc__
        """ grid_get_style(self) -> Gimp.GridStyle """
        pass

    def grid_set_background_color(self, bgcolor): # real signature unknown; restored from __doc__
        """ grid_set_background_color(self, bgcolor:Gegl.Color) -> bool """
        return False

    def grid_set_foreground_color(self, fgcolor): # real signature unknown; restored from __doc__
        """ grid_set_foreground_color(self, fgcolor:Gegl.Color) -> bool """
        return False

    def grid_set_offset(self, xoffset, yoffset): # real signature unknown; restored from __doc__
        """ grid_set_offset(self, xoffset:float, yoffset:float) -> bool """
        return False

    def grid_set_spacing(self, xspacing, yspacing): # real signature unknown; restored from __doc__
        """ grid_set_spacing(self, xspacing:float, yspacing:float) -> bool """
        return False

    def grid_set_style(self, style): # real signature unknown; restored from __doc__
        """ grid_set_style(self, style:Gimp.GridStyle) -> bool """
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

    def id_is_valid(self, image_id): # real signature unknown; restored from __doc__
        """ id_is_valid(image_id:int) -> bool """
        return False

    def import_paths_from_file(self, file, merge, scale): # real signature unknown; restored from __doc__
        """ import_paths_from_file(self, file:Gio.File, merge:bool, scale:bool) -> bool, paths:list """
        return False

    def import_paths_from_string(self, string, length, merge, scale): # real signature unknown; restored from __doc__
        """ import_paths_from_string(self, string:str, length:int, merge:bool, scale:bool) -> bool, paths:list """
        return False

    def insert_channel(self, channel, parent=None, position): # real signature unknown; restored from __doc__
        """ insert_channel(self, channel:Gimp.Channel, parent:Gimp.Channel=None, position:int) -> bool """
        return False

    def insert_layer(self, layer, parent=None, position): # real signature unknown; restored from __doc__
        """ insert_layer(self, layer:Gimp.Layer, parent:Gimp.Layer=None, position:int) -> bool """
        return False

    def insert_path(self, path, parent=None, position): # real signature unknown; restored from __doc__
        """ insert_path(self, path:Gimp.Path, parent:Gimp.Path=None, position:int) -> bool """
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

    def is_dirty(self): # real signature unknown; restored from __doc__
        """ is_dirty(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def lower_item(self, item): # real signature unknown; restored from __doc__
        """ lower_item(self, item:Gimp.Item) -> bool """
        return False

    def lower_item_to_bottom(self, item): # real signature unknown; restored from __doc__
        """ lower_item_to_bottom(self, item:Gimp.Item) -> bool """
        return False

    def merge_down(self, merge_layer, merge_type): # real signature unknown; restored from __doc__
        """ merge_down(self, merge_layer:Gimp.Layer, merge_type:Gimp.MergeType) -> Gimp.Layer """
        pass

    def merge_visible_layers(self, merge_type): # real signature unknown; restored from __doc__
        """ merge_visible_layers(self, merge_type:Gimp.MergeType) -> Gimp.Layer """
        pass

    def metadata_load_thumbnail(self, file): # real signature unknown; restored from __doc__
        """ metadata_load_thumbnail(file:Gio.File) -> Gimp.Image or None """
        pass

    def metadata_save_filter(self, mime_type, metadata, flags, file): # real signature unknown; restored from __doc__
        """ metadata_save_filter(self, mime_type:str, metadata:Gimp.Metadata, flags:Gimp.MetadataSaveFlags, file:Gio.File) -> Gimp.Metadata """
        pass

    def metadata_save_prepare(self, mime_type, suggested_flags): # real signature unknown; restored from __doc__
        """ metadata_save_prepare(self, mime_type:str, suggested_flags:Gimp.MetadataSaveFlags) -> Gimp.Metadata """
        pass

    @classmethod
    def new(cls, width, height, type): # real signature unknown; restored from __doc__
        """ new(width:int, height:int, type:Gimp.ImageBaseType) -> Gimp.Image """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_with_precision(cls, width, height, type, precision): # real signature unknown; restored from __doc__
        """ new_with_precision(width:int, height:int, type:Gimp.ImageBaseType, precision:Gimp.Precision) -> Gimp.Image """
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

    def pick_color(self, drawables, x, y, sample_merged, sample_average, average_radius): # real signature unknown; restored from __doc__
        """ pick_color(self, drawables:list, x:float, y:float, sample_merged:bool, sample_average:bool, average_radius:float) -> bool, color:Gegl.Color """
        return False

    def pick_correlate_layer(self, x, y): # real signature unknown; restored from __doc__
        """ pick_correlate_layer(self, x:int, y:int) -> Gimp.Layer """
        pass

    def policy_color_profile(self, interactive): # real signature unknown; restored from __doc__
        """ policy_color_profile(self, interactive:bool) -> bool """
        return False

    def policy_rotate(self, interactive): # real signature unknown; restored from __doc__
        """ policy_rotate(self, interactive:bool) -> bool """
        return False

    def raise_item(self, item): # real signature unknown; restored from __doc__
        """ raise_item(self, item:Gimp.Item) -> bool """
        return False

    def raise_item_to_top(self, item): # real signature unknown; restored from __doc__
        """ raise_item_to_top(self, item:Gimp.Item) -> bool """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_channel(self, channel): # real signature unknown; restored from __doc__
        """ remove_channel(self, channel:Gimp.Channel) -> bool """
        return False

    def remove_layer(self, layer): # real signature unknown; restored from __doc__
        """ remove_layer(self, layer:Gimp.Layer) -> bool """
        return False

    def remove_path(self, path): # real signature unknown; restored from __doc__
        """ remove_path(self, path:Gimp.Path) -> bool """
        return False

    def reorder_item(self, item, parent=None, position): # real signature unknown; restored from __doc__
        """ reorder_item(self, item:Gimp.Item, parent:Gimp.Item=None, position:int) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def resize(self, new_width, new_height, offx, offy): # real signature unknown; restored from __doc__
        """ resize(self, new_width:int, new_height:int, offx:int, offy:int) -> bool """
        return False

    def resize_to_layers(self): # real signature unknown; restored from __doc__
        """ resize_to_layers(self) -> bool """
        return False

    def rotate(self, rotate_type): # real signature unknown; restored from __doc__
        """ rotate(self, rotate_type:Gimp.RotationType) -> bool """
        return False

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def scale(self, new_width, new_height): # real signature unknown; restored from __doc__
        """ scale(self, new_width:int, new_height:int) -> bool """
        return False

    def select_color(self, operation, drawable, color): # real signature unknown; restored from __doc__
        """ select_color(self, operation:Gimp.ChannelOps, drawable:Gimp.Drawable, color:Gegl.Color) -> bool """
        return False

    def select_contiguous_color(self, operation, drawable, x, y): # real signature unknown; restored from __doc__
        """ select_contiguous_color(self, operation:Gimp.ChannelOps, drawable:Gimp.Drawable, x:float, y:float) -> bool """
        return False

    def select_ellipse(self, operation, x, y, width, height): # real signature unknown; restored from __doc__
        """ select_ellipse(self, operation:Gimp.ChannelOps, x:float, y:float, width:float, height:float) -> bool """
        return False

    def select_item(self, operation, item): # real signature unknown; restored from __doc__
        """ select_item(self, operation:Gimp.ChannelOps, item:Gimp.Item) -> bool """
        return False

    def select_polygon(self, operation, segs): # real signature unknown; restored from __doc__
        """ select_polygon(self, operation:Gimp.ChannelOps, segs:list) -> bool """
        return False

    def select_rectangle(self, operation, x, y, width, height): # real signature unknown; restored from __doc__
        """ select_rectangle(self, operation:Gimp.ChannelOps, x:float, y:float, width:float, height:float) -> bool """
        return False

    def select_round_rectangle(self, operation, x, y, width, height, corner_radius_x, corner_radius_y): # real signature unknown; restored from __doc__
        """ select_round_rectangle(self, operation:Gimp.ChannelOps, x:float, y:float, width:float, height:float, corner_radius_x:float, corner_radius_y:float) -> bool """
        return False

    def set_color_profile(self, profile=None): # real signature unknown; restored from __doc__
        """ set_color_profile(self, profile:Gimp.ColorProfile=None) -> bool """
        return False

    def set_color_profile_from_file(self, file): # real signature unknown; restored from __doc__
        """ set_color_profile_from_file(self, file:Gio.File) -> bool """
        return False

    def set_component_active(self, component, active): # real signature unknown; restored from __doc__
        """ set_component_active(self, component:Gimp.ChannelType, active:bool) -> bool """
        return False

    def set_component_visible(self, component, visible): # real signature unknown; restored from __doc__
        """ set_component_visible(self, component:Gimp.ChannelType, visible:bool) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_file(self, file): # real signature unknown; restored from __doc__
        """ set_file(self, file:Gio.File) -> bool """
        return False

    def set_metadata(self, metadata): # real signature unknown; restored from __doc__
        """ set_metadata(self, metadata:Gimp.Metadata) -> bool """
        return False

    def set_palette(self, new_palette): # real signature unknown; restored from __doc__
        """ set_palette(self, new_palette:Gimp.Palette) -> Gimp.Palette """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, xresolution, yresolution): # real signature unknown; restored from __doc__
        """ set_resolution(self, xresolution:float, yresolution:float) -> bool """
        return False

    def set_selected_channels(self, channels): # real signature unknown; restored from __doc__
        """ set_selected_channels(self, channels:list) -> bool """
        return False

    def set_selected_layers(self, layers): # real signature unknown; restored from __doc__
        """ set_selected_layers(self, layers:list) -> bool """
        return False

    def set_selected_paths(self, paths): # real signature unknown; restored from __doc__
        """ set_selected_paths(self, paths:list) -> bool """
        return False

    def set_simulation_bpc(self, bpc): # real signature unknown; restored from __doc__
        """ set_simulation_bpc(self, bpc:bool) -> bool """
        return False

    def set_simulation_intent(self, intent): # real signature unknown; restored from __doc__
        """ set_simulation_intent(self, intent:Gimp.ColorRenderingIntent) -> bool """
        return False

    def set_simulation_profile(self, profile=None): # real signature unknown; restored from __doc__
        """ set_simulation_profile(self, profile:Gimp.ColorProfile=None) -> bool """
        return False

    def set_simulation_profile_from_file(self, file): # real signature unknown; restored from __doc__
        """ set_simulation_profile_from_file(self, file:Gio.File) -> bool """
        return False

    def set_tattoo_state(self, tattoo_state): # real signature unknown; restored from __doc__
        """ set_tattoo_state(self, tattoo_state:int) -> bool """
        return False

    def set_unit(self, unit): # real signature unknown; restored from __doc__
        """ set_unit(self, unit:Gimp.Unit) -> bool """
        return False

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

    def take_selected_channels(self, channels): # real signature unknown; restored from __doc__
        """ take_selected_channels(self, channels:list) -> bool """
        return False

    def take_selected_layers(self, layers): # real signature unknown; restored from __doc__
        """ take_selected_layers(self, layers:list) -> bool """
        return False

    def take_selected_paths(self, paths): # real signature unknown; restored from __doc__
        """ take_selected_paths(self, paths:list) -> bool """
        return False

    def thaw_channels(self): # real signature unknown; restored from __doc__
        """ thaw_channels(self) -> bool """
        return False

    def thaw_layers(self): # real signature unknown; restored from __doc__
        """ thaw_layers(self) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def thaw_paths(self): # real signature unknown; restored from __doc__
        """ thaw_paths(self) -> bool """
        return False

    def undo_disable(self): # real signature unknown; restored from __doc__
        """ undo_disable(self) -> bool """
        return False

    def undo_enable(self): # real signature unknown; restored from __doc__
        """ undo_enable(self) -> bool """
        return False

    def undo_freeze(self): # real signature unknown; restored from __doc__
        """ undo_freeze(self) -> bool """
        return False

    def undo_group_end(self): # real signature unknown; restored from __doc__
        """ undo_group_end(self) -> bool """
        return False

    def undo_group_start(self): # real signature unknown; restored from __doc__
        """ undo_group_start(self) -> bool """
        return False

    def undo_is_enabled(self): # real signature unknown; restored from __doc__
        """ undo_is_enabled(self) -> bool """
        return False

    def undo_thaw(self): # real signature unknown; restored from __doc__
        """ undo_thaw(self) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset_active_channel(self): # real signature unknown; restored from __doc__
        """ unset_active_channel(self) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001268f3b0310>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Image), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpImage (2359059520)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_with_precision': <classmethod(gi.FunctionInfo(new_with_precision))>, 'convert_set_dither_matrix': <staticmethod(gi.FunctionInfo(convert_set_dither_matrix))>, 'get_by_id': <staticmethod(gi.FunctionInfo(get_by_id))>, 'id_is_valid': <staticmethod(gi.FunctionInfo(id_is_valid))>, 'metadata_load_thumbnail': <staticmethod(gi.FunctionInfo(metadata_load_thumbnail))>, 'add_hguide': gi.FunctionInfo(add_hguide), 'add_sample_point': gi.FunctionInfo(add_sample_point), 'add_vguide': gi.FunctionInfo(add_vguide), 'attach_parasite': gi.FunctionInfo(attach_parasite), 'autocrop': gi.FunctionInfo(autocrop), 'autocrop_selected_layers': gi.FunctionInfo(autocrop_selected_layers), 'clean_all': gi.FunctionInfo(clean_all), 'convert_color_profile': gi.FunctionInfo(convert_color_profile), 'convert_color_profile_from_file': gi.FunctionInfo(convert_color_profile_from_file), 'convert_grayscale': gi.FunctionInfo(convert_grayscale), 'convert_indexed': gi.FunctionInfo(convert_indexed), 'convert_precision': gi.FunctionInfo(convert_precision), 'convert_rgb': gi.FunctionInfo(convert_rgb), 'crop': gi.FunctionInfo(crop), 'delete': gi.FunctionInfo(delete), 'delete_guide': gi.FunctionInfo(delete_guide), 'delete_sample_point': gi.FunctionInfo(delete_sample_point), 'detach_parasite': gi.FunctionInfo(detach_parasite), 'duplicate': gi.FunctionInfo(duplicate), 'export_path_to_file': gi.FunctionInfo(export_path_to_file), 'export_path_to_string': gi.FunctionInfo(export_path_to_string), 'find_next_guide': gi.FunctionInfo(find_next_guide), 'find_next_sample_point': gi.FunctionInfo(find_next_sample_point), 'flatten': gi.FunctionInfo(flatten), 'flip': gi.FunctionInfo(flip), 'floating_sel_attached_to': gi.FunctionInfo(floating_sel_attached_to), 'freeze_channels': gi.FunctionInfo(freeze_channels), 'freeze_layers': gi.FunctionInfo(freeze_layers), 'freeze_paths': gi.FunctionInfo(freeze_paths), 'get_base_type': gi.FunctionInfo(get_base_type), 'get_channel_by_name': gi.FunctionInfo(get_channel_by_name), 'get_channel_by_tattoo': gi.FunctionInfo(get_channel_by_tattoo), 'get_channels': gi.FunctionInfo(get_channels), 'get_color_profile': gi.FunctionInfo(get_color_profile), 'get_component_active': gi.FunctionInfo(get_component_active), 'get_component_visible': gi.FunctionInfo(get_component_visible), 'get_default_new_layer_mode': gi.FunctionInfo(get_default_new_layer_mode), 'get_effective_color_profile': gi.FunctionInfo(get_effective_color_profile), 'get_exported_file': gi.FunctionInfo(get_exported_file), 'get_file': gi.FunctionInfo(get_file), 'get_floating_sel': gi.FunctionInfo(get_floating_sel), 'get_guide_orientation': gi.FunctionInfo(get_guide_orientation), 'get_guide_position': gi.FunctionInfo(get_guide_position), 'get_height': gi.FunctionInfo(get_height), 'get_id': gi.FunctionInfo(get_id), 'get_imported_file': gi.FunctionInfo(get_imported_file), 'get_item_position': gi.FunctionInfo(get_item_position), 'get_layer_by_name': gi.FunctionInfo(get_layer_by_name), 'get_layer_by_tattoo': gi.FunctionInfo(get_layer_by_tattoo), 'get_layers': gi.FunctionInfo(get_layers), 'get_metadata': gi.FunctionInfo(get_metadata), 'get_name': gi.FunctionInfo(get_name), 'get_palette': gi.FunctionInfo(get_palette), 'get_parasite': gi.FunctionInfo(get_parasite), 'get_parasite_list': gi.FunctionInfo(get_parasite_list), 'get_path_by_name': gi.FunctionInfo(get_path_by_name), 'get_path_by_tattoo': gi.FunctionInfo(get_path_by_tattoo), 'get_paths': gi.FunctionInfo(get_paths), 'get_precision': gi.FunctionInfo(get_precision), 'get_resolution': gi.FunctionInfo(get_resolution), 'get_sample_point_position': gi.FunctionInfo(get_sample_point_position), 'get_selected_channels': gi.FunctionInfo(get_selected_channels), 'get_selected_drawables': gi.FunctionInfo(get_selected_drawables), 'get_selected_layers': gi.FunctionInfo(get_selected_layers), 'get_selected_paths': gi.FunctionInfo(get_selected_paths), 'get_selection': gi.FunctionInfo(get_selection), 'get_simulation_bpc': gi.FunctionInfo(get_simulation_bpc), 'get_simulation_intent': gi.FunctionInfo(get_simulation_intent), 'get_simulation_profile': gi.FunctionInfo(get_simulation_profile), 'get_tattoo_state': gi.FunctionInfo(get_tattoo_state), 'get_thumbnail': gi.FunctionInfo(get_thumbnail), 'get_thumbnail_data': gi.FunctionInfo(get_thumbnail_data), 'get_unit': gi.FunctionInfo(get_unit), 'get_width': gi.FunctionInfo(get_width), 'get_xcf_file': gi.FunctionInfo(get_xcf_file), 'grid_get_background_color': gi.FunctionInfo(grid_get_background_color), 'grid_get_foreground_color': gi.FunctionInfo(grid_get_foreground_color), 'grid_get_offset': gi.FunctionInfo(grid_get_offset), 'grid_get_spacing': gi.FunctionInfo(grid_get_spacing), 'grid_get_style': gi.FunctionInfo(grid_get_style), 'grid_set_background_color': gi.FunctionInfo(grid_set_background_color), 'grid_set_foreground_color': gi.FunctionInfo(grid_set_foreground_color), 'grid_set_offset': gi.FunctionInfo(grid_set_offset), 'grid_set_spacing': gi.FunctionInfo(grid_set_spacing), 'grid_set_style': gi.FunctionInfo(grid_set_style), 'import_paths_from_file': gi.FunctionInfo(import_paths_from_file), 'import_paths_from_string': gi.FunctionInfo(import_paths_from_string), 'insert_channel': gi.FunctionInfo(insert_channel), 'insert_layer': gi.FunctionInfo(insert_layer), 'insert_path': gi.FunctionInfo(insert_path), 'is_dirty': gi.FunctionInfo(is_dirty), 'is_valid': gi.FunctionInfo(is_valid), 'lower_item': gi.FunctionInfo(lower_item), 'lower_item_to_bottom': gi.FunctionInfo(lower_item_to_bottom), 'merge_down': gi.FunctionInfo(merge_down), 'merge_visible_layers': gi.FunctionInfo(merge_visible_layers), 'metadata_save_filter': gi.FunctionInfo(metadata_save_filter), 'metadata_save_prepare': gi.FunctionInfo(metadata_save_prepare), 'pick_color': gi.FunctionInfo(pick_color), 'pick_correlate_layer': gi.FunctionInfo(pick_correlate_layer), 'policy_color_profile': gi.FunctionInfo(policy_color_profile), 'policy_rotate': gi.FunctionInfo(policy_rotate), 'raise_item': gi.FunctionInfo(raise_item), 'raise_item_to_top': gi.FunctionInfo(raise_item_to_top), 'remove_channel': gi.FunctionInfo(remove_channel), 'remove_layer': gi.FunctionInfo(remove_layer), 'remove_path': gi.FunctionInfo(remove_path), 'reorder_item': gi.FunctionInfo(reorder_item), 'resize': gi.FunctionInfo(resize), 'resize_to_layers': gi.FunctionInfo(resize_to_layers), 'rotate': gi.FunctionInfo(rotate), 'scale': gi.FunctionInfo(scale), 'select_color': gi.FunctionInfo(select_color), 'select_contiguous_color': gi.FunctionInfo(select_contiguous_color), 'select_ellipse': gi.FunctionInfo(select_ellipse), 'select_item': gi.FunctionInfo(select_item), 'select_polygon': gi.FunctionInfo(select_polygon), 'select_rectangle': gi.FunctionInfo(select_rectangle), 'select_round_rectangle': gi.FunctionInfo(select_round_rectangle), 'set_color_profile': gi.FunctionInfo(set_color_profile), 'set_color_profile_from_file': gi.FunctionInfo(set_color_profile_from_file), 'set_component_active': gi.FunctionInfo(set_component_active), 'set_component_visible': gi.FunctionInfo(set_component_visible), 'set_file': gi.FunctionInfo(set_file), 'set_metadata': gi.FunctionInfo(set_metadata), 'set_palette': gi.FunctionInfo(set_palette), 'set_resolution': gi.FunctionInfo(set_resolution), 'set_selected_channels': gi.FunctionInfo(set_selected_channels), 'set_selected_layers': gi.FunctionInfo(set_selected_layers), 'set_selected_paths': gi.FunctionInfo(set_selected_paths), 'set_simulation_bpc': gi.FunctionInfo(set_simulation_bpc), 'set_simulation_intent': gi.FunctionInfo(set_simulation_intent), 'set_simulation_profile': gi.FunctionInfo(set_simulation_profile), 'set_simulation_profile_from_file': gi.FunctionInfo(set_simulation_profile_from_file), 'set_tattoo_state': gi.FunctionInfo(set_tattoo_state), 'set_unit': gi.FunctionInfo(set_unit), 'take_selected_channels': gi.FunctionInfo(take_selected_channels), 'take_selected_layers': gi.FunctionInfo(take_selected_layers), 'take_selected_paths': gi.FunctionInfo(take_selected_paths), 'thaw_channels': gi.FunctionInfo(thaw_channels), 'thaw_layers': gi.FunctionInfo(thaw_layers), 'thaw_paths': gi.FunctionInfo(thaw_paths), 'undo_disable': gi.FunctionInfo(undo_disable), 'undo_enable': gi.FunctionInfo(undo_enable), 'undo_freeze': gi.FunctionInfo(undo_freeze), 'undo_group_end': gi.FunctionInfo(undo_group_end), 'undo_group_start': gi.FunctionInfo(undo_group_start), 'undo_is_enabled': gi.FunctionInfo(undo_is_enabled), 'undo_thaw': gi.FunctionInfo(undo_thaw), 'unset_active_channel': gi.FunctionInfo(unset_active_channel)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GimpImage\n\nProperties from GimpImage:\n  id -> gint: The image id\n    The image id for internal use\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpImage (2359059520)>'
    __info__ = ObjectInfo(Image)
    __static_attributes__ = ()


