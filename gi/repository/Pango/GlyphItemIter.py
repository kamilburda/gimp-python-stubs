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


class GlyphItemIter(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        GlyphItemIter()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Pango.GlyphItemIter or None """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def init_end(self, glyph_item, text): # real signature unknown; restored from __doc__
        """ init_end(self, glyph_item:Pango.GlyphItem, text:str) -> bool """
        return False

    def init_start(self, glyph_item, text): # real signature unknown; restored from __doc__
        """ init_start(self, glyph_item:Pango.GlyphItem, text:str) -> bool """
        return False

    def next_cluster(self): # real signature unknown; restored from __doc__
        """ next_cluster(self) -> bool """
        return False

    def prev_cluster(self): # real signature unknown; restored from __doc__
        """ prev_cluster(self) -> bool """
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

    end_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_glyph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glyph_item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_glyph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GlyphItemIter), '__module__': 'gi.repository.Pango', '__gtype__': <GType PangoGlyphItemIter (843940320)>, '__dict__': <attribute '__dict__' of 'GlyphItemIter' objects>, '__weakref__': <attribute '__weakref__' of 'GlyphItemIter' objects>, '__doc__': None, 'glyph_item': <property object at 0x00000280355d4cc0>, 'text': <property object at 0x00000280355d4db0>, 'start_glyph': <property object at 0x00000280355d4ea0>, 'start_index': <property object at 0x00000280355d4f90>, 'start_char': <property object at 0x00000280355d5080>, 'end_glyph': <property object at 0x00000280355d5170>, 'end_index': <property object at 0x00000280355d5260>, 'end_char': <property object at 0x00000280355d5350>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'init_end': gi.FunctionInfo(init_end), 'init_start': gi.FunctionInfo(init_start), 'next_cluster': gi.FunctionInfo(next_cluster), 'prev_cluster': gi.FunctionInfo(prev_cluster)})"
    __gtype__ = None # (!) real value is '<GType PangoGlyphItemIter (843940320)>'
    __info__ = StructInfo(GlyphItemIter)


