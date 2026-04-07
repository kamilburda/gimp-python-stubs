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


class FileInfo(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        FileInfo(**properties)
        new() -> Gio.FileInfo
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_status(self): # real signature unknown; restored from __doc__
        """ clear_status(self) """
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

    def copy_into(self, dest_info): # real signature unknown; restored from __doc__
        """ copy_into(self, dest_info:Gio.FileInfo) """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_dispose(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.FileInfo """
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

    def get_access_date_time(self): # real signature unknown; restored from __doc__
        """ get_access_date_time(self) -> GLib.DateTime or None """
        pass

    def get_attribute_as_string(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_as_string(self, attribute:str) -> str or None """
        return ""

    def get_attribute_boolean(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_boolean(self, attribute:str) -> bool """
        return False

    def get_attribute_byte_string(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_byte_string(self, attribute:str) -> str or None """
        return ""

    def get_attribute_data(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_data(self, attribute:str) -> bool, type:Gio.FileAttributeType, value_pp, status:Gio.FileAttributeStatus """
        return False

    def get_attribute_file_path(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_file_path(self, attribute:str) -> str or None """
        return ""

    def get_attribute_int32(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_int32(self, attribute:str) -> int """
        return 0

    def get_attribute_int64(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_int64(self, attribute:str) -> int """
        return 0

    def get_attribute_object(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_object(self, attribute:str) -> GObject.Object or None """
        pass

    def get_attribute_status(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_status(self, attribute:str) -> Gio.FileAttributeStatus """
        pass

    def get_attribute_string(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_string(self, attribute:str) -> str or None """
        return ""

    def get_attribute_stringv(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_stringv(self, attribute:str) -> list or None """
        return []

    def get_attribute_type(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_type(self, attribute:str) -> Gio.FileAttributeType """
        pass

    def get_attribute_uint32(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_uint32(self, attribute:str) -> int """
        return 0

    def get_attribute_uint64(self, attribute): # real signature unknown; restored from __doc__
        """ get_attribute_uint64(self, attribute:str) -> int """
        return 0

    def get_content_type(self): # real signature unknown; restored from __doc__
        """ get_content_type(self) -> str or None """
        return ""

    def get_creation_date_time(self): # real signature unknown; restored from __doc__
        """ get_creation_date_time(self) -> GLib.DateTime or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_deletion_date(self): # real signature unknown; restored from __doc__
        """ get_deletion_date(self) -> GLib.DateTime or None """
        pass

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_edit_name(self): # real signature unknown; restored from __doc__
        """ get_edit_name(self) -> str """
        return ""

    def get_etag(self): # real signature unknown; restored from __doc__
        """ get_etag(self) -> str or None """
        return ""

    def get_file_type(self): # real signature unknown; restored from __doc__
        """ get_file_type(self) -> Gio.FileType """
        pass

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon or None """
        pass

    def get_is_backup(self): # real signature unknown; restored from __doc__
        """ get_is_backup(self) -> bool """
        return False

    def get_is_hidden(self): # real signature unknown; restored from __doc__
        """ get_is_hidden(self) -> bool """
        return False

    def get_is_symlink(self): # real signature unknown; restored from __doc__
        """ get_is_symlink(self) -> bool """
        return False

    def get_modification_date_time(self): # real signature unknown; restored from __doc__
        """ get_modification_date_time(self) -> GLib.DateTime or None """
        pass

    def get_modification_time(self): # real signature unknown; restored from __doc__
        """ get_modification_time(self) -> result:GLib.TimeVal """
        pass

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

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_sort_order(self): # real signature unknown; restored from __doc__
        """ get_sort_order(self) -> int """
        return 0

    def get_symbolic_icon(self): # real signature unknown; restored from __doc__
        """ get_symbolic_icon(self) -> Gio.Icon or None """
        pass

    def get_symlink_target(self): # real signature unknown; restored from __doc__
        """ get_symlink_target(self) -> str or None """
        return ""

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

    def has_attribute(self, attribute): # real signature unknown; restored from __doc__
        """ has_attribute(self, attribute:str) -> bool """
        return False

    def has_namespace(self, name_space): # real signature unknown; restored from __doc__
        """ has_namespace(self, name_space:str) -> bool """
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

    def list_attributes(self, name_space=None): # real signature unknown; restored from __doc__
        """ list_attributes(self, name_space:str=None) -> list or None """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gio.FileInfo """
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

    def remove_attribute(self, attribute): # real signature unknown; restored from __doc__
        """ remove_attribute(self, attribute:str) """
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

    def set_access_date_time(self, atime): # real signature unknown; restored from __doc__
        """ set_access_date_time(self, atime:GLib.DateTime) """
        pass

    def set_attribute(self, attribute, type, value_p): # real signature unknown; restored from __doc__
        """ set_attribute(self, attribute:str, type:Gio.FileAttributeType, value_p) """
        pass

    def set_attribute_boolean(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_boolean(self, attribute:str, attr_value:bool) """
        pass

    def set_attribute_byte_string(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_byte_string(self, attribute:str, attr_value:str) """
        pass

    def set_attribute_file_path(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_file_path(self, attribute:str, attr_value:str) """
        pass

    def set_attribute_int32(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_int32(self, attribute:str, attr_value:int) """
        pass

    def set_attribute_int64(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_int64(self, attribute:str, attr_value:int) """
        pass

    def set_attribute_mask(self, mask): # real signature unknown; restored from __doc__
        """ set_attribute_mask(self, mask:Gio.FileAttributeMatcher) """
        pass

    def set_attribute_object(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_object(self, attribute:str, attr_value:GObject.Object) """
        pass

    def set_attribute_status(self, attribute, status): # real signature unknown; restored from __doc__
        """ set_attribute_status(self, attribute:str, status:Gio.FileAttributeStatus) -> bool """
        return False

    def set_attribute_string(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_string(self, attribute:str, attr_value:str) """
        pass

    def set_attribute_stringv(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_stringv(self, attribute:str, attr_value:list) """
        pass

    def set_attribute_uint32(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_uint32(self, attribute:str, attr_value:int) """
        pass

    def set_attribute_uint64(self, attribute, attr_value): # real signature unknown; restored from __doc__
        """ set_attribute_uint64(self, attribute:str, attr_value:int) """
        pass

    def set_content_type(self, content_type): # real signature unknown; restored from __doc__
        """ set_content_type(self, content_type:str) """
        pass

    def set_creation_date_time(self, creation_time): # real signature unknown; restored from __doc__
        """ set_creation_date_time(self, creation_time:GLib.DateTime) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str) """
        pass

    def set_edit_name(self, edit_name): # real signature unknown; restored from __doc__
        """ set_edit_name(self, edit_name:str) """
        pass

    def set_file_type(self, type): # real signature unknown; restored from __doc__
        """ set_file_type(self, type:Gio.FileType) """
        pass

    def set_icon(self, icon): # real signature unknown; restored from __doc__
        """ set_icon(self, icon:Gio.Icon) """
        pass

    def set_is_hidden(self, is_hidden): # real signature unknown; restored from __doc__
        """ set_is_hidden(self, is_hidden:bool) """
        pass

    def set_is_symlink(self, is_symlink): # real signature unknown; restored from __doc__
        """ set_is_symlink(self, is_symlink:bool) """
        pass

    def set_modification_date_time(self, mtime): # real signature unknown; restored from __doc__
        """ set_modification_date_time(self, mtime:GLib.DateTime) """
        pass

    def set_modification_time(self, mtime): # real signature unknown; restored from __doc__
        """ set_modification_time(self, mtime:GLib.TimeVal) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_sort_order(self, sort_order): # real signature unknown; restored from __doc__
        """ set_sort_order(self, sort_order:int) """
        pass

    def set_symbolic_icon(self, icon): # real signature unknown; restored from __doc__
        """ set_symbolic_icon(self, icon:Gio.Icon) """
        pass

    def set_symlink_target(self, symlink_target): # real signature unknown; restored from __doc__
        """ set_symlink_target(self, symlink_target:str) """
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

    def unset_attribute_mask(self): # real signature unknown; restored from __doc__
        """ unset_attribute_mask(self) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x000001ea70857fd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FileInfo), '__module__': 'gi.repository.Gio', '__gtype__': <GType GFileInfo (1848620816)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'clear_status': gi.FunctionInfo(clear_status), 'copy_into': gi.FunctionInfo(copy_into), 'dup': gi.FunctionInfo(dup), 'get_access_date_time': gi.FunctionInfo(get_access_date_time), 'get_attribute_as_string': gi.FunctionInfo(get_attribute_as_string), 'get_attribute_boolean': gi.FunctionInfo(get_attribute_boolean), 'get_attribute_byte_string': gi.FunctionInfo(get_attribute_byte_string), 'get_attribute_data': gi.FunctionInfo(get_attribute_data), 'get_attribute_file_path': gi.FunctionInfo(get_attribute_file_path), 'get_attribute_int32': gi.FunctionInfo(get_attribute_int32), 'get_attribute_int64': gi.FunctionInfo(get_attribute_int64), 'get_attribute_object': gi.FunctionInfo(get_attribute_object), 'get_attribute_status': gi.FunctionInfo(get_attribute_status), 'get_attribute_string': gi.FunctionInfo(get_attribute_string), 'get_attribute_stringv': gi.FunctionInfo(get_attribute_stringv), 'get_attribute_type': gi.FunctionInfo(get_attribute_type), 'get_attribute_uint32': gi.FunctionInfo(get_attribute_uint32), 'get_attribute_uint64': gi.FunctionInfo(get_attribute_uint64), 'get_content_type': gi.FunctionInfo(get_content_type), 'get_creation_date_time': gi.FunctionInfo(get_creation_date_time), 'get_deletion_date': gi.FunctionInfo(get_deletion_date), 'get_display_name': gi.FunctionInfo(get_display_name), 'get_edit_name': gi.FunctionInfo(get_edit_name), 'get_etag': gi.FunctionInfo(get_etag), 'get_file_type': gi.FunctionInfo(get_file_type), 'get_icon': gi.FunctionInfo(get_icon), 'get_is_backup': gi.FunctionInfo(get_is_backup), 'get_is_hidden': gi.FunctionInfo(get_is_hidden), 'get_is_symlink': gi.FunctionInfo(get_is_symlink), 'get_modification_date_time': gi.FunctionInfo(get_modification_date_time), 'get_modification_time': gi.FunctionInfo(get_modification_time), 'get_name': gi.FunctionInfo(get_name), 'get_size': gi.FunctionInfo(get_size), 'get_sort_order': gi.FunctionInfo(get_sort_order), 'get_symbolic_icon': gi.FunctionInfo(get_symbolic_icon), 'get_symlink_target': gi.FunctionInfo(get_symlink_target), 'has_attribute': gi.FunctionInfo(has_attribute), 'has_namespace': gi.FunctionInfo(has_namespace), 'list_attributes': gi.FunctionInfo(list_attributes), 'remove_attribute': gi.FunctionInfo(remove_attribute), 'set_access_date_time': gi.FunctionInfo(set_access_date_time), 'set_attribute': gi.FunctionInfo(set_attribute), 'set_attribute_boolean': gi.FunctionInfo(set_attribute_boolean), 'set_attribute_byte_string': gi.FunctionInfo(set_attribute_byte_string), 'set_attribute_file_path': gi.FunctionInfo(set_attribute_file_path), 'set_attribute_int32': gi.FunctionInfo(set_attribute_int32), 'set_attribute_int64': gi.FunctionInfo(set_attribute_int64), 'set_attribute_mask': gi.FunctionInfo(set_attribute_mask), 'set_attribute_object': gi.FunctionInfo(set_attribute_object), 'set_attribute_status': gi.FunctionInfo(set_attribute_status), 'set_attribute_string': gi.FunctionInfo(set_attribute_string), 'set_attribute_stringv': gi.FunctionInfo(set_attribute_stringv), 'set_attribute_uint32': gi.FunctionInfo(set_attribute_uint32), 'set_attribute_uint64': gi.FunctionInfo(set_attribute_uint64), 'set_content_type': gi.FunctionInfo(set_content_type), 'set_creation_date_time': gi.FunctionInfo(set_creation_date_time), 'set_display_name': gi.FunctionInfo(set_display_name), 'set_edit_name': gi.FunctionInfo(set_edit_name), 'set_file_type': gi.FunctionInfo(set_file_type), 'set_icon': gi.FunctionInfo(set_icon), 'set_is_hidden': gi.FunctionInfo(set_is_hidden), 'set_is_symlink': gi.FunctionInfo(set_is_symlink), 'set_modification_date_time': gi.FunctionInfo(set_modification_date_time), 'set_modification_time': gi.FunctionInfo(set_modification_time), 'set_name': gi.FunctionInfo(set_name), 'set_size': gi.FunctionInfo(set_size), 'set_sort_order': gi.FunctionInfo(set_sort_order), 'set_symbolic_icon': gi.FunctionInfo(set_symbolic_icon), 'set_symlink_target': gi.FunctionInfo(set_symlink_target), 'unset_attribute_mask': gi.FunctionInfo(unset_attribute_mask)})"
    __gdoc__ = 'Object GFileInfo\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GFileInfo (1848620816)>'
    __info__ = ObjectInfo(FileInfo)


