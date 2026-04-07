# encoding: utf-8
# module gi.repository.Gdk
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gi._gi as __gi__gi
import gobject as __gobject


from .RGBA import RGBA

class RGBA(RGBA):
    """
    :Constructors:
    
    ::
    
        RGBA()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gdk.RGBA """
        pass

    def equal(self, p2): # real signature unknown; restored from __doc__
        """ equal(self, p2:Gdk.RGBA) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    @classmethod
    def from_color(cls, *args, **kwargs): # real signature unknown
        """ Returns a new RGBA instance given a Color instance. """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def parse(self, spec): # real signature unknown; restored from __doc__
        """ parse(self, spec:str) -> bool """
        return False

    def to_color(self): # reliably restored by inspect
        """ Converts this RGBA into a Color instance which excludes alpha. """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
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

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, red=1.0, green=1.0, blue=1.0, alpha=1.0): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        """ Iterator which allows easy conversion to tuple and list types. """
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

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
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

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', '__init__': <function RGBA.__init__ at 0x000001872518aac0>, '__eq__': <function RGBA.__eq__ at 0x000001872518ab60>, '__ne__': <function RGBA.__ne__ at 0x000001872518ac00>, '__repr__': <function RGBA.__repr__ at 0x000001872518aca0>, '__iter__': <function RGBA.__iter__ at 0x000001872518ad40>, 'to_color': <function RGBA.to_color at 0x000001872518ade0>, 'from_color': <classmethod(<function RGBA.from_color at 0x000001872518ae80>)>, '__doc__': None, '__hash__': None})"
    __gtype__ = None # (!) real value is '<GType GdkRGBA (585151488)>'
    __hash__ = None
    __info__ = StructInfo(RGBA)


