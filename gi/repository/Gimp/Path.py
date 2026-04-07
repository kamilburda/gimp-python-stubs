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


from .Item import Item

class Path(Item):
    """
    :Constructors:
    
    ::
    
        Path(**properties)
        new(image:Gimp.Image, name:str=None) -> Gimp.Path
        new_from_text_layer(image:Gimp.Image, layer:Gimp.Layer) -> Gimp.Path
    """
    def attach_parasite(self, parasite): # real signature unknown; restored from __doc__
        """ attach_parasite(self, parasite:Gimp.Parasite) -> bool """
        return False

    def bezier_stroke_conicto(self, stroke_id, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ bezier_stroke_conicto(self, stroke_id:int, x0:float, y0:float, x1:float, y1:float) -> bool """
        return False

    def bezier_stroke_cubicto(self, stroke_id, x0, y0, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ bezier_stroke_cubicto(self, stroke_id:int, x0:float, y0:float, x1:float, y1:float, x2:float, y2:float) -> bool """
        return False

    def bezier_stroke_lineto(self, stroke_id, x0, y0): # real signature unknown; restored from __doc__
        """ bezier_stroke_lineto(self, stroke_id:int, x0:float, y0:float) -> bool """
        return False

    def bezier_stroke_new_ellipse(self, x0, y0, radius_x, radius_y, angle): # real signature unknown; restored from __doc__
        """ bezier_stroke_new_ellipse(self, x0:float, y0:float, radius_x:float, radius_y:float, angle:float) -> int """
        return 0

    def bezier_stroke_new_moveto(self, x0, y0): # real signature unknown; restored from __doc__
        """ bezier_stroke_new_moveto(self, x0:float, y0:float) -> int """
        return 0

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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gimp.Path """
        pass

    def delete(self): # real signature unknown; restored from __doc__
        """ delete(self) -> bool """
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

    def free(self, path): # real signature unknown; restored from __doc__
        """ free(path:list) """
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

    def get_by_id(self, path_id): # real signature unknown; restored from __doc__
        """ get_by_id(path_id:int) -> Gimp.Path or None """
        pass

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> list """
        return []

    def get_color_tag(self): # real signature unknown; restored from __doc__
        """ get_color_tag(self) -> Gimp.ColorTag """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_expanded(self): # real signature unknown; restored from __doc__
        """ get_expanded(self) -> bool """
        return False

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> int """
        return 0

    def get_image(self): # real signature unknown; restored from __doc__
        """ get_image(self) -> Gimp.Image """
        pass

    def get_lock_content(self): # real signature unknown; restored from __doc__
        """ get_lock_content(self) -> bool """
        return False

    def get_lock_position(self): # real signature unknown; restored from __doc__
        """ get_lock_position(self) -> bool """
        return False

    def get_lock_visibility(self): # real signature unknown; restored from __doc__
        """ get_lock_visibility(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_parasite(self, name): # real signature unknown; restored from __doc__
        """ get_parasite(self, name:str) -> Gimp.Parasite """
        pass

    def get_parasite_list(self): # real signature unknown; restored from __doc__
        """ get_parasite_list(self) -> list """
        return []

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gimp.Item """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_strokes(self): # real signature unknown; restored from __doc__
        """ get_strokes(self) -> list """
        return []

    def get_tattoo(self): # real signature unknown; restored from __doc__
        """ get_tattoo(self) -> int """
        return 0

    def get_user_writable_dir(self, path): # real signature unknown; restored from __doc__
        """ get_user_writable_dir(path:list) -> str """
        return ""

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
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

    def id_is_channel(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_channel(item_id:int) -> bool """
        return False

    def id_is_drawable(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_drawable(item_id:int) -> bool """
        return False

    def id_is_group_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_group_layer(item_id:int) -> bool """
        return False

    def id_is_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_layer(item_id:int) -> bool """
        return False

    def id_is_layer_mask(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_layer_mask(item_id:int) -> bool """
        return False

    def id_is_link_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_link_layer(item_id:int) -> bool """
        return False

    def id_is_path(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_path(item_id:int) -> bool """
        return False

    def id_is_selection(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_selection(item_id:int) -> bool """
        return False

    def id_is_text_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_text_layer(item_id:int) -> bool """
        return False

    def id_is_valid(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_valid(item_id:int) -> bool """
        return False

    def id_is_vector_layer(self, item_id): # real signature unknown; restored from __doc__
        """ id_is_vector_layer(item_id:int) -> bool """
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

    def is_channel(self): # real signature unknown; restored from __doc__
        """ is_channel(self) -> bool """
        return False

    def is_drawable(self): # real signature unknown; restored from __doc__
        """ is_drawable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_group(self): # real signature unknown; restored from __doc__
        """ is_group(self) -> bool """
        return False

    def is_group_layer(self): # real signature unknown; restored from __doc__
        """ is_group_layer(self) -> bool """
        return False

    def is_layer(self): # real signature unknown; restored from __doc__
        """ is_layer(self) -> bool """
        return False

    def is_layer_mask(self): # real signature unknown; restored from __doc__
        """ is_layer_mask(self) -> bool """
        return False

    def is_link_layer(self): # real signature unknown; restored from __doc__
        """ is_link_layer(self) -> bool """
        return False

    def is_path(self): # real signature unknown; restored from __doc__
        """ is_path(self) -> bool """
        return False

    def is_selection(self): # real signature unknown; restored from __doc__
        """ is_selection(self) -> bool """
        return False

    def is_text_layer(self): # real signature unknown; restored from __doc__
        """ is_text_layer(self) -> bool """
        return False

    def is_valid(self): # real signature unknown; restored from __doc__
        """ is_valid(self) -> bool """
        return False

    def is_vector_layer(self): # real signature unknown; restored from __doc__
        """ is_vector_layer(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls, image, name=None): # real signature unknown; restored from __doc__
        """ new(image:Gimp.Image, name:str=None) -> Gimp.Path """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_from_text_layer(cls, image, layer): # real signature unknown; restored from __doc__
        """ new_from_text_layer(image:Gimp.Image, layer:Gimp.Layer) -> Gimp.Path """
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

    def parse(self, path, max_paths, check): # real signature unknown; restored from __doc__
        """ parse(path:str, max_paths:int, check:bool) -> list, check_failed:list """
        return []

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_stroke(self, stroke_id): # real signature unknown; restored from __doc__
        """ remove_stroke(self, stroke_id:int) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_color_tag(self, color_tag): # real signature unknown; restored from __doc__
        """ set_color_tag(self, color_tag:Gimp.ColorTag) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_expanded(self, expanded): # real signature unknown; restored from __doc__
        """ set_expanded(self, expanded:bool) -> bool """
        return False

    def set_lock_content(self, lock_content): # real signature unknown; restored from __doc__
        """ set_lock_content(self, lock_content:bool) -> bool """
        return False

    def set_lock_position(self, lock_position): # real signature unknown; restored from __doc__
        """ set_lock_position(self, lock_position:bool) -> bool """
        return False

    def set_lock_visibility(self, lock_visibility): # real signature unknown; restored from __doc__
        """ set_lock_visibility(self, lock_visibility:bool) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_tattoo(self, tattoo): # real signature unknown; restored from __doc__
        """ set_tattoo(self, tattoo:int) -> bool """
        return False

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) -> bool """
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

    def stroke_close(self, stroke_id): # real signature unknown; restored from __doc__
        """ stroke_close(self, stroke_id:int) -> bool """
        return False

    def stroke_flip(self, stroke_id, flip_type, axis): # real signature unknown; restored from __doc__
        """ stroke_flip(self, stroke_id:int, flip_type:Gimp.OrientationType, axis:float) -> bool """
        return False

    def stroke_flip_free(self, stroke_id, x1, y1, x2, y2): # real signature unknown; restored from __doc__
        """ stroke_flip_free(self, stroke_id:int, x1:float, y1:float, x2:float, y2:float) -> bool """
        return False

    def stroke_get_length(self, stroke_id, precision): # real signature unknown; restored from __doc__
        """ stroke_get_length(self, stroke_id:int, precision:float) -> float """
        return 0.0

    def stroke_get_points(self, stroke_id): # real signature unknown; restored from __doc__
        """ stroke_get_points(self, stroke_id:int) -> Gimp.PathStrokeType, controlpoints:list, closed:bool """
        pass

    def stroke_get_point_at_dist(self, stroke_id, dist, precision): # real signature unknown; restored from __doc__
        """ stroke_get_point_at_dist(self, stroke_id:int, dist:float, precision:float) -> bool, x_point:float, y_point:float, slope:float, valid:bool """
        return False

    def stroke_interpolate(self, stroke_id, precision): # real signature unknown; restored from __doc__
        """ stroke_interpolate(self, stroke_id:int, precision:float) -> list, closed:bool """
        return []

    def stroke_new_from_points(self, type, controlpoints, closed): # real signature unknown; restored from __doc__
        """ stroke_new_from_points(self, type:Gimp.PathStrokeType, controlpoints:list, closed:bool) -> int """
        return 0

    def stroke_reverse(self, stroke_id): # real signature unknown; restored from __doc__
        """ stroke_reverse(self, stroke_id:int) -> bool """
        return False

    def stroke_rotate(self, stroke_id, center_x, center_y, angle): # real signature unknown; restored from __doc__
        """ stroke_rotate(self, stroke_id:int, center_x:float, center_y:float, angle:float) -> bool """
        return False

    def stroke_scale(self, stroke_id, scale_x, scale_y): # real signature unknown; restored from __doc__
        """ stroke_scale(self, stroke_id:int, scale_x:float, scale_y:float) -> bool """
        return False

    def stroke_translate(self, stroke_id, off_x, off_y): # real signature unknown; restored from __doc__
        """ stroke_translate(self, stroke_id:int, off_x:float, off_y:float) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def to_str(self, path): # real signature unknown; restored from __doc__
        """ to_str(path:list) -> str """
        return ""

    def transform_2d(self, source_x, source_y, scale_x, scale_y, angle, dest_x, dest_y): # real signature unknown; restored from __doc__
        """ transform_2d(self, source_x:float, source_y:float, scale_x:float, scale_y:float, angle:float, dest_x:float, dest_y:float) -> Gimp.Item """
        pass

    def transform_flip(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ transform_flip(self, x0:float, y0:float, x1:float, y1:float) -> Gimp.Item """
        pass

    def transform_flip_simple(self, flip_type, auto_center, axis): # real signature unknown; restored from __doc__
        """ transform_flip_simple(self, flip_type:Gimp.OrientationType, auto_center:bool, axis:float) -> Gimp.Item """
        pass

    def transform_matrix(self, coeff_0_0, coeff_0_1, coeff_0_2, coeff_1_0, coeff_1_1, coeff_1_2, coeff_2_0, coeff_2_1, coeff_2_2): # real signature unknown; restored from __doc__
        """ transform_matrix(self, coeff_0_0:float, coeff_0_1:float, coeff_0_2:float, coeff_1_0:float, coeff_1_1:float, coeff_1_2:float, coeff_2_0:float, coeff_2_1:float, coeff_2_2:float) -> Gimp.Item """
        pass

    def transform_perspective(self, x0, y0, x1, y1, x2, y2, x3, y3): # real signature unknown; restored from __doc__
        """ transform_perspective(self, x0:float, y0:float, x1:float, y1:float, x2:float, y2:float, x3:float, y3:float) -> Gimp.Item """
        pass

    def transform_rotate(self, angle, auto_center, center_x, center_y): # real signature unknown; restored from __doc__
        """ transform_rotate(self, angle:float, auto_center:bool, center_x:float, center_y:float) -> Gimp.Item """
        pass

    def transform_rotate_simple(self, rotate_type, auto_center, center_x, center_y): # real signature unknown; restored from __doc__
        """ transform_rotate_simple(self, rotate_type:Gimp.RotationType, auto_center:bool, center_x:float, center_y:float) -> Gimp.Item """
        pass

    def transform_scale(self, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ transform_scale(self, x0:float, y0:float, x1:float, y1:float) -> Gimp.Item """
        pass

    def transform_shear(self, shear_type, magnitude): # real signature unknown; restored from __doc__
        """ transform_shear(self, shear_type:Gimp.OrientationType, magnitude:float) -> Gimp.Item """
        pass

    def transform_translate(self, off_x, off_y): # real signature unknown; restored from __doc__
        """ transform_translate(self, off_x:float, off_y:float) -> Gimp.Item """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001268f3b31f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Path), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpPath (2360862224)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_text_layer': <classmethod(gi.FunctionInfo(new_from_text_layer))>, 'free': <staticmethod(gi.FunctionInfo(free))>, 'get_by_id': <staticmethod(gi.FunctionInfo(get_by_id))>, 'get_user_writable_dir': <staticmethod(gi.FunctionInfo(get_user_writable_dir))>, 'parse': <staticmethod(gi.FunctionInfo(parse))>, 'to_str': <staticmethod(gi.FunctionInfo(to_str))>, 'bezier_stroke_conicto': gi.FunctionInfo(bezier_stroke_conicto), 'bezier_stroke_cubicto': gi.FunctionInfo(bezier_stroke_cubicto), 'bezier_stroke_lineto': gi.FunctionInfo(bezier_stroke_lineto), 'bezier_stroke_new_ellipse': gi.FunctionInfo(bezier_stroke_new_ellipse), 'bezier_stroke_new_moveto': gi.FunctionInfo(bezier_stroke_new_moveto), 'copy': gi.FunctionInfo(copy), 'get_strokes': gi.FunctionInfo(get_strokes), 'remove_stroke': gi.FunctionInfo(remove_stroke), 'stroke_close': gi.FunctionInfo(stroke_close), 'stroke_flip': gi.FunctionInfo(stroke_flip), 'stroke_flip_free': gi.FunctionInfo(stroke_flip_free), 'stroke_get_length': gi.FunctionInfo(stroke_get_length), 'stroke_get_point_at_dist': gi.FunctionInfo(stroke_get_point_at_dist), 'stroke_get_points': gi.FunctionInfo(stroke_get_points), 'stroke_interpolate': gi.FunctionInfo(stroke_interpolate), 'stroke_new_from_points': gi.FunctionInfo(stroke_new_from_points), 'stroke_reverse': gi.FunctionInfo(stroke_reverse), 'stroke_rotate': gi.FunctionInfo(stroke_rotate), 'stroke_scale': gi.FunctionInfo(stroke_scale), 'stroke_translate': gi.FunctionInfo(stroke_translate)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GimpPath\n\nProperties from GimpItem:\n  id -> gint: The item id\n    The item id for internal use\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpPath (2360862224)>'
    __info__ = ObjectInfo(Path)
    __static_attributes__ = ()


