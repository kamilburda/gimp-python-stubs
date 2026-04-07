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


from .IconSet import IconSet

class IconSet(IconSet):
    """
    :Constructors:
    
    ::
    
        new() -> Gtk.IconSet
        new_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gtk.IconSet
    """
    def add_source(self, source): # real signature unknown; restored from __doc__
        """ add_source(self, source:Gtk.IconSource) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.IconSet """
        pass

    def get_sizes(self): # real signature unknown; restored from __doc__
        """ get_sizes(self) -> sizes:list """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gtk.IconSet """
        pass

    def new_from_pixbuf(self, pixbuf): # real signature unknown; restored from __doc__
        """ new_from_pixbuf(pixbuf:GdkPixbuf.Pixbuf) -> Gtk.IconSet """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.IconSet """
        pass

    def render_icon(self, style=None, direction, state, size, widget=None, detail=None): # real signature unknown; restored from __doc__
        """ render_icon(self, style:Gtk.Style=None, direction:Gtk.TextDirection, state:Gtk.StateType, size:int, widget:Gtk.Widget=None, detail:str=None) -> GdkPixbuf.Pixbuf """
        pass

    def render_icon_pixbuf(self, context, size): # real signature unknown; restored from __doc__
        """ render_icon_pixbuf(self, context:Gtk.StyleContext, size:int) -> GdkPixbuf.Pixbuf """
        pass

    def render_icon_surface(self, context, size, scale, for_window=None): # real signature unknown; restored from __doc__
        """ render_icon_surface(self, context:Gtk.StyleContext, size:int, scale:int, for_window:Gdk.Window=None) -> cairo.Surface """
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

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(cls, pixbuf=None): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__firstlineno__': 1749, '__new__': <staticmethod(<function IconSet.__new__ at 0x000002bfcebc92d0>)>, '__init__': <function IconSet.__init__ at 0x000002bfcebc9380>, '__static_attributes__': (), '__doc__': None})"
    __firstlineno__ = 1749
    __gtype__ = None # (!) real value is '<GType GtkIconSet (3426611632)>'
    __info__ = StructInfo(IconSet)
    __static_attributes__ = ()


