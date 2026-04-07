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


class Metadata(__gi_overrides_GExiv2.Metadata):
    """
    :Constructors:
    
    ::
    
        Metadata(**properties)
        new() -> Gimp.Metadata
    """
    def add_xmp_history(self, state_status): # real signature unknown; restored from __doc__
        """ add_xmp_history(self, state_status:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_comment(self): # real signature unknown; restored from __doc__
        """ clear_comment(self) """
        pass

    def clear_exif(self): # real signature unknown; restored from __doc__
        """ clear_exif(self) """
        pass

    def clear_iptc(self): # real signature unknown; restored from __doc__
        """ clear_iptc(self) """
        pass

    def clear_tag(self, tag): # real signature unknown; restored from __doc__
        """ clear_tag(self, tag:str) -> bool """
        return False

    def clear_xmp(self): # real signature unknown; restored from __doc__
        """ clear_xmp(self) """
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

    def delete_gps_info(self): # real signature unknown; restored from __doc__
        """ delete_gps_info(self) """
        pass

    def deserialize(self, metadata_xml): # real signature unknown; restored from __doc__
        """ deserialize(metadata_xml:str) -> Gimp.Metadata """
        pass

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
        """ duplicate(self) -> Gimp.Metadata """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def erase_exif_thumbnail(self): # real signature unknown; restored from __doc__
        """ erase_exif_thumbnail(self) """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
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

    def from_app1_segment(self, data): # real signature unknown; restored from __doc__
        """ from_app1_segment(self, data:list) -> bool """
        return False

    def from_stream(self, stream): # real signature unknown; restored from __doc__
        """ from_stream(self, stream:Gio.InputStream) -> bool """
        return False

    def generate_xmp_packet(self, xmp_format_flags, padding): # real signature unknown; restored from __doc__
        """ generate_xmp_packet(self, xmp_format_flags:GExiv2.XmpFormatFlags, padding:int) -> str or None """
        return ""

    def get(self, key, default=None): # reliably restored by inspect
        # no doc
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_colorspace(self): # real signature unknown; restored from __doc__
        """ get_colorspace(self) -> Gimp.MetadataColorspace """
        pass

    def get_comment(self): # real signature unknown; restored from __doc__
        """ get_comment(self) -> str or None """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date_time(self): # reliably restored by inspect
        # no doc
        pass

    def get_exif_data(self, byte_order): # real signature unknown; restored from __doc__
        """ get_exif_data(self, byte_order:GExiv2.ByteOrder) -> GLib.Bytes or None """
        pass

    def get_exif_tags(self): # real signature unknown; restored from __doc__
        """ get_exif_tags(self) -> list """
        return []

    def get_exif_tag_rational(self, key): # reliably restored by inspect
        # no doc
        pass

    def get_exif_thumbnail(self): # real signature unknown; restored from __doc__
        """ get_exif_thumbnail(self) -> buffer:list """
        pass

    def get_exposure_time(self): # reliably restored by inspect
        # no doc
        pass

    def get_fnumber(self): # real signature unknown; restored from __doc__
        """ get_fnumber(self) -> float """
        return 0.0

    def get_focal_length(self): # real signature unknown; restored from __doc__
        """ get_focal_length(self) -> float """
        return 0.0

    def get_gps_altitude(self): # real signature unknown; restored from __doc__
        """ get_gps_altitude(self) -> altitude:float """
        pass

    def get_gps_info(self): # real signature unknown; restored from __doc__
        """ get_gps_info(self) -> longitude:float, latitude:float, altitude:float """
        pass

    def get_gps_latitude(self): # real signature unknown; restored from __doc__
        """ get_gps_latitude(self) -> latitude:float """
        pass

    def get_gps_longitude(self): # real signature unknown; restored from __doc__
        """ get_gps_longitude(self) -> longitude:float """
        pass

    def get_guid(self): # real signature unknown; restored from __doc__
        """ get_guid() -> str """
        return ""

    def get_iptc_tags(self): # real signature unknown; restored from __doc__
        """ get_iptc_tags(self) -> list """
        return []

    def get_iso_speed(self): # real signature unknown; restored from __doc__
        """ get_iso_speed(self) -> int """
        return 0

    def get_metadata_pixel_height(self): # real signature unknown; restored from __doc__
        """ get_metadata_pixel_height(self) -> int """
        return 0

    def get_metadata_pixel_width(self): # real signature unknown; restored from __doc__
        """ get_metadata_pixel_width(self) -> int """
        return 0

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> GExiv2.Orientation """
        pass

    def get_pixel_height(self): # real signature unknown; restored from __doc__
        """ get_pixel_height(self) -> int """
        return 0

    def get_pixel_width(self): # real signature unknown; restored from __doc__
        """ get_pixel_width(self) -> int """
        return 0

    def get_preview_image(self, props): # real signature unknown; restored from __doc__
        """ get_preview_image(self, props:GExiv2.PreviewProperties) -> GExiv2.PreviewImage """
        pass

    def get_preview_properties(self): # real signature unknown; restored from __doc__
        """ get_preview_properties(self) -> list or None """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_raw(self, key): # reliably restored by inspect
        # no doc
        pass

    def get_resolution(self): # real signature unknown; restored from __doc__
        """ get_resolution(self) -> bool, xres:float, yres:float, unit:Gimp.Unit """
        return False

    def get_supports_exif(self): # real signature unknown; restored from __doc__
        """ get_supports_exif(self) -> bool """
        return False

    def get_supports_iptc(self): # real signature unknown; restored from __doc__
        """ get_supports_iptc(self) -> bool """
        return False

    def get_supports_xmp(self): # real signature unknown; restored from __doc__
        """ get_supports_xmp(self) -> bool """
        return False

    def get_tags(self): # reliably restored by inspect
        # no doc
        pass

    def get_tag_description(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_description(tag:str) -> str or None """
        return ""

    def get_tag_interpreted_string(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_interpreted_string(self, tag:str) -> str or None """
        return ""

    def get_tag_label(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_label(tag:str) -> str or None """
        return ""

    def get_tag_long(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_long(self, tag:str) -> int """
        return 0

    def get_tag_multiple(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_multiple(self, tag:str) -> list or None """
        return []

    def get_tag_raw(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_raw(self, tag:str) -> GLib.Bytes or None """
        pass

    def get_tag_string(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_string(self, tag:str) -> str or None """
        return ""

    def get_tag_type(self, tag): # real signature unknown; restored from __doc__
        """ get_tag_type(tag:str) -> str or None """
        return ""

    def get_xmp_namespace_for_tag(self, tag): # real signature unknown; restored from __doc__
        """ get_xmp_namespace_for_tag(tag:str) -> str """
        return ""

    def get_xmp_packet(self): # real signature unknown; restored from __doc__
        """ get_xmp_packet(self) -> str or None """
        return ""

    def get_xmp_tags(self): # real signature unknown; restored from __doc__
        """ get_xmp_tags(self) -> list """
        return []

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

    def has_exif(self): # real signature unknown; restored from __doc__
        """ has_exif(self) -> bool """
        return False

    def has_iptc(self): # real signature unknown; restored from __doc__
        """ has_iptc(self) -> bool """
        return False

    def has_tag(self, tag): # real signature unknown; restored from __doc__
        """ has_tag(self, tag:str) -> bool """
        return False

    def has_xmp(self): # real signature unknown; restored from __doc__
        """ has_xmp(self) -> bool """
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

    def is_exif_tag(self, tag): # real signature unknown; restored from __doc__
        """ is_exif_tag(tag:str) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_iptc_tag(self, tag): # real signature unknown; restored from __doc__
        """ is_iptc_tag(tag:str) -> bool """
        return False

    def is_tag_supported(self, tag, mime_type): # real signature unknown; restored from __doc__
        """ is_tag_supported(tag:str, mime_type:str) -> bool """
        return False

    def is_xmp_tag(self, tag): # real signature unknown; restored from __doc__
        """ is_xmp_tag(tag:str) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load_from_file(self, file): # real signature unknown; restored from __doc__
        """ load_from_file(file:Gio.File) -> Gimp.Metadata """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gimp.Metadata """
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

    def open_buf(self, data): # real signature unknown; restored from __doc__
        """ open_buf(self, data:list) -> bool """
        return False

    def open_path(self, path): # reliably restored by inspect
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

    def register_xmp_namespace(self, name, prefix): # real signature unknown; restored from __doc__
        """ register_xmp_namespace(name:str, prefix:str) """
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

    def save_external(self, path): # real signature unknown; restored from __doc__
        """ save_external(self, path:str) -> bool """
        return False

    def save_file(self, path=None): # reliably restored by inspect
        # no doc
        pass

    def save_to_file(self, file): # real signature unknown; restored from __doc__
        """ save_to_file(self, file:Gio.File) -> bool """
        return False

    def serialize(self): # real signature unknown; restored from __doc__
        """ serialize(self) -> str """
        return ""

    def set_bits_per_sample(self, bits_per_sample): # real signature unknown; restored from __doc__
        """ set_bits_per_sample(self, bits_per_sample:int) """
        pass

    def set_colorspace(self, colorspace): # real signature unknown; restored from __doc__
        """ set_colorspace(self, colorspace:Gimp.MetadataColorspace) """
        pass

    def set_comment(self, comment): # real signature unknown; restored from __doc__
        """ set_comment(self, comment:str) """
        pass

    def set_creation_date(self, datetime): # real signature unknown; restored from __doc__
        """ set_creation_date(self, datetime:GLib.DateTime) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date_time(self, value): # reliably restored by inspect
        # no doc
        pass

    def set_exif_tag_rational(self, key, fraction): # reliably restored by inspect
        # no doc
        pass

    def set_exif_thumbnail_from_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ set_exif_thumbnail_from_buffer(self, buffer:list) """
        pass

    def set_exif_thumbnail_from_file(self, path): # real signature unknown; restored from __doc__
        """ set_exif_thumbnail_from_file(self, path:str) -> bool """
        return False

    def set_from_exif(self, exif_data): # real signature unknown; restored from __doc__
        """ set_from_exif(self, exif_data:list) -> bool """
        return False

    def set_from_iptc(self, iptc_data): # real signature unknown; restored from __doc__
        """ set_from_iptc(self, iptc_data:list) -> bool """
        return False

    def set_from_xmp(self, xmp_data): # real signature unknown; restored from __doc__
        """ set_from_xmp(self, xmp_data:list) -> bool """
        return False

    def set_gps_info(self, longitude, latitude, altitude): # real signature unknown; restored from __doc__
        """ set_gps_info(self, longitude:float, latitude:float, altitude:float) """
        pass

    def set_metadata_pixel_height(self, height): # real signature unknown; restored from __doc__
        """ set_metadata_pixel_height(self, height:int) """
        pass

    def set_metadata_pixel_width(self, width): # real signature unknown; restored from __doc__
        """ set_metadata_pixel_width(self, width:int) """
        pass

    def set_orientation(self, orientation): # real signature unknown; restored from __doc__
        """ set_orientation(self, orientation:GExiv2.Orientation) """
        pass

    def set_pixel_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_pixel_size(self, width:int, height:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, xres, yres, unit): # real signature unknown; restored from __doc__
        """ set_resolution(self, xres:float, yres:float, unit:Gimp.Unit) """
        pass

    def set_tag_long(self, tag, value): # real signature unknown; restored from __doc__
        """ set_tag_long(self, tag:str, value:int) -> bool """
        return False

    def set_tag_multiple(self, tag, values): # real signature unknown; restored from __doc__
        """ set_tag_multiple(self, tag:str, values:list) -> bool """
        return False

    def set_tag_string(self, tag, value): # real signature unknown; restored from __doc__
        """ set_tag_string(self, tag:str, value:str) -> bool """
        return False

    def set_xmp_tag_struct(self, tag, type): # real signature unknown; restored from __doc__
        """ set_xmp_tag_struct(self, tag:str, type:GExiv2.StructureType) -> bool """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def try_clear_tag(self, tag): # real signature unknown; restored from __doc__
        """ try_clear_tag(self, tag:str) -> bool """
        return False

    def try_delete_gps_info(self): # real signature unknown; restored from __doc__
        """ try_delete_gps_info(self) """
        pass

    def try_erase_exif_thumbnail(self): # real signature unknown; restored from __doc__
        """ try_erase_exif_thumbnail(self) """
        pass

    def try_generate_xmp_packet(self, xmp_format_flags, padding): # real signature unknown; restored from __doc__
        """ try_generate_xmp_packet(self, xmp_format_flags:GExiv2.XmpFormatFlags, padding:int) -> str or None """
        return ""

    def try_get_comment(self): # real signature unknown; restored from __doc__
        """ try_get_comment(self) -> str or None """
        return ""

    def try_get_exif_tag_rational(self, tag): # real signature unknown; restored from __doc__
        """ try_get_exif_tag_rational(self, tag:str) -> nom:int, den:int """
        pass

    def try_get_exposure_time(self): # real signature unknown; restored from __doc__
        """ try_get_exposure_time(self) -> nom:int, den:int """
        pass

    def try_get_fnumber(self): # real signature unknown; restored from __doc__
        """ try_get_fnumber(self) -> float """
        return 0.0

    def try_get_focal_length(self): # real signature unknown; restored from __doc__
        """ try_get_focal_length(self) -> float """
        return 0.0

    def try_get_gps_altitude(self): # real signature unknown; restored from __doc__
        """ try_get_gps_altitude(self) -> altitude:float """
        pass

    def try_get_gps_info(self): # real signature unknown; restored from __doc__
        """ try_get_gps_info(self) -> longitude:float, latitude:float, altitude:float """
        pass

    def try_get_gps_latitude(self): # real signature unknown; restored from __doc__
        """ try_get_gps_latitude(self) -> latitude:float """
        pass

    def try_get_gps_longitude(self): # real signature unknown; restored from __doc__
        """ try_get_gps_longitude(self) -> longitude:float """
        pass

    def try_get_iso_speed(self): # real signature unknown; restored from __doc__
        """ try_get_iso_speed(self) -> int """
        return 0

    def try_get_metadata_pixel_height(self): # real signature unknown; restored from __doc__
        """ try_get_metadata_pixel_height(self) -> int """
        return 0

    def try_get_metadata_pixel_width(self): # real signature unknown; restored from __doc__
        """ try_get_metadata_pixel_width(self) -> int """
        return 0

    def try_get_orientation(self): # real signature unknown; restored from __doc__
        """ try_get_orientation(self) -> GExiv2.Orientation """
        pass

    def try_get_preview_image(self, props): # real signature unknown; restored from __doc__
        """ try_get_preview_image(self, props:GExiv2.PreviewProperties) -> GExiv2.PreviewImage """
        pass

    def try_get_tag_description(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_description(tag:str) -> str or None """
        return ""

    def try_get_tag_interpreted_string(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_interpreted_string(self, tag:str) -> str or None """
        return ""

    def try_get_tag_label(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_label(tag:str) -> str or None """
        return ""

    def try_get_tag_long(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_long(self, tag:str) -> int """
        return 0

    def try_get_tag_multiple(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_multiple(self, tag:str) -> list or None """
        return []

    def try_get_tag_raw(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_raw(self, tag:str) -> GLib.Bytes or None """
        pass

    def try_get_tag_string(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_string(self, tag:str) -> str or None """
        return ""

    def try_get_tag_type(self, tag): # real signature unknown; restored from __doc__
        """ try_get_tag_type(tag:str) -> str or None """
        return ""

    def try_get_xmp_namespace_for_tag(self, tag): # real signature unknown; restored from __doc__
        """ try_get_xmp_namespace_for_tag(tag:str) -> str """
        return ""

    def try_get_xmp_packet(self): # real signature unknown; restored from __doc__
        """ try_get_xmp_packet(self) -> str or None """
        return ""

    def try_has_tag(self, tag): # real signature unknown; restored from __doc__
        """ try_has_tag(self, tag:str) -> bool """
        return False

    def try_register_xmp_namespace(self, name, prefix): # real signature unknown; restored from __doc__
        """ try_register_xmp_namespace(name:str, prefix:str) """
        pass

    def try_set_comment(self, comment): # real signature unknown; restored from __doc__
        """ try_set_comment(self, comment:str) """
        pass

    def try_set_exif_tag_rational(self, tag, nom, den): # real signature unknown; restored from __doc__
        """ try_set_exif_tag_rational(self, tag:str, nom:int, den:int) """
        pass

    def try_set_exif_thumbnail_from_buffer(self, buffer): # real signature unknown; restored from __doc__
        """ try_set_exif_thumbnail_from_buffer(self, buffer:list) """
        pass

    def try_set_gps_info(self, longitude, latitude, altitude): # real signature unknown; restored from __doc__
        """ try_set_gps_info(self, longitude:float, latitude:float, altitude:float) """
        pass

    def try_set_metadata_pixel_height(self, height): # real signature unknown; restored from __doc__
        """ try_set_metadata_pixel_height(self, height:int) """
        pass

    def try_set_metadata_pixel_width(self, width): # real signature unknown; restored from __doc__
        """ try_set_metadata_pixel_width(self, width:int) """
        pass

    def try_set_orientation(self, orientation): # real signature unknown; restored from __doc__
        """ try_set_orientation(self, orientation:GExiv2.Orientation) """
        pass

    def try_set_tag_long(self, tag, value): # real signature unknown; restored from __doc__
        """ try_set_tag_long(self, tag:str, value:int) -> bool """
        return False

    def try_set_tag_multiple(self, tag, values): # real signature unknown; restored from __doc__
        """ try_set_tag_multiple(self, tag:str, values:list) -> bool """
        return False

    def try_set_tag_string(self, tag, value): # real signature unknown; restored from __doc__
        """ try_set_tag_string(self, tag:str, value:str) -> bool """
        return False

    def try_set_xmp_tag_struct(self, tag, type): # real signature unknown; restored from __doc__
        """ try_set_xmp_tag_struct(self, tag:str, type:GExiv2.StructureType) -> bool """
        return False

    def try_tag_supports_multiple_values(self, tag): # real signature unknown; restored from __doc__
        """ try_tag_supports_multiple_values(self, tag:str) -> bool """
        return False

    def try_unregister_all_xmp_namespaces(self): # real signature unknown; restored from __doc__
        """ try_unregister_all_xmp_namespaces() """
        pass

    def try_unregister_xmp_namespace(self, name): # real signature unknown; restored from __doc__
        """ try_unregister_xmp_namespace(name:str) """
        pass

    def try_update_gps_info(self, longitude, latitude, altitude): # real signature unknown; restored from __doc__
        """ try_update_gps_info(self, longitude:float, latitude:float, altitude:float) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unregister_all_xmp_namespaces(self): # real signature unknown; restored from __doc__
        """ unregister_all_xmp_namespaces() """
        pass

    def unregister_xmp_namespace(self, name): # real signature unknown; restored from __doc__
        """ unregister_xmp_namespace(name:str) """
        pass

    def update_gps_info(self, longitude, latitude, altitude): # real signature unknown; restored from __doc__
        """ update_gps_info(self, longitude:float, latitude:float, altitude:float) """
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

    def __contains__(self, key): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, key): # reliably restored by inspect
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

    def __init__(self, path=None): # reliably restored by inspect
        # no doc
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ set_tag_string(self, tag:str, value:str) -> bool """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001268f2eaec0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Metadata), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpMetadata (2360672384)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'deserialize': <staticmethod(gi.FunctionInfo(deserialize))>, 'get_guid': <staticmethod(gi.FunctionInfo(get_guid))>, 'is_tag_supported': <staticmethod(gi.FunctionInfo(is_tag_supported))>, 'load_from_file': <staticmethod(gi.FunctionInfo(load_from_file))>, 'add_xmp_history': gi.FunctionInfo(add_xmp_history), 'duplicate': gi.FunctionInfo(duplicate), 'get_colorspace': gi.FunctionInfo(get_colorspace), 'get_resolution': gi.FunctionInfo(get_resolution), 'save_to_file': gi.FunctionInfo(save_to_file), 'serialize': gi.FunctionInfo(serialize), 'set_bits_per_sample': gi.FunctionInfo(set_bits_per_sample), 'set_colorspace': gi.FunctionInfo(set_colorspace), 'set_creation_date': gi.FunctionInfo(set_creation_date), 'set_from_exif': gi.FunctionInfo(set_from_exif), 'set_from_iptc': gi.FunctionInfo(set_from_iptc), 'set_from_xmp': gi.FunctionInfo(set_from_xmp), 'set_pixel_size': gi.FunctionInfo(set_pixel_size), 'set_resolution': gi.FunctionInfo(set_resolution)})"
    __firstlineno__ = 20
    __gdoc__ = 'Object GimpMetadata\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpMetadata (2360672384)>'
    __info__ = ObjectInfo(Metadata)
    __static_attributes__ = (
        '_path',
    )


