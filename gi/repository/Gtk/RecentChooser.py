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


class RecentChooser(__gobject.GInterface):
    # no doc
    def add_filter(self, filter): # real signature unknown; restored from __doc__
        """ add_filter(self, filter:Gtk.RecentFilter) """
        pass

    def get_current_item(self): # real signature unknown; restored from __doc__
        """ get_current_item(self) -> Gtk.RecentInfo """
        pass

    def get_current_uri(self): # real signature unknown; restored from __doc__
        """ get_current_uri(self) -> str """
        return ""

    def get_filter(self): # real signature unknown; restored from __doc__
        """ get_filter(self) -> Gtk.RecentFilter """
        pass

    def get_items(self): # real signature unknown; restored from __doc__
        """ get_items(self) -> list """
        return []

    def get_limit(self): # real signature unknown; restored from __doc__
        """ get_limit(self) -> int """
        return 0

    def get_local_only(self): # real signature unknown; restored from __doc__
        """ get_local_only(self) -> bool """
        return False

    def get_select_multiple(self): # real signature unknown; restored from __doc__
        """ get_select_multiple(self) -> bool """
        return False

    def get_show_icons(self): # real signature unknown; restored from __doc__
        """ get_show_icons(self) -> bool """
        return False

    def get_show_not_found(self): # real signature unknown; restored from __doc__
        """ get_show_not_found(self) -> bool """
        return False

    def get_show_private(self): # real signature unknown; restored from __doc__
        """ get_show_private(self) -> bool """
        return False

    def get_show_tips(self): # real signature unknown; restored from __doc__
        """ get_show_tips(self) -> bool """
        return False

    def get_sort_type(self): # real signature unknown; restored from __doc__
        """ get_sort_type(self) -> Gtk.RecentSortType """
        pass

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
        return []

    def list_filters(self): # real signature unknown; restored from __doc__
        """ list_filters(self) -> list """
        return []

    def remove_filter(self, filter): # real signature unknown; restored from __doc__
        """ remove_filter(self, filter:Gtk.RecentFilter) """
        pass

    def select_all(self): # real signature unknown; restored from __doc__
        """ select_all(self) """
        pass

    def select_uri(self, uri): # real signature unknown; restored from __doc__
        """ select_uri(self, uri:str) -> bool """
        return False

    def set_current_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_current_uri(self, uri:str) -> bool """
        return False

    def set_filter(self, filter=None): # real signature unknown; restored from __doc__
        """ set_filter(self, filter:Gtk.RecentFilter=None) """
        pass

    def set_limit(self, limit): # real signature unknown; restored from __doc__
        """ set_limit(self, limit:int) """
        pass

    def set_local_only(self, local_only): # real signature unknown; restored from __doc__
        """ set_local_only(self, local_only:bool) """
        pass

    def set_select_multiple(self, select_multiple): # real signature unknown; restored from __doc__
        """ set_select_multiple(self, select_multiple:bool) """
        pass

    def set_show_icons(self, show_icons): # real signature unknown; restored from __doc__
        """ set_show_icons(self, show_icons:bool) """
        pass

    def set_show_not_found(self, show_not_found): # real signature unknown; restored from __doc__
        """ set_show_not_found(self, show_not_found:bool) """
        pass

    def set_show_private(self, show_private): # real signature unknown; restored from __doc__
        """ set_show_private(self, show_private:bool) """
        pass

    def set_show_tips(self, show_tips): # real signature unknown; restored from __doc__
        """ set_show_tips(self, show_tips:bool) """
        pass

    def set_sort_func(self, sort_func, sort_data=None): # real signature unknown; restored from __doc__
        """ set_sort_func(self, sort_func:Gtk.RecentSortFunc, sort_data=None) """
        pass

    def set_sort_type(self, sort_type): # real signature unknown; restored from __doc__
        """ set_sort_type(self, sort_type:Gtk.RecentSortType) """
        pass

    def unselect_all(self): # real signature unknown; restored from __doc__
        """ unselect_all(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(RecentChooser), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkRecentChooser (3416388336)>, '__dict__': <attribute '__dict__' of 'RecentChooser' objects>, '__weakref__': <attribute '__weakref__' of 'RecentChooser' objects>, '__doc__': None, '__gsignals__': {}, 'add_filter': gi.FunctionInfo(add_filter), 'get_current_item': gi.FunctionInfo(get_current_item), 'get_current_uri': gi.FunctionInfo(get_current_uri), 'get_filter': gi.FunctionInfo(get_filter), 'get_items': gi.FunctionInfo(get_items), 'get_limit': gi.FunctionInfo(get_limit), 'get_local_only': gi.FunctionInfo(get_local_only), 'get_select_multiple': gi.FunctionInfo(get_select_multiple), 'get_show_icons': gi.FunctionInfo(get_show_icons), 'get_show_not_found': gi.FunctionInfo(get_show_not_found), 'get_show_private': gi.FunctionInfo(get_show_private), 'get_show_tips': gi.FunctionInfo(get_show_tips), 'get_sort_type': gi.FunctionInfo(get_sort_type), 'get_uris': gi.FunctionInfo(get_uris), 'list_filters': gi.FunctionInfo(list_filters), 'remove_filter': gi.FunctionInfo(remove_filter), 'select_all': gi.FunctionInfo(select_all), 'select_uri': gi.FunctionInfo(select_uri), 'set_current_uri': gi.FunctionInfo(set_current_uri), 'set_filter': gi.FunctionInfo(set_filter), 'set_limit': gi.FunctionInfo(set_limit), 'set_local_only': gi.FunctionInfo(set_local_only), 'set_select_multiple': gi.FunctionInfo(set_select_multiple), 'set_show_icons': gi.FunctionInfo(set_show_icons), 'set_show_not_found': gi.FunctionInfo(set_show_not_found), 'set_show_private': gi.FunctionInfo(set_show_private), 'set_show_tips': gi.FunctionInfo(set_show_tips), 'set_sort_func': gi.FunctionInfo(set_sort_func), 'set_sort_type': gi.FunctionInfo(set_sort_type), 'unselect_all': gi.FunctionInfo(unselect_all), 'unselect_uri': gi.FunctionInfo(unselect_uri)})"
    __gdoc__ = 'Interface GtkRecentChooser\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkRecentChooser (3416388336)>'
    __info__ = InterfaceInfo(RecentChooser)


