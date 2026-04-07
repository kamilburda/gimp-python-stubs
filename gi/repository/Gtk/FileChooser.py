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


class FileChooser(__gobject.GInterface):
    # no doc
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

    def get_action(self): # real signature unknown; restored from __doc__
        """ get_action(self) -> Gtk.FileChooserAction """
        pass

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

    def get_select_multiple(self): # real signature unknown; restored from __doc__
        """ get_select_multiple(self) -> bool """
        return False

    def get_show_hidden(self): # real signature unknown; restored from __doc__
        """ get_show_hidden(self) -> bool """
        return False

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str or None """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
        return []

    def get_use_preview_label(self): # real signature unknown; restored from __doc__
        """ get_use_preview_label(self) -> bool """
        return False

    def list_filters(self): # real signature unknown; restored from __doc__
        """ list_filters(self) -> list """
        return []

    def list_shortcut_folders(self): # real signature unknown; restored from __doc__
        """ list_shortcut_folders(self) -> list or None """
        return []

    def list_shortcut_folder_uris(self): # real signature unknown; restored from __doc__
        """ list_shortcut_folder_uris(self) -> list or None """
        return []

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

    def set_action(self, action): # real signature unknown; restored from __doc__
        """ set_action(self, action:Gtk.FileChooserAction) """
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

    def set_preview_widget(self, preview_widget): # real signature unknown; restored from __doc__
        """ set_preview_widget(self, preview_widget:Gtk.Widget) """
        pass

    def set_preview_widget_active(self, active): # real signature unknown; restored from __doc__
        """ set_preview_widget_active(self, active:bool) """
        pass

    def set_select_multiple(self, select_multiple): # real signature unknown; restored from __doc__
        """ set_select_multiple(self, select_multiple:bool) """
        pass

    def set_show_hidden(self, show_hidden): # real signature unknown; restored from __doc__
        """ set_show_hidden(self, show_hidden:bool) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) -> bool """
        return False

    def set_use_preview_label(self, use_label): # real signature unknown; restored from __doc__
        """ set_use_preview_label(self, use_label:bool) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(FileChooser), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkFileChooser (3416383152)>, '__dict__': <attribute '__dict__' of 'FileChooser' objects>, '__weakref__': <attribute '__weakref__' of 'FileChooser' objects>, '__doc__': None, '__gsignals__': {}, 'add_choice': gi.FunctionInfo(add_choice), 'add_filter': gi.FunctionInfo(add_filter), 'add_shortcut_folder': gi.FunctionInfo(add_shortcut_folder), 'add_shortcut_folder_uri': gi.FunctionInfo(add_shortcut_folder_uri), 'get_action': gi.FunctionInfo(get_action), 'get_choice': gi.FunctionInfo(get_choice), 'get_create_folders': gi.FunctionInfo(get_create_folders), 'get_current_folder': gi.FunctionInfo(get_current_folder), 'get_current_folder_file': gi.FunctionInfo(get_current_folder_file), 'get_current_folder_uri': gi.FunctionInfo(get_current_folder_uri), 'get_current_name': gi.FunctionInfo(get_current_name), 'get_do_overwrite_confirmation': gi.FunctionInfo(get_do_overwrite_confirmation), 'get_extra_widget': gi.FunctionInfo(get_extra_widget), 'get_file': gi.FunctionInfo(get_file), 'get_filename': gi.FunctionInfo(get_filename), 'get_filenames': gi.FunctionInfo(get_filenames), 'get_files': gi.FunctionInfo(get_files), 'get_filter': gi.FunctionInfo(get_filter), 'get_local_only': gi.FunctionInfo(get_local_only), 'get_preview_file': gi.FunctionInfo(get_preview_file), 'get_preview_filename': gi.FunctionInfo(get_preview_filename), 'get_preview_uri': gi.FunctionInfo(get_preview_uri), 'get_preview_widget': gi.FunctionInfo(get_preview_widget), 'get_preview_widget_active': gi.FunctionInfo(get_preview_widget_active), 'get_select_multiple': gi.FunctionInfo(get_select_multiple), 'get_show_hidden': gi.FunctionInfo(get_show_hidden), 'get_uri': gi.FunctionInfo(get_uri), 'get_uris': gi.FunctionInfo(get_uris), 'get_use_preview_label': gi.FunctionInfo(get_use_preview_label), 'list_filters': gi.FunctionInfo(list_filters), 'list_shortcut_folder_uris': gi.FunctionInfo(list_shortcut_folder_uris), 'list_shortcut_folders': gi.FunctionInfo(list_shortcut_folders), 'remove_choice': gi.FunctionInfo(remove_choice), 'remove_filter': gi.FunctionInfo(remove_filter), 'remove_shortcut_folder': gi.FunctionInfo(remove_shortcut_folder), 'remove_shortcut_folder_uri': gi.FunctionInfo(remove_shortcut_folder_uri), 'select_all': gi.FunctionInfo(select_all), 'select_file': gi.FunctionInfo(select_file), 'select_filename': gi.FunctionInfo(select_filename), 'select_uri': gi.FunctionInfo(select_uri), 'set_action': gi.FunctionInfo(set_action), 'set_choice': gi.FunctionInfo(set_choice), 'set_create_folders': gi.FunctionInfo(set_create_folders), 'set_current_folder': gi.FunctionInfo(set_current_folder), 'set_current_folder_file': gi.FunctionInfo(set_current_folder_file), 'set_current_folder_uri': gi.FunctionInfo(set_current_folder_uri), 'set_current_name': gi.FunctionInfo(set_current_name), 'set_do_overwrite_confirmation': gi.FunctionInfo(set_do_overwrite_confirmation), 'set_extra_widget': gi.FunctionInfo(set_extra_widget), 'set_file': gi.FunctionInfo(set_file), 'set_filename': gi.FunctionInfo(set_filename), 'set_filter': gi.FunctionInfo(set_filter), 'set_local_only': gi.FunctionInfo(set_local_only), 'set_preview_widget': gi.FunctionInfo(set_preview_widget), 'set_preview_widget_active': gi.FunctionInfo(set_preview_widget_active), 'set_select_multiple': gi.FunctionInfo(set_select_multiple), 'set_show_hidden': gi.FunctionInfo(set_show_hidden), 'set_uri': gi.FunctionInfo(set_uri), 'set_use_preview_label': gi.FunctionInfo(set_use_preview_label), 'unselect_all': gi.FunctionInfo(unselect_all), 'unselect_file': gi.FunctionInfo(unselect_file), 'unselect_filename': gi.FunctionInfo(unselect_filename), 'unselect_uri': gi.FunctionInfo(unselect_uri)})"
    __gdoc__ = 'Interface GtkFileChooser\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkFileChooser (3416383152)>'
    __info__ = InterfaceInfo(FileChooser)


