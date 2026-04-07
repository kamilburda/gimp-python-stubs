# encoding: utf-8
# module gi.repository.Gio
# by generator 1.147
# no doc

# imports
from gi.repository.GioWin32 import (NetworkMonitorClass, 
    NetworkMonitorPrivate, Win32InputStream, Win32InputStreamClass, 
    Win32InputStreamPrivate, Win32NetworkMonitor, Win32OutputStream, 
    Win32OutputStreamClass, Win32OutputStreamPrivate, 
    registry_settings_backend_new)

from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gi._gi as __gi__gi
import gobject as __gobject


from .Settings import Settings

class Settings(Settings):
    """ Provide dictionary-like access to GLib.Settings. """
    def apply(self): # real signature unknown; restored from __doc__
        """ apply(self) """
        pass

    def bind(self, key, p_object, property, flags): # real signature unknown; restored from __doc__
        """ bind(self, key:str, object:GObject.Object, property:str, flags:Gio.SettingsBindFlags) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def bind_with_mapping(self, key, p_object, property, flags, get_mapping=None, set_mapping=None): # real signature unknown; restored from __doc__
        """ bind_with_mapping(self, key:str, object:GObject.Object, property:str, flags:Gio.SettingsBindFlags, get_mapping:GObject.Closure=None, set_mapping:GObject.Closure=None) """
        pass

    def bind_writable(self, key, p_object, property, inverted): # real signature unknown; restored from __doc__
        """ bind_writable(self, key:str, object:GObject.Object, property:str, inverted:bool) """
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

    def create_action(self, key): # real signature unknown; restored from __doc__
        """ create_action(self, key:str) -> Gio.Action """
        pass

    def delay(self): # real signature unknown; restored from __doc__
        """ delay(self) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self, key:str) """
        pass

    def do_change_event(self, *args, **kwargs): # real signature unknown
        """ change_event(self, keys:int, n_keys:int) -> bool """
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def do_writable_changed(self, *args, **kwargs): # real signature unknown
        """ writable_changed(self, key:str) """
        pass

    def do_writable_change_event(self, *args, **kwargs): # real signature unknown
        """ writable_change_event(self, key:int) -> bool """
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

    def get_boolean(self, key): # real signature unknown; restored from __doc__
        """ get_boolean(self, key:str) -> bool """
        return False

    def get_child(self, name): # real signature unknown; restored from __doc__
        """ get_child(self, name:str) -> Gio.Settings """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default_value(self, key): # real signature unknown; restored from __doc__
        """ get_default_value(self, key:str) -> GLib.Variant or None """
        pass

    def get_double(self, key): # real signature unknown; restored from __doc__
        """ get_double(self, key:str) -> float """
        return 0.0

    def get_enum(self, key): # real signature unknown; restored from __doc__
        """ get_enum(self, key:str) -> int """
        return 0

    def get_flags(self, key): # real signature unknown; restored from __doc__
        """ get_flags(self, key:str) -> int """
        return 0

    def get_has_unapplied(self): # real signature unknown; restored from __doc__
        """ get_has_unapplied(self) -> bool """
        return False

    def get_int(self, key): # real signature unknown; restored from __doc__
        """ get_int(self, key:str) -> int """
        return 0

    def get_int64(self, key): # real signature unknown; restored from __doc__
        """ get_int64(self, key:str) -> int """
        return 0

    def get_mapped(self, key, mapping, user_data=None): # real signature unknown; restored from __doc__
        """ get_mapped(self, key:str, mapping:Gio.SettingsGetMapping, user_data=None) """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_range(self, key): # real signature unknown; restored from __doc__
        """ get_range(self, key:str) -> GLib.Variant """
        pass

    def get_string(self, key): # real signature unknown; restored from __doc__
        """ get_string(self, key:str) -> str """
        return ""

    def get_strv(self, key): # real signature unknown; restored from __doc__
        """ get_strv(self, key:str) -> list """
        return []

    def get_uint(self, key): # real signature unknown; restored from __doc__
        """ get_uint(self, key:str) -> int """
        return 0

    def get_uint64(self, key): # real signature unknown; restored from __doc__
        """ get_uint64(self, key:str) -> int """
        return 0

    def get_user_value(self, key): # real signature unknown; restored from __doc__
        """ get_user_value(self, key:str) -> GLib.Variant or None """
        pass

    def get_value(self, key): # real signature unknown; restored from __doc__
        """ get_value(self, key:str) -> GLib.Variant """
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

    def is_writable(self, name): # real signature unknown; restored from __doc__
        """ is_writable(self, name:str) -> bool """
        return False

    def keys(self): # reliably restored by inspect
        # no doc
        pass

    def list_children(self): # real signature unknown; restored from __doc__
        """ list_children(self) -> list """
        return []

    def list_keys(self): # real signature unknown; restored from __doc__
        """ list_keys(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_relocatable_schemas(self): # real signature unknown; restored from __doc__
        """ list_relocatable_schemas() -> list """
        return []

    def list_schemas(self): # real signature unknown; restored from __doc__
        """ list_schemas() -> list """
        return []

    def new(self, schema_id): # real signature unknown; restored from __doc__
        """ new(schema_id:str) -> Gio.Settings """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_full(self, schema, backend=None, path=None): # real signature unknown; restored from __doc__
        """ new_full(schema:Gio.SettingsSchema, backend:Gio.SettingsBackend=None, path:str=None) -> Gio.Settings """
        pass

    def new_with_backend(self, schema_id, backend): # real signature unknown; restored from __doc__
        """ new_with_backend(schema_id:str, backend:Gio.SettingsBackend) -> Gio.Settings """
        pass

    def new_with_backend_and_path(self, schema_id, backend, path): # real signature unknown; restored from __doc__
        """ new_with_backend_and_path(schema_id:str, backend:Gio.SettingsBackend, path:str) -> Gio.Settings """
        pass

    def new_with_path(self, schema_id, path): # real signature unknown; restored from __doc__
        """ new_with_path(schema_id:str, path:str) -> Gio.Settings """
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

    def range_check(self, key, value): # real signature unknown; restored from __doc__
        """ range_check(self, key:str, value:GLib.Variant) -> bool """
        return False

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

    def reset(self, key): # real signature unknown; restored from __doc__
        """ reset(self, key:str) """
        pass

    def revert(self): # real signature unknown; restored from __doc__
        """ revert(self) """
        pass

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def set_boolean(self, key, value): # real signature unknown; restored from __doc__
        """ set_boolean(self, key:str, value:bool) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_double(self, key, value): # real signature unknown; restored from __doc__
        """ set_double(self, key:str, value:float) -> bool """
        return False

    def set_enum(self, key, value): # real signature unknown; restored from __doc__
        """ set_enum(self, key:str, value:int) -> bool """
        return False

    def set_flags(self, key, value): # real signature unknown; restored from __doc__
        """ set_flags(self, key:str, value:int) -> bool """
        return False

    def set_int(self, key, value): # real signature unknown; restored from __doc__
        """ set_int(self, key:str, value:int) -> bool """
        return False

    def set_int64(self, key, value): # real signature unknown; restored from __doc__
        """ set_int64(self, key:str, value:int) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_string(self, key, value): # real signature unknown; restored from __doc__
        """ set_string(self, key:str, value:str) -> bool """
        return False

    def set_strv(self, key, value=None): # real signature unknown; restored from __doc__
        """ set_strv(self, key:str, value:list=None) -> bool """
        return False

    def set_uint(self, key, value): # real signature unknown; restored from __doc__
        """ set_uint(self, key:str, value:int) -> bool """
        return False

    def set_uint64(self, key, value): # real signature unknown; restored from __doc__
        """ set_uint64(self, key:str, value:int) -> bool """
        return False

    def set_value(self, key, value): # real signature unknown; restored from __doc__
        """ set_value(self, key:str, value:GLib.Variant) -> bool """
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

    def sync(self): # real signature unknown; restored from __doc__
        """ sync() """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unbind(self, p_object, property): # real signature unknown; restored from __doc__
        """ unbind(object:GObject.Object, property:str) """
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

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __contains__(self, key): # reliably restored by inspect
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

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
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

    def __setitem__(self, key, value): # reliably restored by inspect
        # no doc
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea70862a40>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gio', '__doc__': 'Provide dictionary-like access to GLib.Settings.', '__init__': <function deprecated_init.<locals>.new_init at 0x000001ea7028a020>, '__contains__': <function Settings.__contains__ at 0x000001ea703080e0>, '__len__': <function Settings.__len__ at 0x000001ea70308180>, '__iter__': <function Settings.__iter__ at 0x000001ea70308220>, '__bool__': <function Settings.__bool__ at 0x000001ea703082c0>, '__getitem__': <function Settings.__getitem__ at 0x000001ea70308360>, '__setitem__': <function Settings.__setitem__ at 0x000001ea70308400>, 'keys': <function Settings.keys at 0x000001ea703084a0>, '__gsignals__': {}})"
    __gdoc__ = 'Object GSettings\n\nProvide dictionary-like access to GLib.Settings.\n\nSignals from GSettings:\n  changed (gchararray)\n  change-event (gpointer, gint) -> gboolean\n  writable-changed (gchararray)\n  writable-change-event (guint) -> gboolean\n\nProperties from GSettings:\n  settings-schema -> GSettingsSchema: settings-schema\n  schema -> gchararray: schema\n  schema-id -> gchararray: schema-id\n  backend -> GSettingsBackend: backend\n  path -> gchararray: path\n  has-unapplied -> gboolean: has-unapplied\n  delay-apply -> gboolean: delay-apply\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GSettings (1845788704)>'
    __info__ = ObjectInfo(Settings)


