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


class ToolShell(__gobject.GInterface):
    # no doc
    def get_ellipsize_mode(self): # real signature unknown; restored from __doc__
        """ get_ellipsize_mode(self) -> Pango.EllipsizeMode """
        pass

    def get_icon_size(self): # real signature unknown; restored from __doc__
        """ get_icon_size(self) -> int """
        return 0

    def get_orientation(self): # real signature unknown; restored from __doc__
        """ get_orientation(self) -> Gtk.Orientation """
        pass

    def get_relief_style(self): # real signature unknown; restored from __doc__
        """ get_relief_style(self) -> Gtk.ReliefStyle """
        pass

    def get_style(self): # real signature unknown; restored from __doc__
        """ get_style(self) -> Gtk.ToolbarStyle """
        pass

    def get_text_alignment(self): # real signature unknown; restored from __doc__
        """ get_text_alignment(self) -> float """
        return 0.0

    def get_text_orientation(self): # real signature unknown; restored from __doc__
        """ get_text_orientation(self) -> Gtk.Orientation """
        pass

    def get_text_size_group(self): # real signature unknown; restored from __doc__
        """ get_text_size_group(self) -> Gtk.SizeGroup """
        pass

    def rebuild_menu(self): # real signature unknown; restored from __doc__
        """ rebuild_menu(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ToolShell), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkToolShell (3414248112)>, '__dict__': <attribute '__dict__' of 'ToolShell' objects>, '__weakref__': <attribute '__weakref__' of 'ToolShell' objects>, '__doc__': None, '__gsignals__': {}, 'get_ellipsize_mode': gi.FunctionInfo(get_ellipsize_mode), 'get_icon_size': gi.FunctionInfo(get_icon_size), 'get_orientation': gi.FunctionInfo(get_orientation), 'get_relief_style': gi.FunctionInfo(get_relief_style), 'get_style': gi.FunctionInfo(get_style), 'get_text_alignment': gi.FunctionInfo(get_text_alignment), 'get_text_orientation': gi.FunctionInfo(get_text_orientation), 'get_text_size_group': gi.FunctionInfo(get_text_size_group), 'rebuild_menu': gi.FunctionInfo(rebuild_menu)})"
    __gdoc__ = 'Interface GtkToolShell\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkToolShell (3414248112)>'
    __info__ = InterfaceInfo(ToolShell)


