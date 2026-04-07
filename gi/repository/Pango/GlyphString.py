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


class GlyphString(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GlyphString()
        new() -> Pango.GlyphString
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.GlyphString or None """
        pass

    def extents(self, font): # real signature unknown; restored from __doc__
        """ extents(self, font:Pango.Font) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def extents_range(self, start, end, font): # real signature unknown; restored from __doc__
        """ extents_range(self, start:int, end:int, font:Pango.Font) -> ink_rect:Pango.Rectangle, logical_rect:Pango.Rectangle """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_logical_widths(self, text, length, embedding_level): # real signature unknown; restored from __doc__
        """ get_logical_widths(self, text:str, length:int, embedding_level:int) -> logical_widths:list """
        pass

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def index_to_x(self, text, length, analysis, index_, trailing): # real signature unknown; restored from __doc__
        """ index_to_x(self, text:str, length:int, analysis:Pango.Analysis, index_:int, trailing:bool) -> x_pos:int """
        pass

    def index_to_x_full(self, text, length, analysis, attrs=None, index_, trailing): # real signature unknown; restored from __doc__
        """ index_to_x_full(self, text:str, length:int, analysis:Pango.Analysis, attrs:Pango.LogAttr=None, index_:int, trailing:bool) -> x_pos:int """
        pass

    @classmethod
    def new(cls): # real signature unknown; restored from __doc__
        """ new() -> Pango.GlyphString """
        pass

    def set_size(self, new_len): # real signature unknown; restored from __doc__
        """ set_size(self, new_len:int) """
        pass

    def x_to_index(self, text, length, analysis, x_pos): # real signature unknown; restored from __doc__
        """ x_to_index(self, text:str, length:int, analysis:Pango.Analysis, x_pos:int) -> index_:int, trailing:int """
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
        """ new() -> Pango.GlyphString """
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

    glyphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    log_clusters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_glyphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GlyphString), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoGlyphString (843940704)>, '__dict__': <attribute '__dict__' of 'GlyphString' objects>, '__weakref__': <attribute '__weakref__' of 'GlyphString' objects>, '__doc__': None, 'num_glyphs': <property object at 0x00000280355d5490>, 'glyphs': <property object at 0x00000280355d5580>, 'log_clusters': <property object at 0x00000280355d5670>, 'space': <property object at 0x00000280355d5760>, 'new': <classmethod(gi.FunctionInfo(new))>, 'copy': gi.FunctionInfo(copy), 'extents': gi.FunctionInfo(extents), 'extents_range': gi.FunctionInfo(extents_range), 'free': gi.FunctionInfo(free), 'get_logical_widths': gi.FunctionInfo(get_logical_widths), 'get_width': gi.FunctionInfo(get_width), 'index_to_x': gi.FunctionInfo(index_to_x), 'index_to_x_full': gi.FunctionInfo(index_to_x_full), 'set_size': gi.FunctionInfo(set_size), 'x_to_index': gi.FunctionInfo(x_to_index), '__new__': <staticmethod(gi.FunctionInfo(new))>, '__init__': <function nothing at 0x0000028034ff1010>})"
    __gtype__ = None # (!) real value is '<GType PangoGlyphString (843940704)>'
    __info__ = StructInfo(GlyphString)


