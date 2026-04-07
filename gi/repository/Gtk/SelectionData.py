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


class SelectionData(__gi.Boxed):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.SelectionData """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_data(self): # real signature unknown; restored from __doc__
        """ get_data(self) -> list """
        return []

    def get_data_type(self): # real signature unknown; restored from __doc__
        """ get_data_type(self) -> Gdk.Atom """
        pass

    def get_display(self): # real signature unknown; restored from __doc__
        """ get_display(self) -> Gdk.Display """
        pass

    def get_format(self): # real signature unknown; restored from __doc__
        """ get_format(self) -> int """
        return 0

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_pixbuf(self): # real signature unknown; restored from __doc__
        """ get_pixbuf(self) -> GdkPixbuf.Pixbuf or None """
        pass

    def get_selection(self): # real signature unknown; restored from __doc__
        """ get_selection(self) -> Gdk.Atom """
        pass

    def get_target(self): # real signature unknown; restored from __doc__
        """ get_target(self) -> Gdk.Atom """
        pass

    def get_targets(self): # real signature unknown; restored from __doc__
        """ get_targets(self) -> bool, targets:list """
        return False

    def get_text(self): # real signature unknown; restored from __doc__
        """ get_text(self) -> str or None """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list """
        return []

    def set(self, type, format, data): # real signature unknown; restored from __doc__
        """ set(self, type:Gdk.Atom, format:int, data:list) """
        pass

    def set_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ set_pixbuf(self, pixbuf:GdkPixbuf.Pixbuf) -> bool """
        return False

    def set_text(self, p_str, len): # real signature unknown; restored from __doc__
        """ set_text(self, str:str, len:int) -> bool """
        return False

    def set_uris(self, uris): # real signature unknown; restored from __doc__
        """ set_uris(self, uris:list) -> bool """
        return False

    def targets_include_image(self, writable): # real signature unknown; restored from __doc__
        """ targets_include_image(self, writable:bool) -> bool """
        return False

    def targets_include_rich_text(self, buffer): # real signature unknown; restored from __doc__
        """ targets_include_rich_text(self, buffer:Gtk.TextBuffer) -> bool """
        return False

    def targets_include_text(self): # real signature unknown; restored from __doc__
        """ targets_include_text(self) -> bool """
        return False

    def targets_include_uri(self): # real signature unknown; restored from __doc__
        """ targets_include_uri(self) -> bool """
        return False

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SelectionData), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkSelectionData (3418527968)>, '__dict__': <attribute '__dict__' of 'SelectionData' objects>, '__weakref__': <attribute '__weakref__' of 'SelectionData' objects>, '__doc__': None, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_data_type': gi.FunctionInfo(get_data_type), 'get_data': gi.FunctionInfo(get_data), 'get_display': gi.FunctionInfo(get_display), 'get_format': gi.FunctionInfo(get_format), 'get_length': gi.FunctionInfo(get_length), 'get_pixbuf': gi.FunctionInfo(get_pixbuf), 'get_selection': gi.FunctionInfo(get_selection), 'get_target': gi.FunctionInfo(get_target), 'get_targets': gi.FunctionInfo(get_targets), 'get_text': gi.FunctionInfo(get_text), 'get_uris': gi.FunctionInfo(get_uris), 'set': gi.FunctionInfo(set), 'set_pixbuf': gi.FunctionInfo(set_pixbuf), 'set_text': gi.FunctionInfo(set_text), 'set_uris': gi.FunctionInfo(set_uris), 'targets_include_image': gi.FunctionInfo(targets_include_image), 'targets_include_rich_text': gi.FunctionInfo(targets_include_rich_text), 'targets_include_text': gi.FunctionInfo(targets_include_text), 'targets_include_uri': gi.FunctionInfo(targets_include_uri)})"
    __gtype__ = None # (!) real value is '<GType GtkSelectionData (3418527968)>'
    __info__ = StructInfo(SelectionData)


