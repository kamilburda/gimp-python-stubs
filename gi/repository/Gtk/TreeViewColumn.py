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


from .TreeViewColumn import TreeViewColumn

class TreeViewColumn(TreeViewColumn):
    """
    :Constructors:
    
    ::
    
        TreeViewColumn(**properties)
        new() -> Gtk.TreeViewColumn
        new_with_area(area:Gtk.CellArea) -> Gtk.TreeViewColumn
    """
    def add_attribute(self, cell_renderer, attribute, column): # real signature unknown; restored from __doc__
        """ add_attribute(self, cell_renderer:Gtk.CellRenderer, attribute:str, column:int) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cell_get_position(*args, **kwargs): # reliably restored by inspect
        """ cell_get_position(self, cell_renderer:Gtk.CellRenderer) -> bool, x_offset:int, width:int """
        pass

    def cell_get_size(self, cell_area=None): # real signature unknown; restored from __doc__
        """ cell_get_size(self, cell_area:Gdk.Rectangle=None) -> x_offset:int, y_offset:int, width:int, height:int """
        pass

    def cell_is_visible(self): # real signature unknown; restored from __doc__
        """ cell_is_visible(self) -> bool """
        return False

    def cell_set_cell_data(self, tree_model, iter, is_expander, is_expanded): # real signature unknown; restored from __doc__
        """ cell_set_cell_data(self, tree_model:Gtk.TreeModel, iter:Gtk.TreeIter, is_expander:bool, is_expanded:bool) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_attributes(self, cell_renderer): # real signature unknown; restored from __doc__
        """ clear_attributes(self, cell_renderer:Gtk.CellRenderer) """
        pass

    def clicked(self): # real signature unknown; restored from __doc__
        """ clicked(self) """
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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
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

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_clicked(self, *args, **kwargs): # real signature unknown
        """ clicked(self) """
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

    def focus_cell(self, cell): # real signature unknown; restored from __doc__
        """ focus_cell(self, cell:Gtk.CellRenderer) """
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
        """ get_alignment(self) -> float """
        return 0.0

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> Gtk.CellArea or None """
        pass

    def get_button(self): # real signature unknown; restored from __doc__
        """ get_button(self) -> Gtk.Widget """
        pass

    def get_cells(self): # real signature unknown; restored from __doc__
        """ get_cells(self) -> list """
        return []

    def get_clickable(self): # real signature unknown; restored from __doc__
        """ get_clickable(self) -> bool """
        return False

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_expand(self): # real signature unknown; restored from __doc__
        """ get_expand(self) -> bool """
        return False

    def get_fixed_width(self): # real signature unknown; restored from __doc__
        """ get_fixed_width(self) -> int """
        return 0

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_max_width(self): # real signature unknown; restored from __doc__
        """ get_max_width(self) -> int """
        return 0

    def get_min_width(self): # real signature unknown; restored from __doc__
        """ get_min_width(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_reorderable(self): # real signature unknown; restored from __doc__
        """ get_reorderable(self) -> bool """
        return False

    def get_resizable(self): # real signature unknown; restored from __doc__
        """ get_resizable(self) -> bool """
        return False

    def get_sizing(self): # real signature unknown; restored from __doc__
        """ get_sizing(self) -> Gtk.TreeViewColumnSizing """
        pass

    def get_sort_column_id(self): # real signature unknown; restored from __doc__
        """ get_sort_column_id(self) -> int """
        return 0

    def get_sort_indicator(self): # real signature unknown; restored from __doc__
        """ get_sort_indicator(self) -> bool """
        return False

    def get_sort_order(self): # real signature unknown; restored from __doc__
        """ get_sort_order(self) -> Gtk.SortType """
        pass

    def get_spacing(self): # real signature unknown; restored from __doc__
        """ get_spacing(self) -> int """
        return 0

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def get_tree_view(self): # real signature unknown; restored from __doc__
        """ get_tree_view(self) -> Gtk.Widget or None """
        pass

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_widget(self): # real signature unknown; restored from __doc__
        """ get_widget(self) -> Gtk.Widget or None """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_x_offset(self): # real signature unknown; restored from __doc__
        """ get_x_offset(self) -> int """
        return 0

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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.TreeViewColumn """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_with_area(self, area): # real signature unknown; restored from __doc__
        """ new_with_area(area:Gtk.CellArea) -> Gtk.TreeViewColumn """
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

    def pack_end(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_end(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def pack_start(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_start(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def queue_resize(self): # real signature unknown; restored from __doc__
        """ queue_resize(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def reorder(self, cell, position): # real signature unknown; restored from __doc__
        """ reorder(self, cell:Gtk.CellRenderer, position:int) """
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

    def set_alignment(self, xalign): # real signature unknown; restored from __doc__
        """ set_alignment(self, xalign:float) """
        pass

    def set_attributes(self, cell_renderer, **attributes): # reliably restored by inspect
        # no doc
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_cell_data_func(self, cell_renderer, func, func_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_clickable(self, clickable): # real signature unknown; restored from __doc__
        """ set_clickable(self, clickable:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_expand(self, expand): # real signature unknown; restored from __doc__
        """ set_expand(self, expand:bool) """
        pass

    def set_fixed_width(self, fixed_width): # real signature unknown; restored from __doc__
        """ set_fixed_width(self, fixed_width:int) """
        pass

    def set_max_width(self, max_width): # real signature unknown; restored from __doc__
        """ set_max_width(self, max_width:int) """
        pass

    def set_min_width(self, min_width): # real signature unknown; restored from __doc__
        """ set_min_width(self, min_width:int) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_reorderable(self, reorderable): # real signature unknown; restored from __doc__
        """ set_reorderable(self, reorderable:bool) """
        pass

    def set_resizable(self, resizable): # real signature unknown; restored from __doc__
        """ set_resizable(self, resizable:bool) """
        pass

    def set_sizing(self, type): # real signature unknown; restored from __doc__
        """ set_sizing(self, type:Gtk.TreeViewColumnSizing) """
        pass

    def set_sort_column_id(self, sort_column_id): # real signature unknown; restored from __doc__
        """ set_sort_column_id(self, sort_column_id:int) """
        pass

    def set_sort_indicator(self, setting): # real signature unknown; restored from __doc__
        """ set_sort_indicator(self, setting:bool) """
        pass

    def set_sort_order(self, order): # real signature unknown; restored from __doc__
        """ set_sort_order(self, order:Gtk.SortType) """
        pass

    def set_spacing(self, spacing): # real signature unknown; restored from __doc__
        """ set_spacing(self, spacing:int) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

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

    def __init__(self, title=None, cell_renderer=None, **attributes): # reliably restored by inspect
        # no doc
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1929450>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 1492, '__init__': <function TreeViewColumn.__init__ at 0x000002bfcebc8040>, 'cell_get_position': <function strip_boolean_result.<locals>.wrapped at 0x000002bfcebc80f0>, 'set_cell_data_func': <function TreeViewColumn.set_cell_data_func at 0x000002bfcebc81a0>, 'set_attributes': <function TreeViewColumn.set_attributes at 0x000002bfcebc8250>, '__static_attributes__': (), '__doc__': None, '__gsignals__': {}})"
    __firstlineno__ = 1492
    __gdoc__ = 'Object GtkTreeViewColumn\n\nSignals from GtkTreeViewColumn:\n  clicked ()\n\nProperties from GtkTreeViewColumn:\n  visible -> gboolean: Visible\n    Whether to display the column\n  resizable -> gboolean: Resizable\n    Column is user-resizable\n  x-offset -> gint: X position\n    Current X position of the column\n  width -> gint: Width\n    Current width of the column\n  spacing -> gint: Spacing\n    Space which is inserted between cells\n  sizing -> GtkTreeViewColumnSizing: Sizing\n    Resize mode of the column\n  fixed-width -> gint: Fixed Width\n    Current fixed width of the column\n  min-width -> gint: Minimum Width\n    Minimum allowed width of the column\n  max-width -> gint: Maximum Width\n    Maximum allowed width of the column\n  title -> gchararray: Title\n    Title to appear in column header\n  expand -> gboolean: Expand\n    Column gets share of extra width allocated to the widget\n  clickable -> gboolean: Clickable\n    Whether the header can be clicked\n  widget -> GtkWidget: Widget\n    Widget to put in column header button instead of column title\n  alignment -> gfloat: Alignment\n    X Alignment of the column header text or widget\n  reorderable -> gboolean: Reorderable\n    Whether the column can be reordered around the headers\n  sort-indicator -> gboolean: Sort indicator\n    Whether to show a sort indicator\n  sort-order -> GtkSortType: Sort order\n    Sort direction the sort indicator should indicate\n  sort-column-id -> gint: Sort column ID\n    Logical sort column ID this column sorts on when selected for sorting\n  cell-area -> GtkCellArea: Cell Area\n    The GtkCellArea used to layout cells\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkTreeViewColumn (3426603888)>'
    __info__ = ObjectInfo(TreeViewColumn)
    __static_attributes__ = ()


