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


from .CellRendererText import CellRendererText

class CellRendererSpin(CellRendererText):
    """
    :Constructors:
    
    ::
    
        CellRendererSpin(**properties)
        new() -> Gtk.CellRenderer
    """
    def activate(self, event, widget, path, background_area, cell_area, flags): # real signature unknown; restored from __doc__
        """ activate(self, event:Gdk.Event, widget:Gtk.Widget, path:str, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> bool """
        return False

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

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self, event:Gdk.Event, widget:Gtk.Widget, path:str, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> bool """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_edited(self, *args, **kwargs): # real signature unknown
        """ edited(self, path:str, new_text:str) """
        pass

    def do_editing_canceled(self, *args, **kwargs): # real signature unknown
        """ editing_canceled(self) """
        pass

    def do_editing_started(self, *args, **kwargs): # real signature unknown
        """ editing_started(self, editable:Gtk.CellEditable, path:str) """
        pass

    def do_get_aligned_area(self, *args, **kwargs): # real signature unknown
        """ get_aligned_area(self, widget:Gtk.Widget, flags:Gtk.CellRendererState, cell_area:Gdk.Rectangle) -> aligned_area:Gdk.Rectangle """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self, widget:Gtk.Widget) -> minimum_size:int, natural_size:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, widget:Gtk.Widget, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self, widget:Gtk.Widget) -> minimum_size:int, natural_size:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, widget:Gtk.Widget, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_get_size(self, *args, **kwargs): # real signature unknown
        """ get_size(self, widget:Gtk.Widget, cell_area:Gdk.Rectangle=None) -> x_offset:int, y_offset:int, width:int, height:int """
        pass

    def do_render(self, *args, **kwargs): # real signature unknown
        """ render(self, cr:cairo.Context, widget:Gtk.Widget, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) """
        pass

    def do_start_editing(self, *args, **kwargs): # real signature unknown
        """ start_editing(self, event:Gdk.Event=None, widget:Gtk.Widget, path:str, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> Gtk.CellEditable or None """
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

    def get_aligned_area(self, widget, flags, cell_area): # real signature unknown; restored from __doc__
        """ get_aligned_area(self, widget:Gtk.Widget, flags:Gtk.CellRendererState, cell_area:Gdk.Rectangle) -> aligned_area:Gdk.Rectangle """
        pass

    def get_alignment(self): # real signature unknown; restored from __doc__
        """ get_alignment(self) -> xalign:float, yalign:float """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_fixed_size(self): # real signature unknown; restored from __doc__
        """ get_fixed_size(self) -> width:int, height:int """
        pass

    def get_padding(self): # real signature unknown; restored from __doc__
        """ get_padding(self) -> xpad:int, ypad:int """
        pass

    def get_preferred_height(self, widget): # real signature unknown; restored from __doc__
        """ get_preferred_height(self, widget:Gtk.Widget) -> minimum_size:int, natural_size:int """
        pass

    def get_preferred_height_for_width(self, widget, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, widget:Gtk.Widget, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_size(self, widget): # real signature unknown; restored from __doc__
        """ get_preferred_size(self, widget:Gtk.Widget) -> minimum_size:Gtk.Requisition, natural_size:Gtk.Requisition """
        pass

    def get_preferred_width(self, widget): # real signature unknown; restored from __doc__
        """ get_preferred_width(self, widget:Gtk.Widget) -> minimum_size:int, natural_size:int """
        pass

    def get_preferred_width_for_height(self, widget, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, widget:Gtk.Widget, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_size(self, widget, cell_area=None): # real signature unknown; restored from __doc__
        """ get_size(self, widget:Gtk.Widget, cell_area:Gdk.Rectangle=None) -> x_offset:int, y_offset:int, width:int, height:int """
        pass

    def get_state(self, widget=None, cell_state): # real signature unknown; restored from __doc__
        """ get_state(self, widget:Gtk.Widget=None, cell_state:Gtk.CellRendererState) -> Gtk.StateFlags """
        pass

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

    def is_activatable(self): # real signature unknown; restored from __doc__
        """ is_activatable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.CellRenderer """
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

    def render(self, cr, widget, background_area, cell_area, flags): # real signature unknown; restored from __doc__
        """ render(self, cr:cairo.Context, widget:Gtk.Widget, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) """
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

    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
        pass

    def set_alignment(self, xalign, yalign): # real signature unknown; restored from __doc__
        """ set_alignment(self, xalign:float, yalign:float) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_fixed_height_from_font(self, number_of_rows): # real signature unknown; restored from __doc__
        """ set_fixed_height_from_font(self, number_of_rows:int) """
        pass

    def set_fixed_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_fixed_size(self, width:int, height:int) """
        pass

    def set_padding(self, xpad, ypad): # real signature unknown; restored from __doc__
        """ set_padding(self, xpad:int, ypad:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def start_editing(self, event=None, widget, path, background_area, cell_area, flags): # real signature unknown; restored from __doc__
        """ start_editing(self, event:Gdk.Event=None, widget:Gtk.Widget, path:str, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> Gtk.CellEditable or None """
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_editing(self, canceled): # real signature unknown; restored from __doc__
        """ stop_editing(self, canceled:bool) """
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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd17efa60>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CellRendererSpin), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkCellRendererSpin (3427457856)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'parent': <property object at 0x000002bfd178d300>, 'priv': <property object at 0x000002bfd178d3f0>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkCellRendererSpin\n\nProperties from GtkCellRendererSpin:\n  adjustment -> GtkAdjustment: Adjustment\n    The adjustment that holds the value of the spin button\n  climb-rate -> gdouble: Climb rate\n    The acceleration rate when you hold down a button\n  digits -> guint: Digits\n    The number of decimal places to display\n\nSignals from GtkCellRendererText:\n  edited (gchararray, gchararray)\n\nProperties from GtkCellRendererText:\n  text -> gchararray: Text\n    Text to render\n  markup -> gchararray: Markup\n    Marked up text to render\n  attributes -> PangoAttrList: Attributes\n    A list of style attributes to apply to the text of the renderer\n  single-paragraph-mode -> gboolean: Single Paragraph Mode\n    Whether to keep all text in a single paragraph\n  width-chars -> gint: Width In Characters\n    The desired width of the label, in characters\n  max-width-chars -> gint: Maximum Width In Characters\n    The maximum width of the cell, in characters\n  wrap-width -> gint: Wrap width\n    The width at which the text is wrapped\n  alignment -> PangoAlignment: Alignment\n    How to align the lines\n  placeholder-text -> gchararray: Placeholder text\n    Text rendered when an editable cell is empty\n  background -> gchararray: Background color name\n    Background color as a string\n  foreground -> gchararray: Foreground color name\n    Foreground color as a string\n  background-gdk -> GdkColor: Background color\n    Background color as a GdkColor\n  foreground-gdk -> GdkColor: Foreground color\n    Foreground color as a GdkColor\n  background-rgba -> GdkRGBA: Background color as RGBA\n    Background color as a GdkRGBA\n  foreground-rgba -> GdkRGBA: Foreground color as RGBA\n    Foreground color as a GdkRGBA\n  font -> gchararray: Font\n    Font description as a string, e.g. "Sans Italic 12"\n  font-desc -> PangoFontDescription: Font\n    Font description as a PangoFontDescription struct\n  family -> gchararray: Font family\n    Name of the font family, e.g. Sans, Helvetica, Times, Monospace\n  style -> PangoStyle: Font style\n    Font style\n  variant -> PangoVariant: Font variant\n    Font variant\n  weight -> gint: Font weight\n    Font weight\n  stretch -> PangoStretch: Font stretch\n    Font stretch\n  size -> gint: Font size\n    Font size\n  size-points -> gdouble: Font points\n    Font size in points\n  scale -> gdouble: Font scale\n    Font scaling factor\n  editable -> gboolean: Editable\n    Whether the text can be modified by the user\n  strikethrough -> gboolean: Strikethrough\n    Whether to strike through the text\n  underline -> PangoUnderline: Underline\n    Style of underline for this text\n  rise -> gint: Rise\n    Offset of text above the baseline (below the baseline if rise is negative)\n  language -> gchararray: Language\n    The language this text is in, as an ISO code. Pango can use this as a hint when rendering the text. If you don\'t understand this parameter, you probably don\'t need it\n  ellipsize -> PangoEllipsizeMode: Ellipsize\n    The preferred place to ellipsize the string, if the cell renderer does not have enough room to display the entire string\n  wrap-mode -> PangoWrapMode: Wrap mode\n    How to break the string into multiple lines, if the cell renderer does not have enough room to display the entire string\n  background-set -> gboolean: Background set\n    Whether this tag affects the background color\n  foreground-set -> gboolean: Foreground set\n    Whether this tag affects the foreground color\n  family-set -> gboolean: Font family set\n    Whether this tag affects the font family\n  style-set -> gboolean: Font style set\n    Whether this tag affects the font style\n  variant-set -> gboolean: Font variant set\n    Whether this tag affects the font variant\n  weight-set -> gboolean: Font weight set\n    Whether this tag affects the font weight\n  stretch-set -> gboolean: Font stretch set\n    Whether this tag affects the font stretch\n  size-set -> gboolean: Font size set\n    Whether this tag affects the font size\n  scale-set -> gboolean: Font scale set\n    Whether this tag scales the font size by a factor\n  editable-set -> gboolean: Editability set\n    Whether this tag affects text editability\n  strikethrough-set -> gboolean: Strikethrough set\n    Whether this tag affects strikethrough\n  underline-set -> gboolean: Underline set\n    Whether this tag affects underlining\n  rise-set -> gboolean: Rise set\n    Whether this tag affects the rise\n  language-set -> gboolean: Language set\n    Whether this tag affects the language the text is rendered as\n  ellipsize-set -> gboolean: Ellipsize set\n    Whether this tag affects the ellipsize mode\n  align-set -> gboolean: Align set\n    Whether this tag affects the alignment mode\n\nSignals from GtkCellRenderer:\n  editing-canceled ()\n  editing-started (GtkCellEditable, gchararray)\n\nProperties from GtkCellRenderer:\n  mode -> GtkCellRendererMode: mode\n    Editable mode of the CellRenderer\n  visible -> gboolean: visible\n    Display the cell\n  sensitive -> gboolean: Sensitive\n    Display the cell sensitive\n  xalign -> gfloat: xalign\n    The x-align\n  yalign -> gfloat: yalign\n    The y-align\n  xpad -> guint: xpad\n    The xpad\n  ypad -> guint: ypad\n    The ypad\n  width -> gint: width\n    The fixed width\n  height -> gint: height\n    The fixed height\n  is-expander -> gboolean: Is Expander\n    Row has children\n  is-expanded -> gboolean: Is Expanded\n    Row is an expander row, and is expanded\n  cell-background -> gchararray: Cell background color name\n    Cell background color as a string\n  cell-background-gdk -> GdkColor: Cell background color\n    Cell background color as a GdkColor\n  cell-background-rgba -> GdkRGBA: Cell background RGBA color\n    Cell background color as a GdkRGBA\n  cell-background-set -> gboolean: Cell background set\n    Whether the cell background color is set\n  editing -> gboolean: Editing\n    Whether the cell renderer is currently in editing mode\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkCellRendererSpin (3427457856)>'
    __info__ = ObjectInfo(CellRendererSpin)
    __static_attributes__ = ()


