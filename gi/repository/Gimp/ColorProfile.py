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


class ColorProfile(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        ColorProfile(**properties)
        new_d50_gray_lab_trc() -> Gimp.ColorProfile
        new_d65_gray_linear() -> Gimp.ColorProfile
        new_d65_gray_srgb_trc() -> Gimp.ColorProfile
        new_from_file(file:Gio.File) -> Gimp.ColorProfile or None
        new_from_icc_profile(data:list) -> Gimp.ColorProfile or None
        new_from_lcms_profile(lcms_profile=None) -> Gimp.ColorProfile or None
        new_rgb_adobe() -> Gimp.ColorProfile
        new_rgb_srgb() -> Gimp.ColorProfile
        new_rgb_srgb_linear() -> Gimp.ColorProfile
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

    def get_copyright(self): # real signature unknown; restored from __doc__
        """ get_copyright(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_format(self, format, intent): # real signature unknown; restored from __doc__
        """ get_format(self, format:Babl.Object, intent:Gimp.ColorRenderingIntent) -> Babl.Object """
        pass

    def get_icc_profile(self): # real signature unknown; restored from __doc__
        """ get_icc_profile(self) -> list """
        return []

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_lcms_format(self, format): # real signature unknown; restored from __doc__
        """ get_lcms_format(format:Babl.Object) -> Babl.Object or None, lcms_format:int """
        pass

    def get_lcms_profile(self): # real signature unknown; restored from __doc__
        """ get_lcms_profile(self) """
        pass

    def get_manufacturer(self): # real signature unknown; restored from __doc__
        """ get_manufacturer(self) -> str """
        return ""

    def get_model(self): # real signature unknown; restored from __doc__
        """ get_model(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_space(self, intent): # real signature unknown; restored from __doc__
        """ get_space(self, intent:Gimp.ColorRenderingIntent) -> Babl.Object """
        pass

    def get_summary(self): # real signature unknown; restored from __doc__
        """ get_summary(self) -> str """
        return ""

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

    def is_cmyk(self): # real signature unknown; restored from __doc__
        """ is_cmyk(self) -> bool """
        return False

    def is_equal(self, profile2): # real signature unknown; restored from __doc__
        """ is_equal(self, profile2:Gimp.ColorProfile) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_gray(self): # real signature unknown; restored from __doc__
        """ is_gray(self) -> bool """
        return False

    def is_linear(self): # real signature unknown; restored from __doc__
        """ is_linear(self) -> bool """
        return False

    def is_rgb(self): # real signature unknown; restored from __doc__
        """ is_rgb(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_d50_gray_lab_trc(cls): # real signature unknown; restored from __doc__
        """ new_d50_gray_lab_trc() -> Gimp.ColorProfile """
        pass

    @classmethod
    def new_d65_gray_linear(cls): # real signature unknown; restored from __doc__
        """ new_d65_gray_linear() -> Gimp.ColorProfile """
        pass

    @classmethod
    def new_d65_gray_srgb_trc(cls): # real signature unknown; restored from __doc__
        """ new_d65_gray_srgb_trc() -> Gimp.ColorProfile """
        pass

    @classmethod
    def new_from_file(cls, file): # real signature unknown; restored from __doc__
        """ new_from_file(file:Gio.File) -> Gimp.ColorProfile or None """
        pass

    @classmethod
    def new_from_icc_profile(cls, data): # real signature unknown; restored from __doc__
        """ new_from_icc_profile(data:list) -> Gimp.ColorProfile or None """
        pass

    @classmethod
    def new_from_lcms_profile(cls, lcms_profile=None): # real signature unknown; restored from __doc__
        """ new_from_lcms_profile(lcms_profile=None) -> Gimp.ColorProfile or None """
        pass

    def new_linear_from_color_profile(self): # real signature unknown; restored from __doc__
        """ new_linear_from_color_profile(self) -> Gimp.ColorProfile or None """
        pass

    @classmethod
    def new_rgb_adobe(cls): # real signature unknown; restored from __doc__
        """ new_rgb_adobe() -> Gimp.ColorProfile """
        pass

    @classmethod
    def new_rgb_srgb(cls): # real signature unknown; restored from __doc__
        """ new_rgb_srgb() -> Gimp.ColorProfile """
        pass

    @classmethod
    def new_rgb_srgb_linear(cls): # real signature unknown; restored from __doc__
        """ new_rgb_srgb_linear() -> Gimp.ColorProfile """
        pass

    def new_srgb_trc_from_color_profile(self): # real signature unknown; restored from __doc__
        """ new_srgb_trc_from_color_profile(self) -> Gimp.ColorProfile or None """
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

    def save_to_file(self, file): # real signature unknown; restored from __doc__
        """ save_to_file(self, file:Gio.File) -> bool """
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

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001268f2f1480>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ColorProfile), '__module__': 'gi.repository.Gimp', '__gtype__': <GType GimpColorProfile (2362466496)>, '__doc__': None, '__gsignals__': {}, 'new_d50_gray_lab_trc': <classmethod(gi.FunctionInfo(new_d50_gray_lab_trc))>, 'new_d65_gray_linear': <classmethod(gi.FunctionInfo(new_d65_gray_linear))>, 'new_d65_gray_srgb_trc': <classmethod(gi.FunctionInfo(new_d65_gray_srgb_trc))>, 'new_from_file': <classmethod(gi.FunctionInfo(new_from_file))>, 'new_from_icc_profile': <classmethod(gi.FunctionInfo(new_from_icc_profile))>, 'new_from_lcms_profile': <classmethod(gi.FunctionInfo(new_from_lcms_profile))>, 'new_rgb_adobe': <classmethod(gi.FunctionInfo(new_rgb_adobe))>, 'new_rgb_srgb': <classmethod(gi.FunctionInfo(new_rgb_srgb))>, 'new_rgb_srgb_linear': <classmethod(gi.FunctionInfo(new_rgb_srgb_linear))>, 'get_lcms_format': <staticmethod(gi.FunctionInfo(get_lcms_format))>, 'get_copyright': gi.FunctionInfo(get_copyright), 'get_description': gi.FunctionInfo(get_description), 'get_format': gi.FunctionInfo(get_format), 'get_icc_profile': gi.FunctionInfo(get_icc_profile), 'get_label': gi.FunctionInfo(get_label), 'get_lcms_profile': gi.FunctionInfo(get_lcms_profile), 'get_manufacturer': gi.FunctionInfo(get_manufacturer), 'get_model': gi.FunctionInfo(get_model), 'get_space': gi.FunctionInfo(get_space), 'get_summary': gi.FunctionInfo(get_summary), 'is_cmyk': gi.FunctionInfo(is_cmyk), 'is_equal': gi.FunctionInfo(is_equal), 'is_gray': gi.FunctionInfo(is_gray), 'is_linear': gi.FunctionInfo(is_linear), 'is_rgb': gi.FunctionInfo(is_rgb), 'new_linear_from_color_profile': gi.FunctionInfo(new_linear_from_color_profile), 'new_srgb_trc_from_color_profile': gi.FunctionInfo(new_srgb_trc_from_color_profile), 'save_to_file': gi.FunctionInfo(save_to_file)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GimpColorProfile\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GimpColorProfile (2362466496)>'
    __info__ = ObjectInfo(ColorProfile)
    __static_attributes__ = ()


