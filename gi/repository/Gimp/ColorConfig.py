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


from .ConfigInterface import ConfigInterface

class ColorConfig(__gi_overrides_GObject.Object, ConfigInterface):
    """
    :Constructors:
    
    ::
    
        ColorConfig(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def build_data_path(self, name): # real signature unknown; restored from __doc__
        """ build_data_path(name:str) -> str """
        return ""

    def build_plug_in_path(self, name): # real signature unknown; restored from __doc__
        """ build_plug_in_path(name:str) -> str """
        return ""

    def build_system_path(self, name): # real signature unknown; restored from __doc__
        """ build_system_path(name:str) -> str """
        return ""

    def build_writable_path(self, name): # real signature unknown; restored from __doc__
        """ build_writable_path(name:str) -> str """
        return ""

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

    def deserialize_return(self, scanner, expected_token, nest_level): # real signature unknown; restored from __doc__
        """ deserialize_return(scanner:GLib.Scanner, expected_token:GLib.TokenType, nest_level:int) -> bool """
        return False

    def diff(self, a, b, flags): # real signature unknown; restored from __doc__
        """ diff(a:GObject.Object, b:GObject.Object, flags:GObject.ParamFlags) -> list """
        return []

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

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

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

    def get_cmyk_color_profile(self): # real signature unknown; restored from __doc__
        """ get_cmyk_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display_bpc(self): # real signature unknown; restored from __doc__
        """ get_display_bpc(self) -> bool """
        return False

    def get_display_color_profile(self): # real signature unknown; restored from __doc__
        """ get_display_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_display_intent(self): # real signature unknown; restored from __doc__
        """ get_display_intent(self) -> Gimp.ColorRenderingIntent """
        pass

    def get_display_optimize(self): # real signature unknown; restored from __doc__
        """ get_display_optimize(self) -> bool """
        return False

    def get_display_profile_from_gdk(self): # real signature unknown; restored from __doc__
        """ get_display_profile_from_gdk(self) -> bool """
        return False

    def get_gray_color_profile(self): # real signature unknown; restored from __doc__
        """ get_gray_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> Gimp.ColorManagementMode """
        pass

    def get_out_of_gamut_color(self): # real signature unknown; restored from __doc__
        """ get_out_of_gamut_color(self) -> Gegl.Color """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rgb_color_profile(self): # real signature unknown; restored from __doc__
        """ get_rgb_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_simulation_bpc(self): # real signature unknown; restored from __doc__
        """ get_simulation_bpc(self) -> bool """
        return False

    def get_simulation_color_profile(self): # real signature unknown; restored from __doc__
        """ get_simulation_color_profile(self) -> Gimp.ColorProfile """
        pass

    def get_simulation_gamut_check(self): # real signature unknown; restored from __doc__
        """ get_simulation_gamut_check(self) -> bool """
        return False

    def get_simulation_intent(self): # real signature unknown; restored from __doc__
        """ get_simulation_intent(self) -> Gimp.ColorRenderingIntent """
        pass

    def get_simulation_optimize(self): # real signature unknown; restored from __doc__
        """ get_simulation_optimize(self) -> bool """
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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
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

    def param_spec_duplicate(self, pspec): # real signature unknown; restored from __doc__
        """ param_spec_duplicate(pspec:GObject.ParamSpec) -> GObject.ParamSpec """
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

    def reset_properties(self, p_object): # real signature unknown; restored from __doc__
        """ reset_properties(object:GObject.Object) """
        pass

    def reset_property(self, p_object, property_name): # real signature unknown; restored from __doc__
        """ reset_property(object:GObject.Object, property_name:str) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def serialize_value(self, value, p_str, escaped): # real signature unknown; restored from __doc__
        """ serialize_value(value:GObject.Value, str:GLib.String, escaped:bool) -> bool """
        return False

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

    def string_append_escaped(self, string, val): # real signature unknown; restored from __doc__
        """ string_append_escaped(string:GLib.String, val:str) """
        pass

    def sync(self, src, dest, flags): # real signature unknown; restored from __doc__
        """ sync(src:GObject.Object, dest:GObject.Object, flags:GObject.ParamFlags) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def type_register(self, parent_type, type_name, pspecs): # real signature unknown; restored from __doc__
        """ type_register(parent_type:GType, type_name:str, pspecs:list) -> GType """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001268f2f3e20>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ColorConfig), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpColorConfig (2362310736)>, '__doc__': None, '__gsignals__': {}, 'get_cmyk_color_profile': gi.FunctionInfo(get_cmyk_color_profile), 'get_display_bpc': gi.FunctionInfo(get_display_bpc), 'get_display_color_profile': gi.FunctionInfo(get_display_color_profile), 'get_display_intent': gi.FunctionInfo(get_display_intent), 'get_display_optimize': gi.FunctionInfo(get_display_optimize), 'get_display_profile_from_gdk': gi.FunctionInfo(get_display_profile_from_gdk), 'get_gray_color_profile': gi.FunctionInfo(get_gray_color_profile), 'get_mode': gi.FunctionInfo(get_mode), 'get_out_of_gamut_color': gi.FunctionInfo(get_out_of_gamut_color), 'get_rgb_color_profile': gi.FunctionInfo(get_rgb_color_profile), 'get_simulation_bpc': gi.FunctionInfo(get_simulation_bpc), 'get_simulation_color_profile': gi.FunctionInfo(get_simulation_color_profile), 'get_simulation_gamut_check': gi.FunctionInfo(get_simulation_gamut_check), 'get_simulation_intent': gi.FunctionInfo(get_simulation_intent), 'get_simulation_optimize': gi.FunctionInfo(get_simulation_optimize)})"
    __firstlineno__ = 651
    __gdoc__ = "Object GimpColorConfig\n\nProperties from GimpColorConfig:\n  mode -> GimpColorManagementMode: Mode of operation\n    How images are displayed on screen.\n  rgb-profile -> GimpConfigPath: Preferred RGB profile\n    The preferred RGB working space color profile. It will be offered next to the built-in RGB profile when a color profile can be chosen.\n  gray-profile -> GimpConfigPath: Preferred grayscale profile\n    The preferred grayscale working space color profile. It will be offered next to the built-in grayscale profile when a color profile can be chosen.\n  cmyk-profile -> GimpConfigPath: CMYK profile\n    The CMYK color profile used to convert between RGB and CMYK.\n  display-profile -> GimpConfigPath: Monitor profile\n    The color profile of your (primary) monitor.\n  display-profile-from-gdk -> gboolean: Use the system monitor profile\n    When enabled, GIMP will try to use the display color profile from the windowing system.  The configured monitor profile is then only used as a fallback.\n  simulation-profile -> GimpConfigPath: Simulation profile for soft-proofing\n    The color profile to use for soft-proofing from your image's color space to some other color space, including soft-proofing to a printer or other output device profile.\n  display-rendering-intent -> GimpColorRenderingIntent: Display rendering intent\n    How colors are converted from your image's color space to your display device. Relative colorimetric is usually the best choice. Unless you use a LUT monitor profile (most monitor profiles are matrix), choosing perceptual intent really gives you relative colorimetric.\n  display-use-black-point-compensation -> gboolean: Use black point compensation for the display\n    Do use black point compensation (unless you know you have a reason not to).\n  display-optimize -> gboolean: Optimize display color transformations\n    When disabled, image display might be of better quality at the cost of speed.\n  simulation-rendering-intent -> GimpColorRenderingIntent: Soft-proofing rendering intent\n    How colors are converted from your image's color space to the output simulation device (usually your monitor). Try them all and choose what looks the best.\n  simulation-use-black-point-compensation -> gboolean: Use black point compensation for soft-proofing\n    Try with and without black point compensation and choose what looks best.\n  simulation-optimize -> gboolean: Optimize soft-proofing color transformations\n    When disabled, soft-proofing might be of better quality at the cost of speed.\n  simulation-gamut-check -> gboolean: Mark out of gamut colors\n    When enabled, the soft-proofing will mark colors which can not be represented in the target color space.\n  out-of-gamut-color -> GeglColor: Out of gamut warning color\n    The color to use for marking colors which are out of gamut.\n  show-rgb-u8 -> gboolean: Show RGB 0..255\n    Show RGB 0..255 scales\n  show-hsv -> gboolean: Show HSV\n    Show HSV instead of LCH\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpColorConfig (2362310736)>'
    __info__ = ObjectInfo(ColorConfig)
    __static_attributes__ = ()


