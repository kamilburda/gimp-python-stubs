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


class ColorDisplayClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ColorDisplayClass()
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

    changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    configure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    convert_buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    help_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    icon_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ColorDisplayClass), '__module__': 'gi.repository.GimpUi', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ColorDisplayClass' objects>, '__weakref__': <attribute '__weakref__' of 'ColorDisplayClass' objects>, '__doc__': None, 'parent_class': <property object at 0x0000020ee1d30a40>, 'name': <property object at 0x0000020ee1d30b30>, 'help_id': <property object at 0x0000020ee1d30c20>, 'icon_name': <property object at 0x0000020ee1d30d10>, 'convert_buffer': <property object at 0x0000020ee1d30e00>, 'configure': <property object at 0x0000020ee1d30ef0>, 'changed': <property object at 0x0000020ee1d30fe0>, '_gimp_reserved0': <property object at 0x0000020ee1d310d0>, '_gimp_reserved1': <property object at 0x0000020ee1d311c0>, '_gimp_reserved2': <property object at 0x0000020ee1d312b0>, '_gimp_reserved3': <property object at 0x0000020ee1d313a0>, '_gimp_reserved4': <property object at 0x0000020ee1d31490>, '_gimp_reserved5': <property object at 0x0000020ee1d31580>, '_gimp_reserved6': <property object at 0x0000020ee1d31670>, '_gimp_reserved7': <property object at 0x0000020ee1d31760>, '_gimp_reserved8': <property object at 0x0000020ee1d31850>, '_gimp_reserved9': <property object at 0x0000020ee1d31940>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ColorDisplayClass)


