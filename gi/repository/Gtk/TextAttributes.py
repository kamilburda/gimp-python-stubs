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


class TextAttributes(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        TextAttributes()
        new() -> Gtk.TextAttributes
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.TextAttributes """
        pass

    def copy_values(self, dest): # real signature unknown; restored from __doc__
        """ copy_values(self, dest:Gtk.TextAttributes) """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Gtk.TextAttributes """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gtk.TextAttributes """
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new() -> Gtk.TextAttributes """
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

    appearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bg_full_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    editable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    font_scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    indent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    invisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    language = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    left_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    letter_spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    no_fallback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pg_bg_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pg_bg_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels_above_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels_below_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixels_inside_wrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    refcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    right_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TextAttributes), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkTextAttributes (3414244944)>, '__dict__': <attribute '__dict__' of 'TextAttributes' objects>, '__weakref__': <attribute '__weakref__' of 'TextAttributes' objects>, '__doc__': None, 'refcount': <property object at 0x000002bfd3a0e930>, 'appearance': <property object at 0x000002bfd3a0ea20>, 'justification': <property object at 0x000002bfd3a0eb10>, 'direction': <property object at 0x000002bfd3a0ec00>, 'font': <property object at 0x000002bfd3a0ecf0>, 'font_scale': <property object at 0x000002bfd3a0ede0>, 'left_margin': <property object at 0x000002bfd3a0eed0>, 'right_margin': <property object at 0x000002bfd3a0efc0>, 'indent': <property object at 0x000002bfd3a0f0b0>, 'pixels_above_lines': <property object at 0x000002bfd3a0f1a0>, 'pixels_below_lines': <property object at 0x000002bfd3a0f290>, 'pixels_inside_wrap': <property object at 0x000002bfd3a0f380>, 'tabs': <property object at 0x000002bfd3a0f470>, 'wrap_mode': <property object at 0x000002bfd3a0f560>, 'language': <property object at 0x000002bfd3a0f650>, 'pg_bg_color': <property object at 0x000002bfd3a0f740>, 'invisible': <property object at 0x000002bfd3a0f830>, 'bg_full_height': <property object at 0x000002bfd3a0f920>, 'editable': <property object at 0x000002bfd3a0fa10>, 'no_fallback': <property object at 0x000002bfd3a0fb00>, 'pg_bg_rgba': <property object at 0x000002bfd3a0fbf0>, 'letter_spacing': <property object at 0x000002bfd3a0fce0>, 'new': <classmethod(gi.FunctionInfo(new))>, 'copy': gi.FunctionInfo(copy), 'copy_values': gi.FunctionInfo(copy_values), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x000002bfce305010>})"
    __gtype__ = None # (!) real value is '<GType GtkTextAttributes (3414244944)>'
    __info__ = StructInfo(TextAttributes)


