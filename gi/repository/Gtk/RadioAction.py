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


from .RadioAction import RadioAction

class RadioAction(RadioAction):
    """
    :Constructors:
    
    ::
    
        RadioAction(**properties)
        new(name:str, label:str=None, tooltip:str=None, stock_id:str=None, value:int) -> Gtk.RadioAction
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def block_activate(self): # real signature unknown; restored from __doc__
        """ block_activate(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_accelerator(self): # real signature unknown; restored from __doc__
        """ connect_accelerator(self) """
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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_icon(self, icon_size): # real signature unknown; restored from __doc__
        """ create_icon(self, icon_size:int) -> Gtk.Widget """
        pass

    def create_menu(self): # real signature unknown; restored from __doc__
        """ create_menu(self) -> Gtk.Widget """
        pass

    def create_menu_item(self): # real signature unknown; restored from __doc__
        """ create_menu_item(self) -> Gtk.Widget """
        pass

    def create_tool_item(self): # real signature unknown; restored from __doc__
        """ create_tool_item(self) -> Gtk.Widget """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_accelerator(self): # real signature unknown; restored from __doc__
        """ disconnect_accelerator(self) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self, current:Gtk.RadioAction) """
        pass

    def do_connect_proxy(self, *args, **kwargs): # real signature unknown
        """ connect_proxy(self, proxy:Gtk.Widget) """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_create_menu(self, *args, **kwargs): # real signature unknown
        """ create_menu(self) -> Gtk.Widget """
        pass

    def do_create_menu_item(self, *args, **kwargs): # real signature unknown
        """ create_menu_item(self) -> Gtk.Widget """
        pass

    def do_create_tool_item(self, *args, **kwargs): # real signature unknown
        """ create_tool_item(self) -> Gtk.Widget """
        pass

    def do_disconnect_proxy(self, *args, **kwargs): # real signature unknown
        """ disconnect_proxy(self, proxy:Gtk.Widget) """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_toggled(self, *args, **kwargs): # real signature unknown
        """ toggled(self) """
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

    def get_accel_closure(self): # real signature unknown; restored from __doc__
        """ get_accel_closure(self) -> GObject.Closure """
        pass

    def get_accel_path(self): # real signature unknown; restored from __doc__
        """ get_accel_path(self) -> str """
        return ""

    def get_active(self): # real signature unknown; restored from __doc__
        """ get_active(self) -> bool """
        return False

    def get_always_show_image(self): # real signature unknown; restored from __doc__
        """ get_always_show_image(self) -> bool """
        return False

    def get_current_value(self): # real signature unknown; restored from __doc__
        """ get_current_value(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_draw_as_radio(self): # real signature unknown; restored from __doc__
        """ get_draw_as_radio(self) -> bool """
        return False

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon """
        pass

    def get_group(self): # real signature unknown; restored from __doc__
        """ get_group(self) -> list """
        return []

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_is_important(self): # real signature unknown; restored from __doc__
        """ get_is_important(self) -> bool """
        return False

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxies(self): # real signature unknown; restored from __doc__
        """ get_proxies(self) -> list """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_short_label(self): # real signature unknown; restored from __doc__
        """ get_short_label(self) -> str """
        return ""

    def get_stock_id(self): # real signature unknown; restored from __doc__
        """ get_stock_id(self) -> str """
        return ""

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visible_horizontal(self): # real signature unknown; restored from __doc__
        """ get_visible_horizontal(self) -> bool """
        return False

    def get_visible_vertical(self): # real signature unknown; restored from __doc__
        """ get_visible_vertical(self) -> bool """
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

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def join_group(self, group_source=None): # real signature unknown; restored from __doc__
        """ join_group(self, group_source:Gtk.RadioAction=None) """
        pass

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def new(self, name, label=None, tooltip=None, stock_id=None, value): # real signature unknown; restored from __doc__
        """ new(name:str, label:str=None, tooltip:str=None, stock_id:str=None, value:int) -> Gtk.RadioAction """
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

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
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

    def set_accel_group(self, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_group(self, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accel_path(self, accel_path): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str) """
        pass

    def set_active(self, is_active): # real signature unknown; restored from __doc__
        """ set_active(self, is_active:bool) """
        pass

    def set_always_show_image(self, always_show): # real signature unknown; restored from __doc__
        """ set_always_show_image(self, always_show:bool) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_current_value(self, current_value): # real signature unknown; restored from __doc__
        """ set_current_value(self, current_value:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_draw_as_radio(self, draw_as_radio): # real signature unknown; restored from __doc__
        """ set_draw_as_radio(self, draw_as_radio:bool) """
        pass

    def set_gicon(self, icon): # real signature unknown; restored from __doc__
        """ set_gicon(self, icon:Gio.Icon) """
        pass

    def set_group(self, group=None): # real signature unknown; restored from __doc__
        """ set_group(self, group:list=None) """
        pass

    def set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str) """
        pass

    def set_is_important(self, is_important): # real signature unknown; restored from __doc__
        """ set_is_important(self, is_important:bool) """
        pass

    def set_label(self, label): # real signature unknown; restored from __doc__
        """ set_label(self, label:str) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_short_label(self, short_label): # real signature unknown; restored from __doc__
        """ set_short_label(self, short_label:str) """
        pass

    def set_stock_id(self, stock_id): # real signature unknown; restored from __doc__
        """ set_stock_id(self, stock_id:str) """
        pass

    def set_tooltip(self, tooltip): # real signature unknown; restored from __doc__
        """ set_tooltip(self, tooltip:str) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visible_horizontal(self, visible_horizontal): # real signature unknown; restored from __doc__
        """ set_visible_horizontal(self, visible_horizontal:bool) """
        pass

    def set_visible_vertical(self, visible_vertical): # real signature unknown; restored from __doc__
        """ set_visible_vertical(self, visible_vertical:bool) """
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

    def toggled(self): # real signature unknown; restored from __doc__
        """ toggled(self) """
        pass

    def unblock_activate(self): # real signature unknown; restored from __doc__
        """ unblock_activate(self) """
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

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        """
        Initializer for a GObject based classes with support for property
        sets through the use of explicit keyword arguments.
        """
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

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd19074f0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 231, '__init__': <function deprecated_init.<locals>.new_init at 0x000002bfce4d62a0>, '__static_attributes__': (), '__doc__': None, '__gsignals__': {}})"
    __firstlineno__ = 231
    __gdoc__ = 'Object GtkRadioAction\n\nSignals from GtkRadioAction:\n  changed (GtkRadioAction)\n\nProperties from GtkRadioAction:\n  value -> gint: The value\n    The value returned by gtk_radio_action_get_current_value() when this action is the current action of its group.\n  group -> GtkRadioAction: Group\n    The radio action whose group this action belongs to.\n  current-value -> gint: The current value\n    The value property of the currently active member of the group to which this action belongs.\n\nSignals from GtkToggleAction:\n  toggled ()\n\nProperties from GtkToggleAction:\n  draw-as-radio -> gboolean: Create the same proxies as a radio action\n    Whether the proxies for this action look like radio action proxies\n  active -> gboolean: Active\n    Whether the toggle action should be active\n\nSignals from GtkAction:\n  activate ()\n\nProperties from GtkAction:\n  name -> gchararray: Name\n    A unique name for the action.\n  label -> gchararray: Label\n    The label used for menu items and buttons that activate this action.\n  short-label -> gchararray: Short label\n    A shorter label that may be used on toolbar buttons.\n  tooltip -> gchararray: Tooltip\n    A tooltip for this action.\n  stock-id -> gchararray: Stock Icon\n    The stock icon displayed in widgets representing this action.\n  icon-name -> gchararray: Icon Name\n    The name of the icon from the icon theme\n  gicon -> GIcon: GIcon\n    The GIcon being displayed\n  visible-horizontal -> gboolean: Visible when horizontal\n    Whether the toolbar item is visible when the toolbar is in a horizontal orientation.\n  visible-vertical -> gboolean: Visible when vertical\n    Whether the toolbar item is visible when the toolbar is in a vertical orientation.\n  visible-overflown -> gboolean: Visible when overflown\n    When TRUE, toolitem proxies for this action are represented in the toolbar overflow menu.\n  is-important -> gboolean: Is important\n    Whether the action is considered important. When TRUE, toolitem proxies for this action show text in GTK_TOOLBAR_BOTH_HORIZ mode.\n  hide-if-empty -> gboolean: Hide if empty\n    When TRUE, empty menu proxies for this action are hidden.\n  sensitive -> gboolean: Sensitive\n    Whether the action is enabled.\n  visible -> gboolean: Visible\n    Whether the action is visible.\n  action-group -> GtkActionGroup: Action Group\n    The GtkActionGroup this GtkAction is associated with, or NULL (for internal use).\n  always-show-image -> gboolean: Always show image\n    Whether the image will always be shown\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkRadioAction (3413531904)>'
    __info__ = ObjectInfo(RadioAction)
    __static_attributes__ = ()


