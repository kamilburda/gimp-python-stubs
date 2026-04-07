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


class StyleClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        StyleClass()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    clone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_arrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_box = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_box_gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_diamond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_expander = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_flat_box = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_focus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_hline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_option = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_resize_grip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_shadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_shadow_gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_slider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_spinner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_tab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw_vline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    init_from_rc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    realize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_background = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unrealize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(StyleClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'StyleClass' objects>, '__weakref__': <attribute '__weakref__' of 'StyleClass' objects>, '__doc__': None, 'parent_class': <property object at 0x000002bfd39fe8e0>, 'realize': <property object at 0x000002bfd39fe9d0>, 'unrealize': <property object at 0x000002bfd39feac0>, 'copy': <property object at 0x000002bfd39febb0>, 'clone': <property object at 0x000002bfd39feca0>, 'init_from_rc': <property object at 0x000002bfd39fed90>, 'set_background': <property object at 0x000002bfd39fee80>, 'render_icon': <property object at 0x000002bfd39fef70>, 'draw_hline': <property object at 0x000002bfd39ff060>, 'draw_vline': <property object at 0x000002bfd39ff150>, 'draw_shadow': <property object at 0x000002bfd39ff240>, 'draw_arrow': <property object at 0x000002bfd39ff330>, 'draw_diamond': <property object at 0x000002bfd39ff420>, 'draw_box': <property object at 0x000002bfd39ff510>, 'draw_flat_box': <property object at 0x000002bfd39ff600>, 'draw_check': <property object at 0x000002bfd39ff6f0>, 'draw_option': <property object at 0x000002bfd39ff7e0>, 'draw_tab': <property object at 0x000002bfd39ff8d0>, 'draw_shadow_gap': <property object at 0x000002bfd39ff9c0>, 'draw_box_gap': <property object at 0x000002bfd39ffab0>, 'draw_extension': <property object at 0x000002bfd39ffba0>, 'draw_focus': <property object at 0x000002bfd39ffc90>, 'draw_slider': <property object at 0x000002bfd39ffd80>, 'draw_handle': <property object at 0x000002bfd39ffe70>, 'draw_expander': <property object at 0x000002bfd39fff60>, 'draw_layout': <property object at 0x000002bfd3a00090>, 'draw_resize_grip': <property object at 0x000002bfd3a00180>, 'draw_spinner': <property object at 0x000002bfd3a00270>, '_gtk_reserved1': <property object at 0x000002bfd3a00360>, '_gtk_reserved2': <property object at 0x000002bfd3a00450>, '_gtk_reserved3': <property object at 0x000002bfd3a00540>, '_gtk_reserved4': <property object at 0x000002bfd3a00630>, '_gtk_reserved5': <property object at 0x000002bfd3a00720>, '_gtk_reserved6': <property object at 0x000002bfd3a00810>, '_gtk_reserved7': <property object at 0x000002bfd3a00900>, '_gtk_reserved8': <property object at 0x000002bfd3a009f0>, '_gtk_reserved9': <property object at 0x000002bfd3a00ae0>, '_gtk_reserved10': <property object at 0x000002bfd3a00bd0>, '_gtk_reserved11': <property object at 0x000002bfd3a00cc0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(StyleClass)


