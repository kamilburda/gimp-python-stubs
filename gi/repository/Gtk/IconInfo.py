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


class IconInfo(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        IconInfo(**properties)
        new_for_pixbuf(icon_theme:Gtk.IconTheme, pixbuf:GdkPixbuf.Pixbuf) -> Gtk.IconInfo
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

    def get_attach_points(self): # real signature unknown; restored from __doc__
        """ get_attach_points(self) -> bool, points:list """
        return False

    def get_base_scale(self): # real signature unknown; restored from __doc__
        """ get_base_scale(self) -> int """
        return 0

    def get_base_size(self): # real signature unknown; restored from __doc__
        """ get_base_size(self) -> int """
        return 0

    def get_builtin_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_builtin_pixbuf(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_embedded_rect(self): # real signature unknown; restored from __doc__
        """ get_embedded_rect(self) -> bool, rectangle:Gdk.Rectangle """
        return False

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str or None """
        return ""

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

    def is_symbolic(self): # real signature unknown; restored from __doc__
        """ is_symbolic(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def load_icon(self): # real signature unknown; restored from __doc__
        """ load_icon(self) -> GdkPixbuf.Pixbuf """
        pass

    def load_icon_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_icon_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_icon_finish(self, res): # real signature unknown; restored from __doc__
        """ load_icon_finish(self, res:Gio.AsyncResult) -> GdkPixbuf.Pixbuf """
        pass

    def load_surface(self, for_window=None): # real signature unknown; restored from __doc__
        """ load_surface(self, for_window:Gdk.Window=None) -> cairo.Surface """
        pass

    def load_symbolic(self, fg, success_color=None, warning_color=None, error_color=None): # real signature unknown; restored from __doc__
        """ load_symbolic(self, fg:Gdk.RGBA, success_color:Gdk.RGBA=None, warning_color:Gdk.RGBA=None, error_color:Gdk.RGBA=None) -> GdkPixbuf.Pixbuf, was_symbolic:bool """
        pass

    def load_symbolic_async(self, fg, success_color=None, warning_color=None, error_color=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_symbolic_async(self, fg:Gdk.RGBA, success_color:Gdk.RGBA=None, warning_color:Gdk.RGBA=None, error_color:Gdk.RGBA=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_symbolic_finish(self, res): # real signature unknown; restored from __doc__
        """ load_symbolic_finish(self, res:Gio.AsyncResult) -> GdkPixbuf.Pixbuf, was_symbolic:bool """
        pass

    def load_symbolic_for_context(self, context): # real signature unknown; restored from __doc__
        """ load_symbolic_for_context(self, context:Gtk.StyleContext) -> GdkPixbuf.Pixbuf, was_symbolic:bool """
        pass

    def load_symbolic_for_context_async(self, context, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_symbolic_for_context_async(self, context:Gtk.StyleContext, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_symbolic_for_context_finish(self, res): # real signature unknown; restored from __doc__
        """ load_symbolic_for_context_finish(self, res:Gio.AsyncResult) -> GdkPixbuf.Pixbuf, was_symbolic:bool """
        pass

    def load_symbolic_for_style(self, style, state): # real signature unknown; restored from __doc__
        """ load_symbolic_for_style(self, style:Gtk.Style, state:Gtk.StateType) -> GdkPixbuf.Pixbuf, was_symbolic:bool """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_for_pixbuf(cls, icon_theme, pixbuf): # real signature unknown; restored from __doc__
        """ new_for_pixbuf(icon_theme:Gtk.IconTheme, pixbuf:GdkPixbuf.Pixbuf) -> Gtk.IconInfo """
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

    def set_raw_coordinates(self, raw_coordinates): # real signature unknown; restored from __doc__
        """ set_raw_coordinates(self, raw_coordinates:bool) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1905c00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(IconInfo), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkIconInfo (3538515584)>, '__doc__': None, '__gsignals__': {}, 'new_for_pixbuf': <classmethod(gi.FunctionInfo(new_for_pixbuf))>, 'get_attach_points': gi.FunctionInfo(get_attach_points), 'get_base_scale': gi.FunctionInfo(get_base_scale), 'get_base_size': gi.FunctionInfo(get_base_size), 'get_builtin_pixbuf': gi.FunctionInfo(get_builtin_pixbuf), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_embedded_rect': gi.FunctionInfo(get_embedded_rect), 'get_filename': gi.FunctionInfo(get_filename), 'is_symbolic': gi.FunctionInfo(is_symbolic), 'load_icon': gi.FunctionInfo(load_icon), 'load_icon_async': gi.FunctionInfo(load_icon_async), 'load_icon_finish': gi.FunctionInfo(load_icon_finish), 'load_surface': gi.FunctionInfo(load_surface), 'load_symbolic': gi.FunctionInfo(load_symbolic), 'load_symbolic_async': gi.FunctionInfo(load_symbolic_async), 'load_symbolic_finish': gi.FunctionInfo(load_symbolic_finish), 'load_symbolic_for_context': gi.FunctionInfo(load_symbolic_for_context), 'load_symbolic_for_context_async': gi.FunctionInfo(load_symbolic_for_context_async), 'load_symbolic_for_context_finish': gi.FunctionInfo(load_symbolic_for_context_finish), 'load_symbolic_for_style': gi.FunctionInfo(load_symbolic_for_style), 'set_raw_coordinates': gi.FunctionInfo(set_raw_coordinates)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkIconInfo\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkIconInfo (3538515584)>'
    __info__ = ObjectInfo(IconInfo)
    __static_attributes__ = ()


