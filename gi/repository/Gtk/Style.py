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


class Style(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Style(**properties)
        new() -> Gtk.Style
    """
    def apply_default_background(self, cr, window, state_type, x, y, width, height): # real signature unknown; restored from __doc__
        """ apply_default_background(self, cr:cairo.Context, window:Gdk.Window, state_type:Gtk.StateType, x:int, y:int, width:int, height:int) """
        pass

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
        """ copy(self) -> Gtk.Style """
        pass

    def detach(self): # real signature unknown; restored from __doc__
        """ detach(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_copy(self, *args, **kwargs): # real signature unknown
        """ copy(self, src:Gtk.Style) """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_draw_arrow(self, *args, **kwargs): # real signature unknown
        """ draw_arrow(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, arrow_type:Gtk.ArrowType, fill:bool, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_box(self, *args, **kwargs): # real signature unknown
        """ draw_box(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_box_gap(self, *args, **kwargs): # real signature unknown
        """ draw_box_gap(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType, gap_x:int, gap_width:int) """
        pass

    def do_draw_check(self, *args, **kwargs): # real signature unknown
        """ draw_check(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_diamond(self, *args, **kwargs): # real signature unknown
        """ draw_diamond(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_expander(self, *args, **kwargs): # real signature unknown
        """ draw_expander(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, x:int, y:int, expander_style:Gtk.ExpanderStyle) """
        pass

    def do_draw_extension(self, *args, **kwargs): # real signature unknown
        """ draw_extension(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType) """
        pass

    def do_draw_flat_box(self, *args, **kwargs): # real signature unknown
        """ draw_flat_box(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_focus(self, *args, **kwargs): # real signature unknown
        """ draw_focus(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_handle(self, *args, **kwargs): # real signature unknown
        """ draw_handle(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int, orientation:Gtk.Orientation) """
        pass

    def do_draw_hline(self, *args, **kwargs): # real signature unknown
        """ draw_hline(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, x1:int, x2:int, y:int) """
        pass

    def do_draw_layout(self, *args, **kwargs): # real signature unknown
        """ draw_layout(self, cr:cairo.Context, state_type:Gtk.StateType, use_text:bool, widget:Gtk.Widget, detail:str, x:int, y:int, layout:Pango.Layout) """
        pass

    def do_draw_option(self, *args, **kwargs): # real signature unknown
        """ draw_option(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_resize_grip(self, *args, **kwargs): # real signature unknown
        """ draw_resize_grip(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, edge:Gdk.WindowEdge, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_shadow(self, *args, **kwargs): # real signature unknown
        """ draw_shadow(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_shadow_gap(self, *args, **kwargs): # real signature unknown
        """ draw_shadow_gap(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int, gap_side:Gtk.PositionType, gap_x:int, gap_width:int) """
        pass

    def do_draw_slider(self, *args, **kwargs): # real signature unknown
        """ draw_slider(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int, orientation:Gtk.Orientation) """
        pass

    def do_draw_spinner(self, *args, **kwargs): # real signature unknown
        """ draw_spinner(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, step:int, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_tab(self, *args, **kwargs): # real signature unknown
        """ draw_tab(self, cr:cairo.Context, state_type:Gtk.StateType, shadow_type:Gtk.ShadowType, widget:Gtk.Widget, detail:str, x:int, y:int, width:int, height:int) """
        pass

    def do_draw_vline(self, *args, **kwargs): # real signature unknown
        """ draw_vline(self, cr:cairo.Context, state_type:Gtk.StateType, widget:Gtk.Widget, detail:str, y1_:int, y2_:int, x:int) """
        pass

    def do_init_from_rc(self, *args, **kwargs): # real signature unknown
        """ init_from_rc(self, rc_style:Gtk.RcStyle) """
        pass

    def do_realize(self, *args, **kwargs): # real signature unknown
        """ realize(self) """
        pass

    def do_render_icon(self, *args, **kwargs): # real signature unknown
        """ render_icon(self, source:Gtk.IconSource, direction:Gtk.TextDirection, state:Gtk.StateType, size:int, widget:Gtk.Widget=None, detail:str=None) -> GdkPixbuf.Pixbuf """
        pass

    def do_set_background(self, *args, **kwargs): # real signature unknown
        """ set_background(self, window:Gdk.Window, state_type:Gtk.StateType) """
        pass

    def do_unrealize(self, *args, **kwargs): # real signature unknown
        """ unrealize(self) """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_style_property(self, widget_type, property_name): # real signature unknown; restored from __doc__
        """ get_style_property(self, widget_type:GType, property_name:str) -> value:GObject.Value """
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

    def has_context(self): # real signature unknown; restored from __doc__
        """ has_context(self) -> bool """
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

    def lookup_color(self, color_name): # real signature unknown; restored from __doc__
        """ lookup_color(self, color_name:str) -> bool, color:Gdk.Color """
        return False

    def lookup_icon_set(self, stock_id): # real signature unknown; restored from __doc__
        """ lookup_icon_set(self, stock_id:str) -> Gtk.IconSet """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.Style """
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

    def render_icon(self, source, direction, state, size, widget=None, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, source:Gtk.IconSource, direction:Gtk.TextDirection, state:Gtk.StateType, size:int, widget:Gtk.Widget=None, detail:str=None) -> GdkPixbuf.Pixbuf """
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

    def set_background(self, window, state_type): # real signature unknown; restored from __doc__
        """ set_background(self, window:Gdk.Window, state_type:Gtk.StateType) """
        pass

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

    attach_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    background = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    black = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_factories = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_font_desc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    property_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rc_style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    styles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_aa = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    visual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    white = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xthickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ythickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd190e0b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Style), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkStyle (3418528544)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'apply_default_background': gi.FunctionInfo(apply_default_background), 'copy': gi.FunctionInfo(copy), 'detach': gi.FunctionInfo(detach), 'get_style_property': gi.FunctionInfo(get_style_property), 'has_context': gi.FunctionInfo(has_context), 'lookup_color': gi.FunctionInfo(lookup_color), 'lookup_icon_set': gi.FunctionInfo(lookup_icon_set), 'render_icon': gi.FunctionInfo(render_icon), 'set_background': gi.FunctionInfo(set_background), 'do_copy': gi.VFuncInfo(copy), 'do_draw_arrow': gi.VFuncInfo(draw_arrow), 'do_draw_box': gi.VFuncInfo(draw_box), 'do_draw_box_gap': gi.VFuncInfo(draw_box_gap), 'do_draw_check': gi.VFuncInfo(draw_check), 'do_draw_diamond': gi.VFuncInfo(draw_diamond), 'do_draw_expander': gi.VFuncInfo(draw_expander), 'do_draw_extension': gi.VFuncInfo(draw_extension), 'do_draw_flat_box': gi.VFuncInfo(draw_flat_box), 'do_draw_focus': gi.VFuncInfo(draw_focus), 'do_draw_handle': gi.VFuncInfo(draw_handle), 'do_draw_hline': gi.VFuncInfo(draw_hline), 'do_draw_layout': gi.VFuncInfo(draw_layout), 'do_draw_option': gi.VFuncInfo(draw_option), 'do_draw_resize_grip': gi.VFuncInfo(draw_resize_grip), 'do_draw_shadow': gi.VFuncInfo(draw_shadow), 'do_draw_shadow_gap': gi.VFuncInfo(draw_shadow_gap), 'do_draw_slider': gi.VFuncInfo(draw_slider), 'do_draw_spinner': gi.VFuncInfo(draw_spinner), 'do_draw_tab': gi.VFuncInfo(draw_tab), 'do_draw_vline': gi.VFuncInfo(draw_vline), 'do_init_from_rc': gi.VFuncInfo(init_from_rc), 'do_realize': gi.VFuncInfo(realize), 'do_render_icon': gi.VFuncInfo(render_icon), 'do_set_background': gi.VFuncInfo(set_background), 'do_unrealize': gi.VFuncInfo(unrealize), 'parent_instance': <property object at 0x000002bfd39fd3f0>, 'fg': <property object at 0x000002bfd39fd4e0>, 'bg': <property object at 0x000002bfd39fd5d0>, 'light': <property object at 0x000002bfd39fd6c0>, 'dark': <property object at 0x000002bfd39fd7b0>, 'mid': <property object at 0x000002bfd39fd8a0>, 'text': <property object at 0x000002bfd39fd990>, 'base': <property object at 0x000002bfd39fda80>, 'text_aa': <property object at 0x000002bfd39fdb70>, 'black': <property object at 0x000002bfd39fdc60>, 'white': <property object at 0x000002bfd39fdd50>, 'font_desc': <property object at 0x000002bfd39fde40>, 'xthickness': <property object at 0x000002bfd39fdf30>, 'ythickness': <property object at 0x000002bfd39fe020>, 'background': <property object at 0x000002bfd39fe110>, 'attach_count': <property object at 0x000002bfd39fe200>, 'visual': <property object at 0x000002bfd39fe2f0>, 'private_font_desc': <property object at 0x000002bfd39fe3e0>, 'rc_style': <property object at 0x000002bfd39fe4d0>, 'styles': <property object at 0x000002bfd39fe5c0>, 'property_cache': <property object at 0x000002bfd39fe6b0>, 'icon_factories': <property object at 0x000002bfd39fe7a0>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkStyle\n\nSignals from GtkStyle:\n  realize ()\n  unrealize ()\n\nProperties from GtkStyle:\n  context -> GtkStyleContext: Style context\n    GtkStyleContext to get style from\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkStyle (3418528544)>'
    __info__ = ObjectInfo(Style)
    __static_attributes__ = ()


