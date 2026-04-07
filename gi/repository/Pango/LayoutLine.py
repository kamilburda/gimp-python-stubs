# encoding: utf-8
# module gi.repository.Pango
# by generator 1.147
# no doc

# imports
from _thread import _lock

import gi as __gi
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi._gi as __gi__gi


class LayoutLine(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        LayoutLine()
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_extents(self): # real signature unknown; restored from __doc__
        """ get_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> height:int """
        pass

    def get_length(self): # real signature unknown; restored from __doc__
        """ get_length(self) -> int """
        return 0

    def get_pixel_extents(self): # real signature unknown; restored from __doc__
        """ get_pixel_extents(self) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def get_resolved_direction(self): # real signature unknown; restored from __doc__
        """ get_resolved_direction(self) -> Pango.Direction """
        pass

    def get_start_index(self): # real signature unknown; restored from __doc__
        """ get_start_index(self) -> int """
        return 0

    def get_x_ranges(self, start_index, end_index): # real signature unknown; restored from __doc__
        """ get_x_ranges(self, start_index:int, end_index:int) -> ranges:list """
        pass

    def index_to_x(self, index_, trailing): # real signature unknown; restored from __doc__
        """ index_to_x(self, index_:int, trailing:bool) -> x_pos:int """
        pass

    def is_paragraph_start(self): # real signature unknown; restored from __doc__
        """ is_paragraph_start(self) -> bool """
        return False

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Pango.LayoutLine or None """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
        pass

    def x_to_index(self, x_pos): # real signature unknown; restored from __doc__
        """ x_to_index(self, x_pos:int) -> bool, index_:int, trailing:int """
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

    layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    resolved_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    runs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LayoutLine), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoLayoutLine (843936384)>, '__dict__': <attribute '__dict__' of 'LayoutLine' objects>, '__weakref__': <attribute '__weakref__' of 'LayoutLine' objects>, '__doc__': None, 'layout': <property object at 0x00000280355d6340>, 'start_index': <property object at 0x00000280355d6430>, 'length': <property object at 0x00000280355d6520>, 'runs': <property object at 0x00000280355d6610>, 'is_paragraph_start': gi.FunctionInfo(is_paragraph_start), 'resolved_dir': <property object at 0x00000280355d67f0>, 'get_extents': gi.FunctionInfo(get_extents), 'get_height': gi.FunctionInfo(get_height), 'get_length': gi.FunctionInfo(get_length), 'get_pixel_extents': gi.FunctionInfo(get_pixel_extents), 'get_resolved_direction': gi.FunctionInfo(get_resolved_direction), 'get_start_index': gi.FunctionInfo(get_start_index), 'get_x_ranges': gi.FunctionInfo(get_x_ranges), 'index_to_x': gi.FunctionInfo(index_to_x), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), 'x_to_index': gi.FunctionInfo(x_to_index)})"
    __gtype__ = None # (!) real value is '<GType PangoLayoutLine (843936384)>'
    __info__ = StructInfo(LayoutLine)


