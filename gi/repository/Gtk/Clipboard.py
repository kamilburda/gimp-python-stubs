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


class Clipboard(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Clipboard(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
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

    def get(self, selection): # real signature unknown; restored from __doc__
        """ get(selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self, display): # real signature unknown; restored from __doc__
        """ get_default(display:Gdk.Display) -> Gtk.Clipboard """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_for_display(self, display, selection): # real signature unknown; restored from __doc__
        """ get_for_display(display:Gdk.Display, selection:Gdk.Atom) -> Gtk.Clipboard """
        pass

    def get_owner(self): # real signature unknown; restored from __doc__
        """ get_owner(self) -> GObject.Object or None """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_selection(self): # real signature unknown; restored from __doc__
        """ get_selection(self) -> Gdk.Atom """
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

    def request_contents(self, target, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_contents(self, target:Gdk.Atom, callback:Gtk.ClipboardReceivedFunc, user_data=None) """
        pass

    def request_image(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_image(self, callback:Gtk.ClipboardImageReceivedFunc, user_data=None) """
        pass

    def request_rich_text(self, buffer, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_rich_text(self, buffer:Gtk.TextBuffer, callback:Gtk.ClipboardRichTextReceivedFunc, user_data=None) """
        pass

    def request_targets(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_targets(self, callback:Gtk.ClipboardTargetsReceivedFunc, user_data=None) """
        pass

    def request_text(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_text(self, callback:Gtk.ClipboardTextReceivedFunc, user_data=None) """
        pass

    def request_uris(self, callback, user_data=None): # real signature unknown; restored from __doc__
        """ request_uris(self, callback:Gtk.ClipboardURIReceivedFunc, user_data=None) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_can_store(self, targets=None): # real signature unknown; restored from __doc__
        """ set_can_store(self, targets:list=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_image(self, pixbuf): # real signature unknown; restored from __doc__
        """ set_image(self, pixbuf:GdkPixbuf.Pixbuf) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_text(self, text, len): # real signature unknown; restored from __doc__
        """ set_text(self, text:str, len:int) """
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

    def store(self): # real signature unknown; restored from __doc__
        """ store(self) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def wait_for_contents(self, target): # real signature unknown; restored from __doc__
        """ wait_for_contents(self, target:Gdk.Atom) -> Gtk.SelectionData or None """
        pass

    def wait_for_image(self): # real signature unknown; restored from __doc__
        """ wait_for_image(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def wait_for_rich_text(self, buffer): # real signature unknown; restored from __doc__
        """ wait_for_rich_text(self, buffer:Gtk.TextBuffer) -> list or None, format:Gdk.Atom """
        return []

    def wait_for_targets(self): # real signature unknown; restored from __doc__
        """ wait_for_targets(self) -> bool, targets:list """
        return False

    def wait_for_text(self): # real signature unknown; restored from __doc__
        """ wait_for_text(self) -> str or None """
        return ""

    def wait_for_uris(self): # real signature unknown; restored from __doc__
        """ wait_for_uris(self) -> list or None """
        return []

    def wait_is_image_available(self): # real signature unknown; restored from __doc__
        """ wait_is_image_available(self) -> bool """
        return False

    def wait_is_rich_text_available(self, buffer): # real signature unknown; restored from __doc__
        """ wait_is_rich_text_available(self, buffer:Gtk.TextBuffer) -> bool """
        return False

    def wait_is_target_available(self, target): # real signature unknown; restored from __doc__
        """ wait_is_target_available(self, target:Gdk.Atom) -> bool """
        return False

    def wait_is_text_available(self): # real signature unknown; restored from __doc__
        """ wait_is_text_available(self) -> bool """
        return False

    def wait_is_uris_available(self): # real signature unknown; restored from __doc__
        """ wait_is_uris_available(self) -> bool """
        return False

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd17f5db0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Clipboard), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkClipboard (3418537760)>, '__doc__': None, '__gsignals__': {}, 'get': <staticmethod(gi.FunctionInfo(get))>, 'get_default': <staticmethod(gi.FunctionInfo(get_default))>, 'get_for_display': <staticmethod(gi.FunctionInfo(get_for_display))>, 'clear': gi.FunctionInfo(clear), 'get_display': gi.FunctionInfo(get_display), 'get_owner': gi.FunctionInfo(get_owner), 'get_selection': gi.FunctionInfo(get_selection), 'request_contents': gi.FunctionInfo(request_contents), 'request_image': gi.FunctionInfo(request_image), 'request_rich_text': gi.FunctionInfo(request_rich_text), 'request_targets': gi.FunctionInfo(request_targets), 'request_text': gi.FunctionInfo(request_text), 'request_uris': gi.FunctionInfo(request_uris), 'set_can_store': gi.FunctionInfo(set_can_store), 'set_image': gi.FunctionInfo(set_image), 'set_text': gi.FunctionInfo(set_text), 'store': gi.FunctionInfo(store), 'wait_for_contents': gi.FunctionInfo(wait_for_contents), 'wait_for_image': gi.FunctionInfo(wait_for_image), 'wait_for_rich_text': gi.FunctionInfo(wait_for_rich_text), 'wait_for_targets': gi.FunctionInfo(wait_for_targets), 'wait_for_text': gi.FunctionInfo(wait_for_text), 'wait_for_uris': gi.FunctionInfo(wait_for_uris), 'wait_is_image_available': gi.FunctionInfo(wait_is_image_available), 'wait_is_rich_text_available': gi.FunctionInfo(wait_is_rich_text_available), 'wait_is_target_available': gi.FunctionInfo(wait_is_target_available), 'wait_is_text_available': gi.FunctionInfo(wait_is_text_available), 'wait_is_uris_available': gi.FunctionInfo(wait_is_uris_available)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkClipboard\n\nSignals from GtkClipboard:\n  owner-change (GdkEvent)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkClipboard (3418537760)>'
    __info__ = ObjectInfo(Clipboard)
    __static_attributes__ = ()


