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


class TextTag(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        TextTag(**properties)
        new(name:str=None) -> Gtk.TextTag
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, size_changed): # real signature unknown; restored from __doc__
        """ changed(self, size_changed:bool) """
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

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, event_object:GObject.Object, event:Gdk.Event, iter:Gtk.TextIter) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def event(self, event_object, event, iter): # real signature unknown; restored from __doc__
        """ event(self, event_object:GObject.Object, event:Gdk.Event, iter:Gtk.TextIter) -> bool """
        return False

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

    def get_priority(self): # real signature unknown; restored from __doc__
        """ get_priority(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    @classmethod
    def new(cls, name=None): # real signature unknown; restored from __doc__
        """ new(name:str=None) -> Gtk.TextTag """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_priority(self, priority): # real signature unknown; restored from __doc__
        """ set_priority(self, priority:int) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd191c370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(TextTag), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkTextTag (3414246960)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'changed': gi.FunctionInfo(changed), 'event': gi.FunctionInfo(event), 'get_priority': gi.FunctionInfo(get_priority), 'set_priority': gi.FunctionInfo(set_priority), 'do_event': gi.VFuncInfo(event), 'parent_instance': <property object at 0x000002bfd3a16700>, 'priv': <property object at 0x000002bfd3a16930>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkTextTag\n\nSignals from GtkTextTag:\n  event (GObject, GdkEvent, GtkTextIter) -> gboolean\n\nProperties from GtkTextTag:\n  name -> gchararray: Tag name\n    Name used to refer to the text tag. NULL for anonymous tags\n  background -> gchararray: Background color name\n    Background color as a string\n  foreground -> gchararray: Foreground color name\n    Foreground color as a string\n  background-gdk -> GdkColor: Background color\n    Background color as a GdkColor\n  foreground-gdk -> GdkColor: Foreground color\n    Foreground color as a GdkColor\n  background-rgba -> GdkRGBA: Background RGBA\n    Background color as a GdkRGBA\n  foreground-rgba -> GdkRGBA: Foreground RGBA\n    Foreground color as a GdkRGBA\n  font -> gchararray: Font\n    Font description as a string, e.g. "Sans Italic 12"\n  font-desc -> PangoFontDescription: Font\n    Font description as a PangoFontDescription struct\n  family -> gchararray: Font family\n    Name of the font family, e.g. Sans, Helvetica, Times, Monospace\n  style -> PangoStyle: Font style\n    Font style as a PangoStyle, e.g. PANGO_STYLE_ITALIC\n  variant -> PangoVariant: Font variant\n    Font variant as a PangoVariant, e.g. PANGO_VARIANT_SMALL_CAPS\n  weight -> gint: Font weight\n    Font weight as an integer, see predefined values in PangoWeight; for example, PANGO_WEIGHT_BOLD\n  stretch -> PangoStretch: Font stretch\n    Font stretch as a PangoStretch, e.g. PANGO_STRETCH_CONDENSED\n  size -> gint: Font size\n    Font size in Pango units\n  size-points -> gdouble: Font points\n    Font size in points\n  scale -> gdouble: Font scale\n    Font size as a scale factor relative to the default font size. This properly adapts to theme changes etc. so is recommended. Pango predefines some scales such as PANGO_SCALE_X_LARGE\n  pixels-above-lines -> gint: Pixels above lines\n    Pixels of blank space above paragraphs\n  pixels-below-lines -> gint: Pixels below lines\n    Pixels of blank space below paragraphs\n  pixels-inside-wrap -> gint: Pixels inside wrap\n    Pixels of blank space between wrapped lines in a paragraph\n  editable -> gboolean: Editable\n    Whether the text can be modified by the user\n  wrap-mode -> GtkWrapMode: Wrap mode\n    Whether to wrap lines never, at word boundaries, or at character boundaries\n  justification -> GtkJustification: Justification\n    Left, right, or center justification\n  direction -> GtkTextDirection: Text direction\n    Text direction, e.g. right-to-left or left-to-right\n  left-margin -> gint: Left margin\n    Width of the left margin in pixels\n  indent -> gint: Indent\n    Amount to indent the paragraph, in pixels\n  strikethrough -> gboolean: Strikethrough\n    Whether to strike through the text\n  strikethrough-rgba -> GdkRGBA: Strikethrough RGBA\n    Color of strikethrough for this text\n  right-margin -> gint: Right margin\n    Width of the right margin in pixels\n  underline -> PangoUnderline: Underline\n    Style of underline for this text\n  underline-rgba -> GdkRGBA: Underline RGBA\n    Color of underline for this text\n  rise -> gint: Rise\n    Offset of text above the baseline (below the baseline if rise is negative) in Pango units\n  background-full-height -> gboolean: Background full height\n    Whether the background color fills the entire line height or only the height of the tagged characters\n  language -> gchararray: Language\n    The language this text is in, as an ISO code. Pango can use this as a hint when rendering the text. If not set, an appropriate default will be used.\n  tabs -> PangoTabArray: Tabs\n    Custom tabs for this text\n  invisible -> gboolean: Invisible\n    Whether this text is hidden.\n  paragraph-background -> gchararray: Paragraph background color name\n    Paragraph background color as a string\n  paragraph-background-gdk -> GdkColor: Paragraph background color\n    Paragraph background color as a GdkColor\n  paragraph-background-rgba -> GdkRGBA: Paragraph background RGBA\n    Paragraph background RGBA as a GdkRGBA\n  fallback -> gboolean: Fallback\n    Whether font fallback is enabled.\n  letter-spacing -> gint: Letter Spacing\n    Extra spacing between graphemes\n  font-features -> gchararray: Font Features\n    OpenType Font Features to use\n  accumulative-margin -> gboolean: Margin Accumulates\n    Whether left and right margins accumulate.\n  background-set -> gboolean: Background set\n    Whether this tag affects the background color\n  foreground-set -> gboolean: Foreground set\n    Whether this tag affects the foreground color\n  family-set -> gboolean: Font family set\n    Whether this tag affects the font family\n  style-set -> gboolean: Font style set\n    Whether this tag affects the font style\n  variant-set -> gboolean: Font variant set\n    Whether this tag affects the font variant\n  weight-set -> gboolean: Font weight set\n    Whether this tag affects the font weight\n  stretch-set -> gboolean: Font stretch set\n    Whether this tag affects the font stretch\n  size-set -> gboolean: Font size set\n    Whether this tag affects the font size\n  scale-set -> gboolean: Font scale set\n    Whether this tag scales the font size by a factor\n  pixels-above-lines-set -> gboolean: Pixels above lines set\n    Whether this tag affects the number of pixels above lines\n  pixels-below-lines-set -> gboolean: Pixels below lines set\n    Whether this tag affects the number of pixels above lines\n  pixels-inside-wrap-set -> gboolean: Pixels inside wrap set\n    Whether this tag affects the number of pixels between wrapped lines\n  editable-set -> gboolean: Editability set\n    Whether this tag affects text editability\n  wrap-mode-set -> gboolean: Wrap mode set\n    Whether this tag affects line wrap mode\n  justification-set -> gboolean: Justification set\n    Whether this tag affects paragraph justification\n  left-margin-set -> gboolean: Left margin set\n    Whether this tag affects the left margin\n  indent-set -> gboolean: Indent set\n    Whether this tag affects indentation\n  strikethrough-set -> gboolean: Strikethrough set\n    Whether this tag affects strikethrough\n  strikethrough-rgba-set -> gboolean: Strikethrough RGBA set\n    Whether this tag affects strikethrough color\n  right-margin-set -> gboolean: Right margin set\n    Whether this tag affects the right margin\n  underline-set -> gboolean: Underline set\n    Whether this tag affects underlining\n  underline-rgba-set -> gboolean: Underline RGBA set\n    Whether this tag affects underlining color\n  rise-set -> gboolean: Rise set\n    Whether this tag affects the rise\n  background-full-height-set -> gboolean: Background full height set\n    Whether this tag affects background height\n  language-set -> gboolean: Language set\n    Whether this tag affects the language the text is rendered as\n  tabs-set -> gboolean: Tabs set\n    Whether this tag affects tabs\n  invisible-set -> gboolean: Invisible set\n    Whether this tag affects text visibility\n  paragraph-background-set -> gboolean: Paragraph background set\n    Whether this tag affects the paragraph background color\n  fallback-set -> gboolean: Fallback set\n    Whether this tag affects font fallback\n  letter-spacing-set -> gboolean: Letter spacing set\n    Whether this tag affects letter spacing\n  font-features-set -> gboolean: Font features set\n    Whether this tag affects font features\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkTextTag (3414246960)>'
    __info__ = ObjectInfo(TextTag)
    __static_attributes__ = ()


