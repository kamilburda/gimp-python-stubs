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


from .ToggleButtonAccessible import ToggleButtonAccessible

class MenuButtonAccessible(ToggleButtonAccessible):
    """
    :Constructors:
    
    ::
    
        MenuButtonAccessible(**properties)
    """
    def add_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ add_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
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

    def connect_widget_destroyed(self): # real signature unknown; restored from __doc__
        """ connect_widget_destroyed(self) """
        pass

    def contains(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ contains(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_action(self, i): # real signature unknown; restored from __doc__
        """ do_action(self, i:int) -> bool """
        return False

    def do_active_descendant_changed(self, *args, **kwargs): # real signature unknown
        """ active_descendant_changed(self, child=None) """
        pass

    def do_children_changed(self, *args, **kwargs): # real signature unknown
        """ children_changed(self, change_index:int, changed_child=None) """
        pass

    def do_connect_widget_destroyed(self, *args, **kwargs): # real signature unknown
        """ connect_widget_destroyed(self) """
        pass

    def do_constructed(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_focus_event(self, *args, **kwargs): # real signature unknown
        """ focus_event(self, focus_in:bool) """
        pass

    def do_get_attributes(self, *args, **kwargs): # real signature unknown
        """ get_attributes(self) -> list """
        pass

    def do_get_description(self, *args, **kwargs): # real signature unknown
        """ get_description(self) -> str """
        pass

    def do_get_index_in_parent(self, *args, **kwargs): # real signature unknown
        """ get_index_in_parent(self) -> int """
        pass

    def do_get_layer(self, *args, **kwargs): # real signature unknown
        """ get_layer(self) -> Atk.Layer """
        pass

    def do_get_mdi_zorder(self, *args, **kwargs): # real signature unknown
        """ get_mdi_zorder(self) -> int """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_get_n_children(self, *args, **kwargs): # real signature unknown
        """ get_n_children(self) -> int """
        pass

    def do_get_object_locale(self, *args, **kwargs): # real signature unknown
        """ get_object_locale(self) -> str """
        pass

    def do_get_parent(self, *args, **kwargs): # real signature unknown
        """ get_parent(self) -> Atk.Object """
        pass

    def do_get_role(self, *args, **kwargs): # real signature unknown
        """ get_role(self) -> Atk.Role """
        pass

    def do_initialize(self, *args, **kwargs): # real signature unknown
        """ initialize(self, data=None) """
        pass

    def do_property_change(self, *args, **kwargs): # real signature unknown
        """ property_change(self, values:Atk.PropertyValues) """
        pass

    def do_ref_relation_set(self, *args, **kwargs): # real signature unknown
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def do_ref_state_set(self, *args, **kwargs): # real signature unknown
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def do_remove_property_change_handler(self, *args, **kwargs): # real signature unknown
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def do_set_description(self, *args, **kwargs): # real signature unknown
        """ set_description(self, description:str) """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str) """
        pass

    def do_set_parent(self, *args, **kwargs): # real signature unknown
        """ set_parent(self, parent:Atk.Object) """
        pass

    def do_set_role(self, *args, **kwargs): # real signature unknown
        """ set_role(self, role:Atk.Role) """
        pass

    def do_state_change(self, *args, **kwargs): # real signature unknown
        """ state_change(self, name:str, state_set:bool) """
        pass

    def do_visible_data_changed(self, *args, **kwargs): # real signature unknown
        """ visible_data_changed(self) """
        pass

    def do_widget_set(self, *args, **kwargs): # real signature unknown
        """ widget_set(self) """
        pass

    def do_widget_unset(self, *args, **kwargs): # real signature unknown
        """ widget_unset(self) """
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

    def get_accessible_id(self): # real signature unknown; restored from __doc__
        """ get_accessible_id(self) -> str """
        return ""

    def get_alpha(self): # real signature unknown; restored from __doc__
        """ get_alpha(self) -> float """
        return 0.0

    def get_attributes(self): # real signature unknown; restored from __doc__
        """ get_attributes(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_extents(self, coord_type): # real signature unknown; restored from __doc__
        """ get_extents(self, coord_type:Atk.CoordType) -> x:int, y:int, width:int, height:int """
        pass

    def get_help_text(self): # real signature unknown; restored from __doc__
        """ get_help_text(self) -> str """
        return ""

    def get_image_description(self): # real signature unknown; restored from __doc__
        """ get_image_description(self) -> str """
        return ""

    def get_image_locale(self): # real signature unknown; restored from __doc__
        """ get_image_locale(self) -> str or None """
        return ""

    def get_image_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_image_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_image_size(self): # real signature unknown; restored from __doc__
        """ get_image_size(self) -> width:int, height:int """
        pass

    def get_index_in_parent(self): # real signature unknown; restored from __doc__
        """ get_index_in_parent(self) -> int """
        return 0

    def get_keybinding(self, i): # real signature unknown; restored from __doc__
        """ get_keybinding(self, i:int) -> str or None """
        return ""

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Atk.Layer """
        pass

    def get_localized_name(self, i): # real signature unknown; restored from __doc__
        """ get_localized_name(self, i:int) -> str or None """
        return ""

    def get_mdi_zorder(self): # real signature unknown; restored from __doc__
        """ get_mdi_zorder(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_accessible_children(self): # real signature unknown; restored from __doc__
        """ get_n_accessible_children(self) -> int """
        return 0

    def get_n_actions(self): # real signature unknown; restored from __doc__
        """ get_n_actions(self) -> int """
        return 0

    def get_object_locale(self): # real signature unknown; restored from __doc__
        """ get_object_locale(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Atk.Object """
        pass

    def get_position(self, coord_type): # real signature unknown; restored from __doc__
        """ get_position(self, coord_type:Atk.CoordType) -> x:int, y:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_role(self): # real signature unknown; restored from __doc__
        """ get_role(self) -> Atk.Role """
        pass

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> width:int, height:int """
        pass

    def get_widget(self): # real signature unknown; restored from __doc__
        """ get_widget(self) -> Gtk.Widget or None """
        pass

    def grab_focus(self): # real signature unknown; restored from __doc__
        """ grab_focus(self) -> bool """
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

    def initialize(self, data=None): # real signature unknown; restored from __doc__
        """ initialize(self, data=None) """
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

    def notify_state_change(self, state, value): # real signature unknown; restored from __doc__
        """ notify_state_change(self, state:int, value:bool) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def peek_parent(self): # real signature unknown; restored from __doc__
        """ peek_parent(self) -> Atk.Object """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_accessible_at_point(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ ref_accessible_at_point(self, x:int, y:int, coord_type:Atk.CoordType) -> Atk.Object or None """
        pass

    def ref_accessible_child(self, i): # real signature unknown; restored from __doc__
        """ ref_accessible_child(self, i:int) -> Atk.Object """
        pass

    def ref_relation_set(self): # real signature unknown; restored from __doc__
        """ ref_relation_set(self) -> Atk.RelationSet """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_state_set(self): # real signature unknown; restored from __doc__
        """ ref_state_set(self) -> Atk.StateSet """
        pass

    def remove_focus_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_focus_handler(self, handler_id:int) """
        pass

    def remove_property_change_handler(self, handler_id): # real signature unknown; restored from __doc__
        """ remove_property_change_handler(self, handler_id:int) """
        pass

    def remove_relationship(self, relationship, target): # real signature unknown; restored from __doc__
        """ remove_relationship(self, relationship:Atk.RelationType, target:Atk.Object) -> bool """
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

    def scroll_to(self, type): # real signature unknown; restored from __doc__
        """ scroll_to(self, type:Atk.ScrollType) -> bool """
        return False

    def scroll_to_point(self, coords, x, y): # real signature unknown; restored from __doc__
        """ scroll_to_point(self, coords:Atk.CoordType, x:int, y:int) -> bool """
        return False

    def set_accessible_id(self, id): # real signature unknown; restored from __doc__
        """ set_accessible_id(self, id:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_description(self, description): # real signature unknown; restored from __doc__
        """ set_description(self, description:str) """
        pass

    def set_extents(self, x, y, width, height, coord_type): # real signature unknown; restored from __doc__
        """ set_extents(self, x:int, y:int, width:int, height:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_help_text(self, help_text): # real signature unknown; restored from __doc__
        """ set_help_text(self, help_text:str) """
        pass

    def set_image_description(self, description): # real signature unknown; restored from __doc__
        """ set_image_description(self, description:str) -> bool """
        return False

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_parent(self, parent): # real signature unknown; restored from __doc__
        """ set_parent(self, parent:Atk.Object) """
        pass

    def set_position(self, x, y, coord_type): # real signature unknown; restored from __doc__
        """ set_position(self, x:int, y:int, coord_type:Atk.CoordType) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_role(self, role): # real signature unknown; restored from __doc__
        """ set_role(self, role:Atk.Role) """
        pass

    def set_size(self, width, height): # real signature unknown; restored from __doc__
        """ set_size(self, width:int, height:int) -> bool """
        return False

    def set_widget(self, widget=None): # real signature unknown; restored from __doc__
        """ set_widget(self, widget:Gtk.Widget=None) """
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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    accessible_parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    relation_set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd190b370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MenuButtonAccessible), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkMenuButtonAccessible (3427493008)>, '__doc__': None, '__gsignals__': {}, 'parent': <property object at 0x000002bfd18b49f0>, 'priv': <property object at 0x000002bfd18b4ae0>})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkMenuButtonAccessible\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nSignals from AtkComponent:\n  bounds-changed (AtkRectangle)\n\nProperties from GtkAccessible:\n  widget -> GtkWidget: Widget\n    The widget referenced by this accessible.\n\nSignals from AtkObject:\n  children-changed (guint, gpointer)\n  focus-event (gboolean)\n  property-change (gpointer)\n  state-change (gchararray, gboolean)\n  visible-data-changed ()\n  active-descendant-changed (gpointer)\n  announcement (gchararray)\n  notification (gchararray, gint)\n  attribute-changed (gchararray, gchararray)\n\nProperties from AtkObject:\n  accessible-name -> gchararray: Accessible Name\n    Object instance’s name formatted for assistive technology access\n  accessible-description -> gchararray: Accessible Description\n    Description of an object, formatted for assistive technology access\n  accessible-parent -> AtkObject: Accessible Parent\n    Parent of the current accessible as returned by atk_object_get_parent()\n  accessible-value -> gdouble: Accessible Value\n    Is used to notify that the value has changed\n  accessible-role -> AtkRole: Accessible Role\n    The accessible role of this object\n  accessible-component-layer -> gint: Accessible Layer\n    The accessible layer of this object\n  accessible-component-mdi-zorder -> gint: Accessible MDI Value\n    The accessible MDI value of this object\n  accessible-table-caption -> gchararray: Accessible Table Caption\n    Is used to notify that the table caption has changed; this property should not be used. accessible-table-caption-object should be used instead\n  accessible-table-column-description -> gchararray: Accessible Table Column Description\n    Is used to notify that the table column description has changed\n  accessible-table-column-header -> AtkObject: Accessible Table Column Header\n    Is used to notify that the table column header has changed\n  accessible-table-row-description -> gchararray: Accessible Table Row Description\n    Is used to notify that the table row description has changed\n  accessible-table-row-header -> AtkObject: Accessible Table Row Header\n    Is used to notify that the table row header has changed\n  accessible-table-summary -> AtkObject: Accessible Table Summary\n    Is used to notify that the table summary has changed\n  accessible-table-caption-object -> AtkObject: Accessible Table Caption Object\n    Is used to notify that the table caption has changed\n  accessible-hypertext-nlinks -> gint: Number of Accessible Hypertext Links\n    The number of links which the current AtkHypertext has\n  accessible-id -> gchararray: Accessible ID\n    ID for the accessible; useful for automated testing\n  accessible-help-text -> gchararray: Help text\n    Help text associated with the accessible\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkMenuButtonAccessible (3427493008)>'
    __info__ = ObjectInfo(MenuButtonAccessible)
    __static_attributes__ = ()


