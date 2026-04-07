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


class PageSetup(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        PageSetup(**properties)
        new() -> Gtk.PageSetup
        new_from_file(file_name:str) -> Gtk.PageSetup
        new_from_gvariant(variant:GLib.Variant) -> Gtk.PageSetup
        new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PageSetup
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

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.PageSetup """
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

    def get_bottom_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_bottom_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_left_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_left_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> Gtk.PageOrientation """
        pass

    def get_page_height(self, unit): # real signature unknown; restored from __doc__
        """ get_page_height(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_page_width(self, unit): # real signature unknown; restored from __doc__
        """ get_page_width(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_paper_height(self, unit): # real signature unknown; restored from __doc__
        """ get_paper_height(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_paper_size(self): # real signature unknown; restored from __doc__
        """ get_paper_size(self) -> Gtk.PaperSize """
        pass

    def get_paper_width(self, unit): # real signature unknown; restored from __doc__
        """ get_paper_width(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_right_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_right_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

    def get_top_margin(self, unit): # real signature unknown; restored from __doc__
        """ get_top_margin(self, unit:Gtk.Unit) -> float """
        return 0.0

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

    def load_file(self, file_name): # real signature unknown; restored from __doc__
        """ load_file(self, file_name:str) -> bool """
        return False

    def load_key_file(self, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ load_key_file(self, key_file:GLib.KeyFile, group_name:str=None) -> bool """
        return False

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.PageSetup """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    @classmethod
    def new_from_file(cls, file_name): # real signature unknown; restored from __doc__
        """ new_from_file(file_name:str) -> Gtk.PageSetup """
        pass

    @classmethod
    def new_from_gvariant(cls, variant): # real signature unknown; restored from __doc__
        """ new_from_gvariant(variant:GLib.Variant) -> Gtk.PageSetup """
        pass

    @classmethod
    def new_from_key_file(cls, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ new_from_key_file(key_file:GLib.KeyFile, group_name:str=None) -> Gtk.PageSetup """
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

    def set_bottom_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_bottom_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_left_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_left_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_orientation(self, orientation): # real signature unknown; restored from __doc__
        """ set_orientation(self, orientation:Gtk.PageOrientation) """
        pass

    def set_paper_size(self, size): # real signature unknown; restored from __doc__
        """ set_paper_size(self, size:Gtk.PaperSize) """
        pass

    def set_paper_size_and_default_margins(self, size): # real signature unknown; restored from __doc__
        """ set_paper_size_and_default_margins(self, size:Gtk.PaperSize) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_right_margin(self, margin:float, unit:Gtk.Unit) """
        pass

    def set_top_margin(self, margin, unit): # real signature unknown; restored from __doc__
        """ set_top_margin(self, margin:float, unit:Gtk.Unit) """
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

    def to_file(self, file_name): # real signature unknown; restored from __doc__
        """ to_file(self, file_name:str) -> bool """
        return False

    def to_gvariant(self): # real signature unknown; restored from __doc__
        """ to_gvariant(self) -> GLib.Variant """
        pass

    def to_key_file(self, key_file, group_name=None): # real signature unknown; restored from __doc__
        """ to_key_file(self, key_file:GLib.KeyFile, group_name:str=None) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd1913280>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(PageSetup), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkPageSetup (3540063616)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'new_from_file': <classmethod(gi.FunctionInfo(new_from_file))>, 'new_from_gvariant': <classmethod(gi.FunctionInfo(new_from_gvariant))>, 'new_from_key_file': <classmethod(gi.FunctionInfo(new_from_key_file))>, 'copy': gi.FunctionInfo(copy), 'get_bottom_margin': gi.FunctionInfo(get_bottom_margin), 'get_left_margin': gi.FunctionInfo(get_left_margin), 'get_orientation': gi.FunctionInfo(get_orientation), 'get_page_height': gi.FunctionInfo(get_page_height), 'get_page_width': gi.FunctionInfo(get_page_width), 'get_paper_height': gi.FunctionInfo(get_paper_height), 'get_paper_size': gi.FunctionInfo(get_paper_size), 'get_paper_width': gi.FunctionInfo(get_paper_width), 'get_right_margin': gi.FunctionInfo(get_right_margin), 'get_top_margin': gi.FunctionInfo(get_top_margin), 'load_file': gi.FunctionInfo(load_file), 'load_key_file': gi.FunctionInfo(load_key_file), 'set_bottom_margin': gi.FunctionInfo(set_bottom_margin), 'set_left_margin': gi.FunctionInfo(set_left_margin), 'set_orientation': gi.FunctionInfo(set_orientation), 'set_paper_size': gi.FunctionInfo(set_paper_size), 'set_paper_size_and_default_margins': gi.FunctionInfo(set_paper_size_and_default_margins), 'set_right_margin': gi.FunctionInfo(set_right_margin), 'set_top_margin': gi.FunctionInfo(set_top_margin), 'to_file': gi.FunctionInfo(to_file), 'to_gvariant': gi.FunctionInfo(to_gvariant), 'to_key_file': gi.FunctionInfo(to_key_file)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkPageSetup\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkPageSetup (3540063616)>'
    __info__ = ObjectInfo(PageSetup)
    __static_attributes__ = ()


