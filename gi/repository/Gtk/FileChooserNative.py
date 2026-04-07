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


from .NativeDialog import NativeDialog

from .FileChooser import FileChooser

class FileChooserNative(NativeDialog, FileChooser):
    """
    :Constructors:
    
    ::
    
        FileChooserNative(**properties)
        new(title:str=None, parent:Gtk.Window=None, action:Gtk.FileChooserAction, accept_label:str=None, cancel_label:str=None) -> Gtk.FileChooserNative
    """
    def add_choice(self, id, label, options=None, option_labels=None): # real signature unknown; restored from __doc__
        """ add_choice(self, id:str, label:str, options:list=None, option_labels:list=None) """
        pass

    def add_filter(self, filter): # real signature unknown; restored from __doc__
        """ add_filter(self, filter:Gtk.FileFilter) """
        pass

    def add_shortcut_folder(self, folder): # real signature unknown; restored from __doc__
        """ add_shortcut_folder(self, folder:str) -> bool """
        return False

    def add_shortcut_folder_uri(self, uri): # real signature unknown; restored from __doc__
        """ add_shortcut_folder_uri(self, uri:str) -> bool """
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

    def destroy(self): # real signature unknown; restored from __doc__
        """ destroy(self) """
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

    def do_hide(self, *args, **kwargs): # real signature unknown
        """ hide(self) """
        pass

    def do_response(self, *args, **kwargs): # real signature unknown
        """ response(self, response_id:int) """
        pass

    def do_show(self, *args, **kwargs): # real signature unknown
        """ show(self) """
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

    def get_accept_label(self): # real signature unknown; restored from __doc__
        """ get_accept_label(self) -> str or None """
        return ""

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> Gtk.FileChooserAction """
        pass

    def get_cancel_label(self): # real signature unknown; restored from __doc__
        """ get_cancel_label(self) -> str or None """
        return ""

    def get_choice(self, id): # real signature unknown; restored from __doc__
        """ get_choice(self, id:str) -> str """
        return ""

    def get_create_folders(self): # real signature unknown; restored from __doc__
        """ get_create_folders(self) -> bool """
        return False

    def get_current_folder(self): # real signature unknown; restored from __doc__
        """ get_current_folder(self) -> str or None """
        return ""

    def get_current_folder_file(self): # real signature unknown; restored from __doc__
        """ get_current_folder_file(self) -> Gio.File or None """
        pass

    def get_current_folder_uri(self): # real signature unknown; restored from __doc__
        """ get_current_folder_uri(self) -> str or None """
        return ""

    def get_current_name(self): # real signature unknown; restored from __doc__
        """ get_current_name(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_do_overwrite_confirmation(self): # real signature unknown; restored from __doc__
        """ get_do_overwrite_confirmation(self) -> bool """
        return False

    def get_extra_widget(self): # real signature unknown; restored from __doc__
        """ get_extra_widget(self) -> Gtk.Widget or None """
        pass

    def get_file(self): # real signature unknown; restored from __doc__
        """ get_file(self) -> Gio.File """
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """ get_filename(self) -> str or None """
        return ""

    def get_filenames(self): # real signature unknown; restored from __doc__
        """ get_filenames(self) -> list """
        return []

    def get_files(self): # real signature unknown; restored from __doc__
        """ get_files(self) -> list """
        return []

    def get_filter(self): # real signature unknown; restored from __doc__
        """ get_filter(self) -> Gtk.FileFilter or None """
        pass

    def get_local_only(self): # real signature unknown; restored from __doc__
        """ get_local_only(self) -> bool """
        return False

    def get_modal(self): # real signature unknown; restored from __doc__
        """ get_modal(self) -> bool """
        return False

    def get_preview_file(self): # real signature unknown; restored from __doc__
        """ get_preview_file(self) -> Gio.File or None """
        pass

    def get_preview_filename(self): # real signature unknown; restored from __doc__
        """ get_preview_filename(self) -> str or None """
        return ""

    def get_preview_uri(self): # real signature unknown; restored from __doc__
        """ get_preview_uri(self) -> str or None """
        return ""

    def get_preview_widget(self): # real signature unknown; restored from __doc__
        """ get_preview_widget(self) -> Gtk.Widget or None """
        pass

    def get_preview_widget_active(self): # real signature unknown; restored from __doc__
        """ get_preview_widget_active(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_select_multiple(self): # real signature unknown; restored from __doc__
        """ get_select_multiple(self) -> bool """
        return False

    def get_show_hidden(self): # real signature unknown; restored from __doc__
        """ get_show_hidden(self) -> bool """
        return False

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str or None """
        return ""

    def get_transient_for(self): # real signature unknown; restored from __doc__
        """ get_transient_for(self) -> Gtk.Window or None """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
        return []

    def get_use_preview_label(self): # real signature unknown; restored from __doc__
        """ get_use_preview_label(self) -> bool """
        return False

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

    def hide(self): # real signature unknown; restored from __doc__
        """ hide(self) """
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

    def list_filters(self): # real signature unknown; restored from __doc__
        """ list_filters(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list """
        return []

    def list_shortcut_folders(self): # real signature unknown; restored from __doc__
        """ list_shortcut_folders(self) -> list or None """
        return []

    def list_shortcut_folder_uris(self): # real signature unknown; restored from __doc__
        """ list_shortcut_folder_uris(self) -> list or None """
        return []

    @classmethod
    def new(cls, title=None, parent=None, action, accept_label=None, cancel_label=None): # real signature unknown; restored from __doc__
        """ new(title:str=None, parent:Gtk.Window=None, action:Gtk.FileChooserAction, accept_label:str=None, cancel_label:str=None) -> Gtk.FileChooserNative """
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

    def remove_choice(self, id): # real signature unknown; restored from __doc__
        """ remove_choice(self, id:str) """
        pass

    def remove_filter(self, filter): # real signature unknown; restored from __doc__
        """ remove_filter(self, filter:Gtk.FileFilter) """
        pass

    def remove_shortcut_folder(self, folder): # real signature unknown; restored from __doc__
        """ remove_shortcut_folder(self, folder:str) -> bool """
        return False

    def remove_shortcut_folder_uri(self, uri): # real signature unknown; restored from __doc__
        """ remove_shortcut_folder_uri(self, uri:str) -> bool """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self): # real signature unknown; restored from __doc__
        """ run(self) -> int """
        return 0

    def run_dispose(self): # real signature unknown; restored from __doc__
        """ run_dispose(self) """
        pass

    def select_all(self): # real signature unknown; restored from __doc__
        """ select_all(self) """
        pass

    def select_file(self, file): # real signature unknown; restored from __doc__
        """ select_file(self, file:Gio.File) -> bool """
        return False

    def select_filename(self, filename): # real signature unknown; restored from __doc__
        """ select_filename(self, filename:str) -> bool """
        return False

    def select_uri(self, uri): # real signature unknown; restored from __doc__
        """ select_uri(self, uri:str) -> bool """
        return False

    def set_accept_label(self, accept_label=None): # real signature unknown; restored from __doc__
        """ set_accept_label(self, accept_label:str=None) """
        pass

    def set_action(self, action): # real signature unknown; restored from __doc__
        """ set_action(self, action:Gtk.FileChooserAction) """
        pass

    def set_cancel_label(self, cancel_label=None): # real signature unknown; restored from __doc__
        """ set_cancel_label(self, cancel_label:str=None) """
        pass

    def set_choice(self, id, option): # real signature unknown; restored from __doc__
        """ set_choice(self, id:str, option:str) """
        pass

    def set_create_folders(self, create_folders): # real signature unknown; restored from __doc__
        """ set_create_folders(self, create_folders:bool) """
        pass

    def set_current_folder(self, filename): # real signature unknown; restored from __doc__
        """ set_current_folder(self, filename:str) -> bool """
        return False

    def set_current_folder_file(self, file): # real signature unknown; restored from __doc__
        """ set_current_folder_file(self, file:Gio.File) -> bool """
        return False

    def set_current_folder_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_current_folder_uri(self, uri:str) -> bool """
        return False

    def set_current_name(self, name): # real signature unknown; restored from __doc__
        """ set_current_name(self, name:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_do_overwrite_confirmation(self, do_overwrite_confirmation): # real signature unknown; restored from __doc__
        """ set_do_overwrite_confirmation(self, do_overwrite_confirmation:bool) """
        pass

    def set_extra_widget(self, extra_widget): # real signature unknown; restored from __doc__
        """ set_extra_widget(self, extra_widget:Gtk.Widget) """
        pass

    def set_file(self, file): # real signature unknown; restored from __doc__
        """ set_file(self, file:Gio.File) -> bool """
        return False

    def set_filename(self, filename): # real signature unknown; restored from __doc__
        """ set_filename(self, filename:str) -> bool """
        return False

    def set_filter(self, filter): # real signature unknown; restored from __doc__
        """ set_filter(self, filter:Gtk.FileFilter) """
        pass

    def set_local_only(self, local_only): # real signature unknown; restored from __doc__
        """ set_local_only(self, local_only:bool) """
        pass

    def set_modal(self, modal): # real signature unknown; restored from __doc__
        """ set_modal(self, modal:bool) """
        pass

    def set_preview_widget(self, preview_widget): # real signature unknown; restored from __doc__
        """ set_preview_widget(self, preview_widget:Gtk.Widget) """
        pass

    def set_preview_widget_active(self, active): # real signature unknown; restored from __doc__
        """ set_preview_widget_active(self, active:bool) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_select_multiple(self, select_multiple): # real signature unknown; restored from __doc__
        """ set_select_multiple(self, select_multiple:bool) """
        pass

    def set_show_hidden(self, show_hidden): # real signature unknown; restored from __doc__
        """ set_show_hidden(self, show_hidden:bool) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
        pass

    def set_transient_for(self, parent=None): # real signature unknown; restored from __doc__
        """ set_transient_for(self, parent:Gtk.Window=None) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) -> bool """
        return False

    def set_use_preview_label(self, use_label): # real signature unknown; restored from __doc__
        """ set_use_preview_label(self, use_label:bool) """
        pass

    def show(self): # real signature unknown; restored from __doc__
        """ show(self) """
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

    def unselect_all(self): # real signature unknown; restored from __doc__
        """ unselect_all(self) """
        pass

    def unselect_file(self, file): # real signature unknown; restored from __doc__
        """ unselect_file(self, file:Gio.File) """
        pass

    def unselect_filename(self, filename): # real signature unknown; restored from __doc__
        """ unselect_filename(self, filename:str) """
        pass

    def unselect_uri(self, uri): # real signature unknown; restored from __doc__
        """ unselect_uri(self, uri:str) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x000002bfd17e45e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(FileChooserNative), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkFileChooserNative (3537640656)>, '__doc__': None, '__gsignals__': {}, 'new': <classmethod(gi.FunctionInfo(new))>, 'get_accept_label': gi.FunctionInfo(get_accept_label), 'get_cancel_label': gi.FunctionInfo(get_cancel_label), 'set_accept_label': gi.FunctionInfo(set_accept_label), 'set_cancel_label': gi.FunctionInfo(set_cancel_label)})"
    __firstlineno__ = 651
    __gdoc__ = 'Object GtkFileChooserNative\n\nProperties from GtkFileChooserNative:\n  accept-label -> gchararray: Accept label\n    The label on the accept button\n  cancel-label -> gchararray: Cancel label\n    The label on the cancel button\n\nSignals from GtkFileChooser:\n  selection-changed ()\n  current-folder-changed ()\n  update-preview ()\n  file-activated ()\n  confirm-overwrite () -> GtkFileChooserConfirmation\n\nSignals from GtkNativeDialog:\n  response (gint)\n\nProperties from GtkNativeDialog:\n  title -> gchararray: Dialog Title\n    The title of the file chooser dialog\n  visible -> gboolean: Visible\n    Whether the dialog is currently visible\n  modal -> gboolean: Modal\n    If TRUE, the dialog is modal (other windows are not usable while this one is up)\n  transient-for -> GtkWindow: Transient for Window\n    The transient parent of the dialog\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkFileChooserNative (3537640656)>'
    __info__ = ObjectInfo(FileChooserNative)
    __static_attributes__ = ()


