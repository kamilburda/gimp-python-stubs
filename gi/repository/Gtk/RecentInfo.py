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


from .RecentInfo import RecentInfo

class RecentInfo(RecentInfo):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def create_app_info(self, app_name=None): # real signature unknown; restored from __doc__
        """ create_app_info(self, app_name:str=None) -> Gio.AppInfo or None """
        pass

    def exists(self): # real signature unknown; restored from __doc__
        """ exists(self) -> bool """
        return False

    def get_added(self): # real signature unknown; restored from __doc__
        """ get_added(self) -> int """
        return 0

    def get_age(self): # real signature unknown; restored from __doc__
        """ get_age(self) -> int """
        return 0

    def get_applications(self): # real signature unknown; restored from __doc__
        """ get_applications(self) -> list """
        return []

    def get_application_info(*args, **kwargs): # reliably restored by inspect
        """ get_application_info(self, app_name:str) -> bool, app_exec:str, count:int, time_:int """
        pass

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str """
        return ""

    def get_display_name(self): # real signature unknown; restored from __doc__
        """ get_display_name(self) -> str """
        return ""

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon or None """
        pass

    def get_groups(self): # real signature unknown; restored from __doc__
        """ get_groups(self) -> list """
        return []

    def get_icon(self, size): # real signature unknown; restored from __doc__
        """ get_icon(self, size:int) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_mime_type(self): # real signature unknown; restored from __doc__
        """ get_mime_type(self) -> str """
        return ""

    def get_modified(self): # real signature unknown; restored from __doc__
        """ get_modified(self) -> int """
        return 0

    def get_private_hint(self): # real signature unknown; restored from __doc__
        """ get_private_hint(self) -> bool """
        return False

    def get_short_name(self): # real signature unknown; restored from __doc__
        """ get_short_name(self) -> str """
        return ""

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_uri_display(self): # real signature unknown; restored from __doc__
        """ get_uri_display(self) -> str or None """
        return ""

    def get_visited(self): # real signature unknown; restored from __doc__
        """ get_visited(self) -> int """
        return 0

    def has_application(self, app_name): # real signature unknown; restored from __doc__
        """ has_application(self, app_name:str) -> bool """
        return False

    def has_group(self, group_name): # real signature unknown; restored from __doc__
        """ has_group(self, group_name:str) -> bool """
        return False

    def is_local(self): # real signature unknown; restored from __doc__
        """ is_local(self) -> bool """
        return False

    def last_application(self): # real signature unknown; restored from __doc__
        """ last_application(self) -> str """
        return ""

    def match(self, info_b): # real signature unknown; restored from __doc__
        """ match(self, info_b:Gtk.RecentInfo) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.RecentInfo """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 796, 'get_application_info': <function strip_boolean_result.<locals>.wrapped at 0x000002bfce4d7cc0>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 796
    __gtype__ = None # (!) real value is '<GType GtkRecentInfo (3416386704)>'
    __info__ = StructInfo(RecentInfo)
    __static_attributes__ = ()


