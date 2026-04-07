# encoding: utf-8
# module gi.repository.Gtk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


class ThemingEngine(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        ThemingEngine(**properties)
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

    def do_render_activity(self, *args, **kwargs): # real signature unknown
        """ render_activity(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_arrow(self, *args, **kwargs): # real signature unknown
        """ render_arrow(self, cr:cairo.Context, angle:float, x:float, y:float, size:float) """
        pass

    def do_render_background(self, *args, **kwargs): # real signature unknown
        """ render_background(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_check(self, *args, **kwargs): # real signature unknown
        """ render_check(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_expander(self, *args, **kwargs): # real signature unknown
        """ render_expander(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_extension(self, *args, **kwargs): # real signature unknown
        """ render_extension(self, cr:cairo.Context, x:float, y:float, width:float, height:float, gap_side:Gtk.PositionType) """
        pass

    def do_render_focus(self, *args, **kwargs): # real signature unknown
        """ render_focus(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_frame(self, *args, **kwargs): # real signature unknown
        """ render_frame(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_frame_gap(self, *args, **kwargs): # real signature unknown
        """ render_frame_gap(self, cr:cairo.Context, x:float, y:float, width:float, height:float, gap_side:Gtk.PositionType, xy0_gap:float, xy1_gap:float) """
        pass

    def do_render_handle(self, *args, **kwargs): # real signature unknown
        """ render_handle(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_icon(self, *args, **kwargs): # real signature unknown
        """ render_icon(self, cr:cairo.Context, pixbuf:GdkPixbuf.Pixbuf, x:float, y:float) """
        pass

    def do_render_icon_surface(self, *args, **kwargs): # real signature unknown
        """ render_icon_surface(self, cr:cairo.Context, surface:cairo.Surface, x:float, y:float) """
        pass

    def do_render_layout(self, *args, **kwargs): # real signature unknown
        """ render_layout(self, cr:cairo.Context, x:float, y:float, layout:Pango.Layout) """
        pass

    def do_render_line(self, *args, **kwargs): # real signature unknown
        """ render_line(self, cr:cairo.Context, x0:float, y0:float, x1:float, y1:float) """
        pass

    def do_render_option(self, *args, **kwargs): # real signature unknown
        """ render_option(self, cr:cairo.Context, x:float, y:float, width:float, height:float) """
        pass

    def do_render_slider(self, *args, **kwargs): # real signature unknown
        """ render_slider(self, cr:cairo.Context, x:float, y:float, width:float, height:float, orientation:Gtk.Orientation) """
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

    def get_background_color(self, state): # real signature unknown; restored from __doc__
        """ get_background_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_border(self, state): # real signature unknown; restored from __doc__
        """ get_border(self, state:Gtk.StateFlags) -> border:Gtk.Border """
        pass

    def get_border_color(self, state): # real signature unknown; restored from __doc__
        """ get_border_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_color(self, state): # real signature unknown; restored from __doc__
        """ get_color(self, state:Gtk.StateFlags) -> color:Gdk.RGBA """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_direction(self): # real signature unknown; restored from __doc__
        """ get_direction(self) -> Gtk.TextDirection """
        pass

    def get_font(self, state): # real signature unknown; restored from __doc__
        """ get_font(self, state:Gtk.StateFlags) -> Pango.FontDescription """
        pass

    def get_junction_sides(self): # real signature unknown; restored from __doc__
        """ get_junction_sides(self) -> Gtk.JunctionSides """
        pass

    def get_margin(self, state): # real signature unknown; restored from __doc__
        """ get_margin(self, state:Gtk.StateFlags) -> margin:Gtk.Border """
        pass

    def get_padding(self, state): # real signature unknown; restored from __doc__
        """ get_padding(self, state:Gtk.StateFlags) -> padding:Gtk.Border """
        pass

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> Gtk.WidgetPath """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, property, state): # real signature unknown; restored from __doc__
        """ get_property(self, property:str, state:Gtk.StateFlags) -> value:GObject.Value """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_screen(self): # real signature unknown; restored from __doc__
        """ get_screen(self) -> Gdk.Screen or None """
        pass

    def get_state(self): # real signature unknown; restored from __doc__
        """ get_state(self) -> Gtk.StateFlags """
        pass

    def get_style_property(self, property_name): # real signature unknown; restored from __doc__
        """ get_style_property(self, property_name:str) -> value:GObject.Value """
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

    def has_class(self, style_class): # real signature unknown; restored from __doc__
        """ has_class(self, style_class:str) -> bool """
        return False

    def has_region(self, style_region): # real signature unknown; restored from __doc__
        """ has_region(self, style_region:str) -> bool, flags:Gtk.RegionFlags """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load(self, name): # real signature unknown; restored from __doc__
        """ load(name:str) -> Gtk.ThemingEngine or None """
        pass

    def lookup_color(self, color_name): # real signature unknown; restored from __doc__
        """ lookup_color(self, color_name:str) -> bool, color:Gdk.RGBA """
        return False

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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def state_is_running(self, state): # real signature unknown; restored from __doc__
        """ state_is_running(self, state:Gtk.StateType) -> bool, progress:float """
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

    parent_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1913f10>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ThemingEngine), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkThemingEngine (3414247152)>, '__doc__': None, '__gsignals__': {}, 'load': <staticmethod(gi.FunctionInfo(load))>, 'get_background_color': gi.FunctionInfo(get_background_color), 'get_border': gi.FunctionInfo(get_border), 'get_border_color': gi.FunctionInfo(get_border_color), 'get_color': gi.FunctionInfo(get_color), 'get_direction': gi.FunctionInfo(get_direction), 'get_font': gi.FunctionInfo(get_font), 'get_junction_sides': gi.FunctionInfo(get_junction_sides), 'get_margin': gi.FunctionInfo(get_margin), 'get_padding': gi.FunctionInfo(get_padding), 'get_path': gi.FunctionInfo(get_path), 'get_property': gi.FunctionInfo(get_property), 'get_screen': gi.FunctionInfo(get_screen), 'get_state': gi.FunctionInfo(get_state), 'get_style_property': gi.FunctionInfo(get_style_property), 'has_class': gi.FunctionInfo(has_class), 'has_region': gi.FunctionInfo(has_region), 'lookup_color': gi.FunctionInfo(lookup_color), 'state_is_running': gi.FunctionInfo(state_is_running), 'do_render_activity': gi.VFuncInfo(render_activity), 'do_render_arrow': gi.VFuncInfo(render_arrow), 'do_render_background': gi.VFuncInfo(render_background), 'do_render_check': gi.VFuncInfo(render_check), 'do_render_expander': gi.VFuncInfo(render_expander), 'do_render_extension': gi.VFuncInfo(render_extension), 'do_render_focus': gi.VFuncInfo(render_focus), 'do_render_frame': gi.VFuncInfo(render_frame), 'do_render_frame_gap': gi.VFuncInfo(render_frame_gap), 'do_render_handle': gi.VFuncInfo(render_handle), 'do_render_icon': gi.VFuncInfo(render_icon), 'do_render_icon_surface': gi.VFuncInfo(render_icon_surface), 'do_render_layout': gi.VFuncInfo(render_layout), 'do_render_line': gi.VFuncInfo(render_line), 'do_render_option': gi.VFuncInfo(render_option), 'do_render_slider': gi.VFuncInfo(render_slider), 'parent_object': <property object at 0x000002bfd3a1d940>, 'priv': <property object at 0x000002bfd3a1d6c0>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkThemingEngine\n\nProperties from GtkThemingEngine:\n  name -> gchararray: Name\n    Theming engine name\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkThemingEngine (3414247152)>'
    __info__ = ObjectInfo(ThemingEngine)
    __static_attributes__ = ()


