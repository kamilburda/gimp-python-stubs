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


class Gradient(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new_linear(x0:float, y0:float, x1:float, y1:float) -> Gtk.Gradient
        new_radial(x0:float, y0:float, radius0:float, x1:float, y1:float, radius1:float) -> Gtk.Gradient
    """
    def add_color_stop(self, offset, color): # real signature unknown; restored from __doc__
        """ add_color_stop(self, offset:float, color:Gtk.SymbolicColor) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def new_linear(cls, x0, y0, x1, y1): # real signature unknown; restored from __doc__
        """ new_linear(x0:float, y0:float, x1:float, y1:float) -> Gtk.Gradient """
        pass

    @classmethod
    def new_radial(cls, x0, y0, radius0, x1, y1, radius1): # real signature unknown; restored from __doc__
        """ new_radial(x0:float, y0:float, radius0:float, x1:float, y1:float, radius1:float) -> Gtk.Gradient """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.Gradient """
        pass

    def resolve(self, props): # real signature unknown; restored from __doc__
        """ resolve(self, props:Gtk.StyleProperties) -> bool, resolved_gradient:cairo.Pattern """
        return False

    def resolve_for_context(self, context): # real signature unknown; restored from __doc__
        """ resolve_for_context(self, context:Gtk.StyleContext) -> cairo.Pattern """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(Gradient), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkGradient (3537897584)>, '__dict__': <attribute '__dict__' of 'Gradient' objects>, '__weakref__': <attribute '__weakref__' of 'Gradient' objects>, '__doc__': None, 'new_linear': <classmethod(gi.FunctionInfo(new_linear))>, 'new_radial': <classmethod(gi.FunctionInfo(new_radial))>, 'add_color_stop': gi.FunctionInfo(add_color_stop), 'ref': gi.FunctionInfo(ref), 'resolve': gi.FunctionInfo(resolve), 'resolve_for_context': gi.FunctionInfo(resolve_for_context), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GtkGradient (3537897584)>'
    __info__ = StructInfo(Gradient)


