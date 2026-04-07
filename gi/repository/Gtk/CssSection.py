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


class CssSection(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_end_line(self): # real signature unknown; restored from __doc__
        """ get_end_line(self) -> int """
        return 0

    def get_end_position(self): # real signature unknown; restored from __doc__
        """ get_end_position(self) -> int """
        return 0

    def get_file(self): # real signature unknown; restored from __doc__
        """ get_file(self) -> Gio.File """
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gtk.CssSection or None """
        pass

    def get_section_type(self): # real signature unknown; restored from __doc__
        """ get_section_type(self) -> Gtk.CssSectionType """
        pass

    def get_start_line(self): # real signature unknown; restored from __doc__
        """ get_start_line(self) -> int """
        return 0

    def get_start_position(self): # real signature unknown; restored from __doc__
        """ get_start_position(self) -> int """
        return 0

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.CssSection """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CssSection), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkCssSection (3537891824)>, '__dict__': <attribute '__dict__' of 'CssSection' objects>, '__weakref__': <attribute '__weakref__' of 'CssSection' objects>, '__doc__': None, 'get_end_line': gi.FunctionInfo(get_end_line), 'get_end_position': gi.FunctionInfo(get_end_position), 'get_file': gi.FunctionInfo(get_file), 'get_parent': gi.FunctionInfo(get_parent), 'get_section_type': gi.FunctionInfo(get_section_type), 'get_start_line': gi.FunctionInfo(get_start_line), 'get_start_position': gi.FunctionInfo(get_start_position), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GtkCssSection (3537891824)>'
    __info__ = StructInfo(CssSection)


