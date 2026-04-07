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


class GlyphItem(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GlyphItem()
    """
    def apply_attrs(self, text, p_list): # real signature unknown; restored from __doc__
        """ apply_attrs(self, text:str, list:Pango.AttrList) -> list """
        return []

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.GlyphItem or None """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_logical_widths(self, text): # real signature unknown; restored from __doc__
        """ get_logical_widths(self, text:str) -> logical_widths:list """
        pass

    def letter_space(self, text, log_attrs, letter_spacing): # real signature unknown; restored from __doc__
        """ letter_space(self, text:str, log_attrs:list, letter_spacing:int) """
        pass

    def split(self, text, split_index): # real signature unknown; restored from __doc__
        """ split(self, text:str, split_index:int) -> Pango.GlyphItem or None """
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

    end_x_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glyphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_x_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GlyphItem), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoGlyphItem (843937824)>, '__dict__': <attribute '__dict__' of 'GlyphItem' objects>, '__weakref__': <attribute '__weakref__' of 'GlyphItem' objects>, '__doc__': None, 'item': <property object at 0x00000280355d47c0>, 'glyphs': <property object at 0x00000280355d48b0>, 'y_offset': <property object at 0x00000280355d49a0>, 'start_x_offset': <property object at 0x00000280355d4a90>, 'end_x_offset': <property object at 0x00000280355d4b80>, 'apply_attrs': gi.FunctionInfo(apply_attrs), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_logical_widths': gi.FunctionInfo(get_logical_widths), 'letter_space': gi.FunctionInfo(letter_space), 'split': gi.FunctionInfo(split)})"
    __gtype__ = None # (!) real value is '<GType PangoGlyphItem (843937824)>'
    __info__ = StructInfo(GlyphItem)


