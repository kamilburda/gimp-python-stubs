# encoding: utf-8
# module gi.repository.GimpUi
# by generator 1.147
# no doc

# imports
from _thread import _lock

import enum as __enum
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gimp as __gi_repository_Gimp
import gi.repository.Gtk as __gi_repository_Gtk
import gi._gi as __gi__gi


class ColorSelectorClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ColorSelectorClass()
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

    channel_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    color_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    help_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    model_visible_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_channel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_config = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_model_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_show_alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_simulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_toggles_sensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_toggles_visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    simulation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved7 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gimp_reserved9 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorSelectorClass), '__module__': 'gi.repository.GimpUi', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ColorSelectorClass' objects>, '__weakref__': <attribute '__weakref__' of 'ColorSelectorClass' objects>, '__doc__': None, 'parent_class': <property object at 0x0000020ee1d33e70>, 'name': <property object at 0x0000020ee1d33d80>, 'help_id': <property object at 0x0000020ee1d33c90>, 'icon_name': <property object at 0x0000020ee1d33fb0>, 'set_toggles_visible': <property object at 0x0000020ee1d240e0>, 'set_toggles_sensitive': <property object at 0x0000020ee1d241d0>, 'set_show_alpha': <property object at 0x0000020ee1d242c0>, 'set_color': <property object at 0x0000020ee1d243b0>, 'set_channel': <property object at 0x0000020ee1d244a0>, 'set_model_visible': <property object at 0x0000020ee1d24590>, 'set_config': <property object at 0x0000020ee1d24680>, 'set_format': <property object at 0x0000020ee1d24770>, 'set_simulation': <property object at 0x0000020ee1d24860>, 'color_changed': <property object at 0x0000020ee1d24950>, 'channel_changed': <property object at 0x0000020ee1d24a40>, 'model_visible_changed': <property object at 0x0000020ee1d24b30>, 'simulation': <property object at 0x0000020ee1d24c20>, '_gimp_reserved0': <property object at 0x0000020ee1d24d10>, '_gimp_reserved1': <property object at 0x0000020ee1d24e00>, '_gimp_reserved2': <property object at 0x0000020ee1d24ef0>, '_gimp_reserved3': <property object at 0x0000020ee1d24fe0>, '_gimp_reserved4': <property object at 0x0000020ee1d250d0>, '_gimp_reserved5': <property object at 0x0000020ee1d251c0>, '_gimp_reserved6': <property object at 0x0000020ee1d252b0>, '_gimp_reserved7': <property object at 0x0000020ee1d253a0>, '_gimp_reserved8': <property object at 0x0000020ee1d25490>, '_gimp_reserved9': <property object at 0x0000020ee1d25580>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ColorSelectorClass)


