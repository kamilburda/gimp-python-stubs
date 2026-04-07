# encoding: utf-8
# module gi.repository.Pango
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


from .Layout import Layout

class Layout(Layout):
    """
    :Constructors:
    
    ::
    
        Layout(**properties)
        new(context:Pango.Context) -> Pango.Layout
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

    def context_changed(self): # real signature unknown; restored from __doc__
        """ context_changed(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.Layout """
        pass

    def deserialize(self, context, bytes, flags): # real signature unknown; restored from __doc__
        """ deserialize(context:Pango.Context, bytes:GLib.Bytes, flags:Pango.LayoutDeserializeFlags) -> Pango.Layout or None """
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

    def get_alignment(self): # real signature unknown; restored from __doc__
        """ get_alignment(self) -> Pango.Alignment """
        pass

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> Pango.AttrList or None """
        pass

    def get_auto_dir(self): # real signature unknown; restored from __doc__
        """ get_auto_dir(self) -> bool """
        return False

    def get_baseline(self): # real signature unknown; restored from __doc__
        """ get_baseline(self) -> int """
        return 0

    def get_caret_pos(self, index_): # real signature unknown; restored from __doc__
        """ get_caret_pos(self, index_:int) -> strong_pos:Pango.Rectangle, weak_pos:Pango.Rectangle """
        pass

    def get_character_count(self): # real signature unknown; restored from __doc__
        """ get_character_count(self) -> int """
        return 0

    def get_context(self): # real signature unknown; restored from __doc__
        """ get_context(self) -> Pango.Context """
        pass

    def get_cursor_pos(self, index_): # real signature unknown; restored from __doc__
        """ get_cursor_pos(self, index_:int) -> strong_pos:Pango.Rectangle, weak_pos:Pango.Rectangle """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_direction(self, index): # real signature unknown; restored from __doc__
        """ get_direction(self, index:int) -> Pango.Direction """
        pass

    def get_ellipsize(self): # real signature unknown; restored from __doc__
        """ get_ellipsize(self) -> Pango.EllipsizeMode """
        pass

    def get_extents(self): # real signature unknown; restored from __doc__
        """ get_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_font_description(self): # real signature unknown; restored from __doc__
        """ get_font_description(self) -> Pango.FontDescription or None """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_indent(self): # real signature unknown; restored from __doc__
        """ get_indent(self) -> int """
        return 0

    def get_iter(self): # real signature unknown; restored from __doc__
        """ get_iter(self) -> Pango.LayoutIter """
        pass

    def get_justify(self): # real signature unknown; restored from __doc__
        """ get_justify(self) -> bool """
        return False

    def get_justify_last_line(self): # real signature unknown; restored from __doc__
        """ get_justify_last_line(self) -> bool """
        return False

    def get_line(self, line): # real signature unknown; restored from __doc__
        """ get_line(self, line:int) -> Pango.LayoutLine or None """
        pass

    def get_lines(self): # real signature unknown; restored from __doc__
        """ get_lines(self) -> list """
        return []

    def get_lines_readonly(self): # real signature unknown; restored from __doc__
        """ get_lines_readonly(self) -> list """
        return []

    def get_line_count(self): # real signature unknown; restored from __doc__
        """ get_line_count(self) -> int """
        return 0

    def get_line_readonly(self, line): # real signature unknown; restored from __doc__
        """ get_line_readonly(self, line:int) -> Pango.LayoutLine or None """
        pass

    def get_line_spacing(self): # real signature unknown; restored from __doc__
        """ get_line_spacing(self) -> float """
        return 0.0

    def get_log_attrs(self): # real signature unknown; restored from __doc__
        """ get_log_attrs(self) -> attrs:list """
        pass

    def get_log_attrs_readonly(self): # real signature unknown; restored from __doc__
        """ get_log_attrs_readonly(self) -> list """
        return []

    def get_pixel_extents(self): # real signature unknown; restored from __doc__
        """ get_pixel_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_pixel_size(self): # real signature unknown; restored from __doc__
        """ get_pixel_size(self) -> width:int, height:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_serial(self): # real signature unknown; restored from __doc__
        """ get_serial(self) -> int """
        return 0

    def get_single_paragraph_mode(self): # real signature unknown; restored from __doc__
        """ get_single_paragraph_mode(self) -> bool """
        return False

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def get_spacing(self): # real signature unknown; restored from __doc__
        """ get_spacing(self) -> int """
        return 0

    def get_tabs(self): # real signature unknown; restored from __doc__
        """ get_tabs(self) -> Pango.TabArray or None """
        pass

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str """
        return ""

    def get_unknown_glyphs_count(self): # real signature unknown; restored from __doc__
        """ get_unknown_glyphs_count(self) -> int """
        return 0

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_wrap(self): # real signature unknown; restored from __doc__
        """ get_wrap(self) -> Pango.WrapMode """
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

    def index_to_line_x(self, index_, trailing): # real signature unknown; restored from __doc__
        """ index_to_line_x(self, index_:int, trailing:bool) -> line:int, x_pos:int """
        pass

    def index_to_pos(self, index_): # real signature unknown; restored from __doc__
        """ index_to_pos(self, index_:int) -> pos:Pango.Rectangle """
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

    def is_ellipsized(self): # real signature unknown; restored from __doc__
        """ is_ellipsized(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_wrapped(self): # real signature unknown; restored from __doc__
        """ is_wrapped(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def move_cursor_visually(self, strong, old_index, old_trailing, direction): # real signature unknown; restored from __doc__
        """ move_cursor_visually(self, strong:bool, old_index:int, old_trailing:int, direction:int) -> new_index:int, new_trailing:int """
        pass

    def new(self, context): # real signature unknown; restored from __doc__
        """ new(context:Pango.Context) -> Pango.Layout """
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

    def serialize(self, flags): # real signature unknown; restored from __doc__
        """ serialize(self, flags:Pango.LayoutSerializeFlags) -> GLib.Bytes """
        pass

    def set_alignment(self, alignment): # real signature unknown; restored from __doc__
        """ set_alignment(self, alignment:Pango.Alignment) """
        pass

    def set_attributes(self, attrs=None): # real signature unknown; restored from __doc__
        """ set_attributes(self, attrs:Pango.AttrList=None) """
        pass

    def set_auto_dir(self, auto_dir): # real signature unknown; restored from __doc__
        """ set_auto_dir(self, auto_dir:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_ellipsize(self, ellipsize): # real signature unknown; restored from __doc__
        """ set_ellipsize(self, ellipsize:Pango.EllipsizeMode) """
        pass

    def set_font_description(self, desc=None): # real signature unknown; restored from __doc__
        """ set_font_description(self, desc:Pango.FontDescription=None) """
        pass

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:int) """
        pass

    def set_indent(self, indent): # real signature unknown; restored from __doc__
        """ set_indent(self, indent:int) """
        pass

    def set_justify(self, justify): # real signature unknown; restored from __doc__
        """ set_justify(self, justify:bool) """
        pass

    def set_justify_last_line(self, justify): # real signature unknown; restored from __doc__
        """ set_justify_last_line(self, justify:bool) """
        pass

    def set_line_spacing(self, factor): # real signature unknown; restored from __doc__
        """ set_line_spacing(self, factor:float) """
        pass

    def set_markup(self, text, length=-1): # reliably restored by inspect
        # no doc
        pass

    def set_markup_with_accel(self, markup, length, accel_marker): # real signature unknown; restored from __doc__
        """ set_markup_with_accel(self, markup:str, length:int, accel_marker:str) -> accel_char:str """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_single_paragraph_mode(self, setting): # real signature unknown; restored from __doc__
        """ set_single_paragraph_mode(self, setting:bool) """
        pass

    def set_spacing(self, spacing): # real signature unknown; restored from __doc__
        """ set_spacing(self, spacing:int) """
        pass

    def set_tabs(self, tabs=None): # real signature unknown; restored from __doc__
        """ set_tabs(self, tabs:Pango.TabArray=None) """
        pass

    def set_text(self, text, length=-1): # reliably restored by inspect
        # no doc
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:int) """
        pass

    def set_wrap(self, wrap): # real signature unknown; restored from __doc__
        """ set_wrap(self, wrap:Pango.WrapMode) """
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

    def write_to_file(self, flags, filename): # real signature unknown; restored from __doc__
        """ write_to_file(self, flags:Pango.LayoutSerializeFlags, filename:str) -> bool """
        return False

    def xy_to_index(self, x, y): # real signature unknown; restored from __doc__
        """ xy_to_index(self, x:int, y:int) -> bool, index_:int, trailing:int """
        return False

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
    def __new__(cls, context): # reliably restored by inspect
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x0000028033703f40>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Pango', '__firstlineno__': 56, '__new__': <staticmethod(<function Layout.__new__ at 0x0000028035132ae0>)>, 'set_markup': <function Layout.set_markup at 0x0000028035132c40>, 'set_text': <function Layout.set_text at 0x0000028035132da0>, '__static_attributes__': (), '__doc__': None, '__gsignals__': {}})"
    __firstlineno__ = 56
    __gdoc__ = 'Object PangoLayout\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType PangoLayout (842607872)>'
    __info__ = ObjectInfo(Layout)
    __static_attributes__ = ()


